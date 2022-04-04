from gc import callbacks
from unittest.util import _count_diff_hashable
import sounddevice as sd
import numpy as np

#print(sd.query_devices())
#1 entrada
#3 salida

#indata: Arreglo de numpy con la info recopilada por la tarjeta de sonido
#             a traves del dispositivo de entrada
#outdata: Arreglo de numpy que se le enviará al dispositivo de salida
#             por default es un silencio (puro 0's)
#frames: El numero de muestras que tiene indata
#time:   El tiempo que se lleva haciendo el Stream
#status: Si ha habido algun error
def callback_stream(indata, outdata, frames, time, status):
    #outdata[:] = indata
    return

try: #Intenta hacer esto

    with sd.Stream(
        device = (1, 3), #Se eligen dispositivos (Entrada, Salida)
        blocksize = 0, #0 es que la tarjeta de sonido decide el mejor tamaño
        samplerate = 44100, #Frecuencia de Muestreo
        channels = 1, #Canales
        dtype = np.int16, #Tipo de dato (Profundidad de bits)
        latency = 'high', #Latencia, que tanto tiempo pasa desde entrada hasta salida
        callback = callback_stream
    ):

        print('Presiona tecla Enter para salir')
        input()

except Exception as e: #Si fallas has esto
    print(str(e))