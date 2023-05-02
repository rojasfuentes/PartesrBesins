import PySimpleGUI as sg
import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Define la ventana emergente
layout = [[sg.Text('Ingresa la nota:'), sg.InputText()], [sg.Button('Ok')]]
window = sg.Window('Ingresar nota', layout)

while True:
    event, values = window.read()
    if event == 'Ok':
        nota = values[0]
        break

window.close()

print("Ultima nota:", nota)

orden_path = filedialog.askopenfilename(
    title="Orden Cliente", filetypes=(("Archivo de Excel", "*.xlsx"),))

inventario_path = filedialog.askopenfilename(
    title="Consulta de Inventarios", filetypes=(("Archivo de Excel", "*.xlsx"),))
