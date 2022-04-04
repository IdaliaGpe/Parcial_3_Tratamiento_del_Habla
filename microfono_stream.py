import sounddevice as sd
import numpy as np

print(sd.query_devices())
#1 entrada
#3 salida

try: #Intenta hacer esto
    with sd.Stream():
        print('Presiona tecla Enter para salir')
        input()
except Exception as e: #Si fallas has esto
    print(str(e))