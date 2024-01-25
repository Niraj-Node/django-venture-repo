from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registration_view, name='registration')
]