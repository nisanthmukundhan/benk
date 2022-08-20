from django.urls import path

from credentials import views



urlpatterns = [

    path('registertest', views.registertest, name='registertest'),
    path('logintest', views.logintest, name='logintest'),
    path('logouttest', views.logouttest, name='logouttest'),
]
