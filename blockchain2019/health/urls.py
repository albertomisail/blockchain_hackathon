from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('dashboard/<int:client_id>/', views.dashboard, name='dashboard'),
    path('checkup/<int:client_id>/', views.checkup, name='checkup'),
    # path('payment/<int:client_id>/', views.payment, name='payment'),
]
