from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('tpo', views.tpo, name='tpo'),
    path('tpoLogin', views.tpoLogin, name='tpoLogin'),
    path('adminDash', views.adminDash, name='adminDash'),
    path('tpoLogout', views.tpoLogout, name='tpoLogout'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('studentDash', views.studentDash, name='student'),
    path('viewDrive', views.viewDrive, name='viewDrive'),
    # path('updateStudentDetails', views.updateStudentDetails, name='updateStudentDetails'),
    path('logout', views.logout, name='logout'),

    path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='campus/password_reset.html'),
         name='reset_password'
    ),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='campus/password_reset_sent.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/token/',
         auth_views.PasswordResetConfirmView.as_view(template_name='campus/password_reset_form.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='campus/password_reset_done.html'),
         name='password_reset_complete'),
]
