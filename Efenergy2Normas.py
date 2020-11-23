﻿#!/usr/bin/env python3
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

        rutaPdf = values['-seleccionPDF-']
        webbrowser.open_new(rutaPdf)

# ************************************************************************************************************************

def definirTituloNorma(tipoProceso, columna1, columna4, labelTituloNorma):

    columna1.Update(visible=False)
    columna4.Update(visible=True)

    if tipoProceso == idVoltaje:

        txtTituloNorma = 'VOLTAJE'

    elif tipoProceso == idPotencia:

        txtTituloNorma = 'POTENCIA'

    elif tipoProceso == idArmonicos:

        txtTituloNorma = 'ARMÓNICOS'

    labelTituloNorma.update(txtTituloNorma)
    #window['-labelTituloNorma-'].update(txtTituloNorma)

# ************************************************************************************************************************

def sustituirNorma(tipoProceso, botonActualizarNorma, botonDescartarGestion, botonVerSeleccionado, window, values):

    try:

        archivoSeleccionado = values['-seleccionPDF-']

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

        botonActualizarNorma.update(disabled=True)
        botonDescartarGestion.update(disabled=True)
        botonVerSeleccionado.update(disabled=True)
        window['-seleccionPDF-'].update('')

    except:

        sg.Popup('ERROR', 
                    'Ocurrió un problema al intentar actualizar el archivo PDF de la norma. Revise que el archivo actual no esté abierto para visualización y que sean diferentes. Ciérrelo e intente de nuevo.',
                    text_color=eColor1, 
                    background_color=eColor6,
                    button_color=eColores1,
                    keep_on_top=True,
                    no_titlebar=False)

# ************************************************************************************************************************

def botonesGestionarNorma(estado, botonActualizarNorma, botonDescartarGestion, botonVerSeleccionado):

    botonActualizarNorma.update(disabled=estado)
    botonDescartarGestion.update(disabled=estado)
    botonVerSeleccionado.update(disabled=estado)

# ************************************************************************************************************************
