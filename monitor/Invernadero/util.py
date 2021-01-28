import serial
import time


def leer_datos():
    s = serial.Serial()
    s.port = 'COM3'
    s.baudrate = 9600
    s.setDTR(False)
    s.open()

    # s.dtr = 0
    # s.dtr = 1
    #time.sleep(1)
    #s.reset_input_buffer()

    data_str = s.readline().decode()

    data_str = data_str.replace(' ','')
    data_str = data_str.replace('\r','')
    data_str = data_str.replace('\n','')

    data_list = data_str.split(",")
    
    return data_list