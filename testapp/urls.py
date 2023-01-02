"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('base',views.base,name="base"),
    # path('msgs',views.msgs,name="msgs"),
    # path('demo/',views.demo,name="demo"),
    path('machin1',views.first_machine,name="machin1"),
    path('machin2',views.second_machine,name="machin2"),
    path('home/',views.home,name="home"),
    path('tables/',views.data_tabel,name="tables"),
    path('charts/',views.charts,name="charts"),

    path('', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    
    
    # reset password urls
    # path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    
    
    
    
 
    
    # urls masters
    # alert_masters 
    path('alert_details/', views.alert_details, name='alert_details'),
    path('add_alertmaster/', views.add_alertmaster, name='add_alertmaster'),
    path('updatealert/<int:id>/', views.update_alert, name='update_alert'),
    path('del/<int:id>/', views.delete_alert, name='delete_alert'),
    
    # device_detials 
    path('device_details/', views.device_details, name='device_details'),
    path('add_device/', views.add_device, name='add_device'),
    path('updatedevice/<int:id>/', views.update_device, name='update_device'),
    path('dele/<int:id>/', views.delete_device, name='delete_device'),

    # company_info
    path('company/', views.company, name='company'),
    path('add_company/', views.add_company, name='add_company'),
    path('updateinfo/<int:id>/', views.update_data, name='updatedata'),
    path('delet/<int:id>/', views.delete_data, name='deletedata'),
    
    # user_details 
    path('user_details/', views.user_details, name='user_details'),
    path('add_user/', views.add_user, name='add_user'),
    path('updateuser/<int:id>/', views.update_user, name='update_user'),
    path('deletes/<int:id>/', views.deleteuser, name='deleteuser'),
   
   
   
   
   
   

# demo template (only for practice )
    # path('temp_one/', views.temp_one, name='temp_one'),
    
    # dynamic url asel id integer mde yete <int:(conveter)id>
    

]