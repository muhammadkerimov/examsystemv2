from django.urls import path , include
from . import views
urlpatterns = [
    path('student/regnewchild',views.register,name='register'),
    path('student/login',views.login,name='login'),
    path('student/main',views.main,name='main'),
    path('student/exams',views.exams,name='exams'),
    path('student/logout',views.logout,name='logout'),
    path('student/startexam',views.examstart,name='startexam'),
    path('student/result',views.result,name='result')
]

handler404 = views.handler404