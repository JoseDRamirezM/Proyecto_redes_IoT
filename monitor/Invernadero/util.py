import serial
import time
from datetime import date, datetime

def leer_datos():
    s = serial.Serial()
    s.port = 'COM3'
    s.baudrate = 9600
    s.setDTR(False)
    s.open()

    data_str = s.readline().decode()
    data_str = data_str.replace(' ','')
    data_str = data_str.replace('\r','')
    data_str = data_str.replace('\n','')

    data_list = data_str.split(",")
    
    return data_list

def get_date():
    # datetime object containing current date and time
    hoy = date.today()
    # dd/mm/YY H:M:S
    fecha = hoy.strftime("%B %d, %Y")
    return fecha

def get_datetime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    return now