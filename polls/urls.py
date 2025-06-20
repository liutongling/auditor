from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("idx/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("registeridx/", views.registeridx, name="registeridx"),
    path("register/", views.register, name="register"),
    path('g/', views.g),
]