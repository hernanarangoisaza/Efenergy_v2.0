# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import webbrowser
import shutil

from Efenergy2Globales import *
import Efenergy2UI

# ************************************************************************************************************************

def visualizarNorma(tipoProceso, values):

    if tipoProceso == idVoltaje:

        webbrowser.open_new(rutaPdfVoltaje)

    elif tipoProceso == idPotencia:

        webbrowser.open_new(rutaPdfPotencia)

    elif tipoProceso == idArmonicos:

        webbrowser.open_new(rutaPdfArmonicos)

    elif tipoProceso == idOtroPDF:

        rutaPdf = values['-inputSeleccionPDF-']
        webbrowser.open_new(rutaPdf)

# ************************************************************************************************************************

def definirTituloNorma(tipoProceso, window):

    window['-columna1-'].update(visible=False)
    window['-columna4-'].update(visible=True)

    if tipoProceso == idVoltaje:

        txtTituloNorma = 'VOLTAJE'

    elif tipoProceso == idPotencia:

        txtTituloNorma = 'POTENCIA'

    elif tipoProceso == idArmonicos:

        txtTituloNorma = 'ARMÓNICOS'

    window['-labelTituloNorma-'].update(txtTituloNorma)

# ************************************************************************************************************************

def sustituirNorma(tipoProceso, window, values):

    try:

        archivoSeleccionado = values['-inputSeleccionPDF-']

        if tipoProceso == idVoltaje:

            shutil.copy(archivoSeleccionado, rutaPdfVoltaje)

        elif tipoProceso == idPotencia:

            shutil.copy(archivoSeleccionado, rutaPdfPotencia)

        elif tipoProceso == idArmonicos:

            shutil.copy(archivoSeleccionado, rutaPdfArmonicos)

        sg.Popup('NOTIFICACIÓN', 
                    'El archivo PDF de la norma ha sido actualizado correctamente.',
                    text_color=eColor1, 
                    background_color=eColor6,
                    button_color=eColores1,
                    keep_on_top=True,
                    no_titlebar=False)

        window['-botonActualizarNorma-'].update(disabled=True)
        window['-botonDescartarGestion-'].update(disabled=True)
        window['-botonVerSeleccionado-'].update(disabled=True)
        window['-inputSeleccionPDF-'].update('')

    except:

        sg.Popup('ERROR', 
                    'Ocurrió un problema al intentar actualizar el archivo PDF de la norma. Revise que el archivo actual no esté abierto para visualización y que sean diferentes. Ciérrelo e intente de nuevo.',
                    text_color=eColor1, 
                    background_color=eColor6,
                    button_color=eColores1,
                    keep_on_top=True,
                    no_titlebar=False)

# ************************************************************************************************************************

def botonesGestionarNorma(estado, window):

    window['-botonActualizarNorma-'].update(disabled=estado)
    window['-botonDescartarGestion-'].update(disabled=estado)
    window['-botonVerSeleccionado-'].update(disabled=estado)

# ************************************************************************************************************************
