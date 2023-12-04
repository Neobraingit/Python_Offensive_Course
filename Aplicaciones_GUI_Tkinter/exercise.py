#!/usr/bin/env python3

import tkinter as tk

# Creamos nuestra primera ventana y mostramos un texto
def accion_de_boton():
    print ('Se ha presionado el botón')
root = tk.Tk()
label = tk.Label(root, text='Hola mundo')
button = tk.Button(root, text='Presióname', command=accion_de_boton)
label.pack()
root.mainloop()



