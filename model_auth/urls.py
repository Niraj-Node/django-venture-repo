from django.urls import path
from . import views

app_name = "model_auth"

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("", views.home, name="home"),
    path("logout", views.logout_request, name="logout"),
]