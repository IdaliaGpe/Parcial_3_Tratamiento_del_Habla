from threading import Thread
import tkinter as tk
import sounddevice
import numpy as np

class StreamThread(Thread):
    def __init__(self):
        super().__init__()
        self.dispositivo_input = 1
        self.dispositivo_output = 3
        self.tamaño_bloque = 5500
        self.canales = 1
        self.tipo_dato = np.int16
        self.latencia = "high"

#Heredamos de Tk para hacer una ventana
class App(tk.Tk):

    def __init__(self):

        super().__init__()
        #Titulo de la ventana
        self.title("Aplicacion de audio")
        #Establecer Tamaño
        self.geometry("400x300")

        #Crear Boton
        boton_iniciar = tk.Button(self, width = 20, text = "Iniciar Grabación")
        #Mostrar Boton
        boton_iniciar.grid(column = 0, row = 0)

        boton_detener  = tk.Button(self, width = 20, text = "Detener Grabación")
        boton_detener.grid(column = 1, row = 0)

        etiqueta_estado = tk.Label(text = "Estado: ")
        etiqueta_estado.grid(column = 0, row = 1)

        etiqueta_valor_estado = tk.Label(text = " - ")
        etiqueta_valor_estado.grid(column = 1, row = 1)

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()