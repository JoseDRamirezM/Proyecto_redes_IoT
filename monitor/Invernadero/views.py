from django.shortcuts import render
from .models import Lectura
from . import util
from serial.serialutil import SerialException

from .models import Lectura

# Create your views here.
def index(request):
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
    try:
        lecturas = Lectura.objects.all().order_by('-id')[:10]
        return render(request, "invernadero/historico.html", {
            "datos": lecturas, "fecha": util.get_date()
        })
    except:
        return render(request, "invernadero/error.html", {
            "mensaje": "Algo salio mal :("
        })