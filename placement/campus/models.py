from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

User = settings.AUTH_USER_MODEL


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tpo = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)


class StudentReg(models.Model):
    admino = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=500, unique=True, default='youremail@gmail.com')
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


# class StudentReg(models.Model):
#     admino = models.CharField(max_length=5, unique=True, default=None)
#     email = models.EmailField(max_length=100, unique=True, null=True)
#     password = models.CharField(max_length=30, null=True)
#
#     def __str__(self):
#         return self.admino


class MCAStudentDetails(models.Model):
    branch = (
        ('mca', 'MCA'),
        ('intmca', 'INT MCA'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )

    first_name = models.OneToOneField(StudentReg, null=False, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50, choices=branch)
    DoB = models.DateTimeField(max_length=10)
    gender = models.CharField(max_length=6, choices=gender)
    mobileNoIndian = models.CharField(max_length=10)
    alternativeNo = models.CharField(max_length=15)
    personalMail = models.CharField(max_length=200)
    collegeMail = models.CharField(max_length=200)
    fatherName = models.CharField(max_length=50)
    fatherNo = models.CharField(max_length=15)
    motherName = models.CharField(max_length=30)
    motherNo = models.CharField(max_length=15)
    fullAddress = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    nationality = models.CharField(max_length=15)
    planAfterGraduate = models.CharField(max_length=15)
    sslcPer = models.FloatField(max_length=5)
    sslcYoP = models.CharField(max_length=4)
    sslcBoard = models.CharField(max_length=35)
    hsePer = models.CharField(max_length=5)
    hseYoP = models.CharField(max_length=4)
    hseBoard = models.CharField(max_length=30)
    nameOfUG = models.CharField(max_length=10)
    ugPer = models.CharField(max_length=5)
    ugCgpa = models.CharField(max_length=5)
    ugYoP = models.CharField(max_length=4)
    collegeNameUg = models.CharField(max_length=50)
    ugUniversity = models.CharField(max_length=50)
    entranceRank = models.CharField(max_length=6)
    mcaAggregateCgpa = models.CharField(max_length=4)
    activeArrears = models.CharField(max_length=2)
    historyOfArrears = models.CharField(max_length=2)
    examsNotAttended = models.CharField(max_length=2)
    pgUniversity = models.CharField(max_length=50)
    technicalSkills = models.CharField(max_length=500)
    certifications = models.CharField(max_length=500)
    internships = models.CharField(max_length=500)
    workExperience = models.CharField(max_length=500)
    projectGithub = models.CharField(max_length=500)
    linkedIn = models.CharField(max_length=500)
    achievement = models.CharField(max_length=500)
    languagesKnown = models.CharField(max_length=500)

    def __str__(self):
        return self.branch


class BTechStudentDetails(models.Model):
    branch = (
        ('it', 'information_technology'),
        ('me', 'mech'),
        ('ce', 'civil'),
        ('eee', 'eee'),
        ('ece', 'ece'),
        ('ch', 'chemical'),
        ('cse', 'cse'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )

    branch = models.CharField(max_length=50, choices=branch)
    DoB = models.DateTimeField(max_length=10)
    gender = models.CharField(max_length=6, choices=gender)
    mobileNoIndian = models.CharField(max_length=10)
    alternativeNo = models.CharField(max_length=15)
    personalMail = models.CharField(max_length=200)
    collegeMail = models.CharField(max_length=200)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=30)
    motherNo = models.CharField(max_length=15)
    fatherNo = models.CharField(max_length=15)
    fullAddress = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    nationality = models.CharField(max_length=15)
    planAfterGraduate = models.CharField(max_length=15)
    sslcPer = models.FloatField(max_length=5)
    sslcYoP = models.CharField(max_length=4)
    sslcBoard = models.CharField(max_length=35)
    hsePer = models.CharField(max_length=5)
    hseYoP = models.CharField(max_length=4)
    hseBoard = models.CharField(max_length=30)
    ugUniversity = models.CharField(max_length=50)
    entranceRank = models.CharField(max_length=6)
    AggregateCgpa = models.CharField(max_length=4)
    activeArrears = models.CharField(max_length=2)
    historyOfArrears = models.CharField(max_length=2)
    examsNotAttended = models.CharField(max_length=2)
    technicalSkills = models.CharField(max_length=500)
    certifications = models.CharField(max_length=500)
    internships = models.CharField(max_length=500)
    workExperience = models.CharField(max_length=500)
    projectGithub = models.CharField(max_length=500)
    linkedIn = models.CharField(max_length=500)
    achievement = models.CharField(max_length=500)
    languagesKnown = models.CharField(max_length=500)

    def __str__(self):
        return self.branch


class Tpo(models.Model):
    tpoName = models.CharField(max_length=50)
    tpoMail = models.EmailField(max_length=75)
    tpoPassword = models.CharField(max_length=30)

    def __str__(self):
        return self.tpoName;
