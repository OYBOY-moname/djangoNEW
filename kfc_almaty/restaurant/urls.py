from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('payment/', views.payment, name='payment'),
    path('delivery/', views.delivery, name='delivery'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
