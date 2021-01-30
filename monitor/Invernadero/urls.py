from django.urls import path

from . import views

app_name = "invernadero"

urlpatterns = [
    path("", views.index, name="index"),
    path("historico", views.historico, name="historico")
]