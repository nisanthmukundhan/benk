from django.urls import path
from . import views

app_name = 'bankapp'
urlpatterns = [

    path('register', views.register, name='register'),
    path('registerform/', views.registerform, name='registerform'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.navbar, name='navbar'),
    path('district/', views.districtdetail, name='districtdetail'),
    path('<slug:d_slug>/', views.districtdetail, name='d_by_details'),
    path('<slug:d_slug/<slug:b_slug/',views.branchdetail,name='bdetail'),



    path('account/', views.accountdetail, name='accountdetail'),
    path('<slug:d_slug>/', views.accountdetail, name='a_by_details'),
    path('meterial/', views.meterialdetails, name='meterialdetails'),
    path('<slug:m_slug>/', views.meterialdetail, name='m_by_details'),

]
