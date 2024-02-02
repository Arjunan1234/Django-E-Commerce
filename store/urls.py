from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'store'


urlpatterns = [
    path('', views.home, name="home"),
     path('accounts/register/', views.RegistrationView.as_view(), name="register"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
   
    path('accounts/add-address/', views.AddressView.as_view(), name="add-address"),
    
   path('accounts/logout/', views.LogoutPage,name="logout"),
]