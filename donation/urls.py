from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_list, name='donation_list'),
    path('donation/<int:pk>/', views.donation_details, name='donation_details'),
    path('donation/new/', views.donation_new, name='donation_new'),
    path('donation/signup/', views.sign_up, name='signup'),
]