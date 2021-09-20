from django.urls import path
from django.contrib.auth.views import auth_login, logout_then_login


from . import views

app_name = "invernadero"

urlpatterns = [
    path("", views.index, name="index"),
    path("historico", views.historico, name="historico"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
