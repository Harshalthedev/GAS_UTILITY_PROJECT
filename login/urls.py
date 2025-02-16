from django.urls import path
from . import views
from .views import  customer_login, customer_dashboard, admin_login, forget_password, customer_dashboard



urlpatterns = [
    path('',views.authlogin,name='login'),
    path('customer_login/', customer_login, name='customer_login'),  # `/customer_login/`
    path('admin/', admin_login, name='admin_login'),  # `/customer_login/`
    path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
    path('registration/', views.registration, name='registration'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('logout/', views.authlogout, name='logout'), 
    ]


