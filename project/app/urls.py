from django.urls import path
from app import views

urlpatterns = [
    path("", views.sign_up, name="signup"),
    path("index", views.index, name="index"),
    path("login", views.log_In, name="login"),
    path("signup", views.sign_up, name="signup"),
    path("logout", views.log_out, name="logout"),
]
