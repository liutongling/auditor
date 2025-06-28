
from django.urls import include, path
from . import views

urlpatterns = [

    path("idx/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("registeridx/", views.registeridx, name="registeridx"),
    path("register/", views.register, name="register"),
    path("Academy/", views.AcademyAdd, name="Academy"),
    path('g/', views.g),
    path('delete/',views.delete,name="delete"),
    # 访问查看成员资料页面
    path('view/',views.view,name="view"),
    path('addP/',views.addP,name="addP"),
]