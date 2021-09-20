from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Lectura
from . import util
from serial.serialutil import SerialException

from .models import Lectura

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("invernadero:login"))
    else:
        try:
            datos = util.leer_datos()
            lectura = Lectura(temperatura=float(datos[0]),
                              humedad=float(datos[1]), intensidad_luz=float(datos[2]),
                              datetime=util.get_datetime())
            lectura.save()
            return render(request, "invernadero/index.html", {
                "datos": util.leer_datos(), "fecha": util.get_date()
            })
        except SerialException:
            return render(request, "invernadero/error.html", {
                "mensaje": "Asegurese de que el dispositivo este conectado"
            })
        except:
            return render(request, "invernadero/error.html", {
                "mensaje": "Algo salio mal :("
            })


def historico(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("invernadero:login"))
    else:
        try:
            lecturas = Lectura.objects.all().order_by('-id')[:30]
            return render(request, "invernadero/historico.html", {
                "datos": lecturas, "fecha": util.get_date()
            })
        except:
            return render(request, "invernadero/error.html", {
                "mensaje": "Algo salio mal :("
            })


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("invernadero:index"))
        else:
            return render(request, "login.html", {
                "message": "Credenciales no válidas"
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html", {
        "message": "Sesión cerrada."
    })
