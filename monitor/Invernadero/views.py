from django.shortcuts import render
from .models import Lectura
from . import util
from serial.serialutil import SerialException

# Create your views here.
def index(request):
    try:
        return render(request, "invernadero/index.html", {
            "datos": util.leer_datos()
        })
    except SerialException:
        return render(request, "invernadero/error.html", {
            "mensaje": "Asegurese de que el dispositivo este conectado"
        })
    except:
        return render(request, "invernadero/error.html", {
            "mensaje": "Algo salio mal :("
        })