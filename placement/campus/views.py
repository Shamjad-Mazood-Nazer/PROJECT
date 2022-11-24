from hashlib import sha256

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.sites import requests
from django.views import View
from .forms import *

from django.template import loader

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm, LoginForm
from .decorators import user_login_required
import random
from placement.settings import EMAIL_HOST_USER

User = get_user_model()


# Create your views here.

def ajax_generate_code(request):
    print(request.GET)
    for x in request.GET:
        if x != '_':
            email = x
            ## Generate Code and save it in a session
            request.session['code'] = random.randint(111111, 999999)
            ## Send email Functionality
            text_content = "Your Email Verification Code for Placement-Cell Registration is " + str(
                request.session['code'])
            msg = EmailMultiAlternatives('Verify Email', text_content, EMAIL_HOST_USER, [email])
            msg.send()
    return HttpResponse("success")


# def activateEmail(request, user, to_email):
#     mail_subject = "Activate your user account."
#     messages = render_to_string()


def register(request):
    form = RegisterForm()
    # is_private = request.POST.get('is_private', False)
    success = None
    if request.method == 'POST':
        if StudentReg.objects.filter(admino=request.POST['admino']).exists():
            error = "This Admission number is already taken"
            return render(request, 'campus/register.html', {'form': form, 'error': error})

        if StudentReg.objects.filter(email=request.POST['email']).exists():
            error = "This email is already taken"
            return render(request, 'campus/register.html', {'form': form, 'error': error})

        ## Check Verification Code
        if (not 'code' in request.POST) or (not 'code' in request.session) or (
                not request.POST['code'] == str(request.session['code'])):
            error = "Invalid Verification Code"
            return render(request, 'campus/register.html', {'form': form, 'error': error})
            ## Safe to go
        form = RegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "New User Created Successfully, You may go back and try to login !"
    return render(request, 'campus/register.html', {'form': form, 'success': success})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if StudentReg.objects.filter(email=email, password=password).exists():
            user = StudentReg.objects.filter(email=email)
            for std in user:
                email = std.email
                id = std.admino
                print(email)
                request.session['email'] = std.email
                # This is a session variable and will remain existing as long as you don't delete this manually or clear your browser cache
                request.session['admino'] = std.admino
                return redirect('student')
        return render(request, 'campus/login.html', {'form': form})
    else:
        return render(request, 'campus/login.html', {'form': form})


def tpoLogin(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Tpo.objects.filter(tpoMail=email, tpoPassword=password).exists():
            user = Tpo.objects.get(tpoMail=email)
            request.session[
                'tpoMail'] = user.tpoMail  # This is a session variable and will remain existing as long as you don't delete this manually or clear your browser cache
            return redirect('adminDash')
        return render(request, 'campus/adminLogin.html', {'form': form})
    else:
        return render(request, 'campus/adminLogin.html', {'form': form})


def get_admin(request):
    return Tpo.objects.get(tpoMail=request.session['tpoMail'])


@login_required(login_url='tpoLogin')
def adminDash(request):
    user = get_admin(request)
    return render(request, 'campus/adminDashboard.html', {'user': user})


def tpoLogout(request):
    if 'email' in request.session:
        del request.session['email']  # delete user session
    return redirect('tpo')


def get_user(request):
    # request.session['admino']=13312
    return StudentReg.objects.get(email=request.session['email'])


def home(request):
    if 'email' in request.session:
        user = get_user(request)
        return render(request, 'campus/studentDashboard.html', {'user': user})
    else:
        return render(request, 'campus/login.html')


@user_login_required
def studentDash(request):
    user = get_user(request)
    myData = StudentReg.objects.filter(admino=user.admino)
    # print(myData)
    return render(request, 'campus/studentDashboard.html', {'user': user, 'myData': myData})


# def logout(request):
#     if 'email' in request.session:
#         request.session.clear()  # delete user session
#     return redirect('login')


def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return render(request, "campus/login.html")


def tpo(request):
    return render(request, 'campus/adminLogin.html')


# def studentDash(request):
#     return render(request, 'campus/studentDashboard.html')

# @user_login_required()
def updateStudentDetails(request):
    form = MCAStudentDetails()
    # is_private = request.POST.get('is_private', False)
    success = None
    if request.method == 'POST':
        form = MCAStudentDetails(request.POST)
        if form.is_valid():
            data = form.save()
            form.save()
        success = "Updated Successfully !"
    return render(request, 'campus/studentForm.html', {'form': form, 'success': success})


# def adminDash(request):
#     return render(request, 'campus/adminDashboard.html')


@login_required(login_url='login')
def password_change(request):
    user = request.user
    form = SetPasswordForm(user)
    return render(request, 'password_reset_form.html', {'form': form})


def viewDrive(request):
    user = get_user(request)
    viewDrive = Drives.objects.all()
    myData = StudentReg.objects.get(email=user.email)
    return render(request, 'campus/viewDrive.html', {'myData': myData, 'viewDrive': viewDrive})


class applyDrive(View):
    def get(self, request, drive_id):
        sid = request.session.get('email')
        print(sid)
        job = ApplyDrive.objects.get(id=drive_id)
        add = ApplyDrive(email=sid, job_id=job)
        add.save()

        return HttpResponse("<script>alert('Applied Successful!');window.location='/viewDrive';</script>")