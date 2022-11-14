from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('index', views.index, name='home'),
    path('tpo', views.tpo, name='tpo'),
    path('tpoLogin', views.tpoLogin, name='tpoLogin'),
    path('tpoLogout', views.tpoLogout, name='tpoLogout'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('studentDash', views.studentDash, name='student'),
    path('adminDash', views.adminDash, name='adminDash'),
    path('updateStudentDetails', views.updateStudentDetails, name='updateStudentDetails'),
    path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),
]
