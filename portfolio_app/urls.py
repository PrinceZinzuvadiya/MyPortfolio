from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact, name='contact'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
