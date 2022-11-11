from django.urls import path
from . import views
urlpatterns=[
    path('', views.registerpage),
    path('adminlogin/',views.adminlogin),
    path('userlogin/',views.userlogin),

]


