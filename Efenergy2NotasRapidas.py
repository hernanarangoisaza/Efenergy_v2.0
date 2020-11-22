#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from Efenergy2Globales import *

# ************************************************************************************************************************

def leerArchivo(file):

    try:

        archivo = open(file, "r", encoding="utf8", errors='ignore')
        contenido = archivo.read()

        return contenido

    except:

        sg.Popup('ERROR', 
                    'Ocurrió un problema al leer el archivo de texto de Notas Rápidas.',
                    text_color=eColor1, 
                    background_color=eColor6,
                    button_color=eColores1,
                    keep_on_top=True,
                    no_titlebar=False)
    
    finally:
    
        archivo.close()

# ************************************************************************************************************************

def escribirArchivo(file, contenido):

    try:

        archivo = open(file, "w", encoding="utf8")
        archivo.write(contenido)

    except:

        sg.Popup('ERROR', 
                    'Ocurrió un problema al escribir el archivo de texto de Notas Rápidas.',
                    text_color=eColor1, 
                    background_color=eColor6,
                    button_color=eColores1,
                    keep_on_top=True,
                    no_titlebar=False)

    finally:
        
        archivo.close()

# ************************************************************************************************************************

def definirTituloNota(tipoProceso):

    if tipoProceso == idVoltaje:

        txtTituloNota = 'VOLTAJE'

    elif tipoProceso == idPotencia:

        txtTituloNota = 'POTENCIA'

    elif tipoProceso == idArmonicos:

        txtTituloNota = 'ARMÓNICOS'

    window['-labelTituloNota-'].update(txtTituloNota)

# ************************************************************************************************************************

class Efenergy2NotasRapidas():

    def __init__(self):

        #self.datosVoltaje = datosVoltaje
        print()

    # ************************************************************************************************************************

    def grabarNota(tipoProceso):

        global informacionVoltaje
        global informacionPotencia
        global informacionArmonicos

        botonEditarNota.update(disabled=False)
        botonGrabarNota.update(disabled=True)
        botonDescartarGrabacion.update(disabled=True)
        visorEditor.update(disabled=True)
        visorEditor.update(background_color=eColor2)

        if (tipoProceso == idVoltaje):

            informacionVoltaje = values['-visorEditorNotas-']
            escribirArchivo(rutaInformacionVoltaje, informacionVoltaje)

        elif (tipoProceso == idPotencia):

            informacionPotencia = values['-visorEditorNotas-']
            escribirArchivo(rutaInformacionPotencia, informacionPotencia)

        elif (tipoProceso == idArmonicos):

            informacionArmonicos = values['-visorEditorNotas-']
            escribirArchivo(rutaInformacionArmonicos, informacionArmonicos)

    # ************************************************************************************************************************

    def editarNota():

        botonEditarNota.update(disabled=True)
        botonGrabarNota.update(disabled=False)
        botonDescartarGrabacion.update(disabled=False)
        visorEditor.update(disabled=False)
        visorEditor.update(background_color=eColor3)

    # ************************************************************************************************************************

    def gestionarNota(tipoProceso):

        definirTituloNota(tipoProceso)
        
        columna1.Update(visible=False)
        columna3.Update(visible=True)
        botonEditarNota.update(disabled=False)
        botonGrabarNota.update(disabled=True)
        botonDescartarGrabacion.update(disabled=True)
        visorEditor.update(disabled=True)
        visorEditor.update(background_color=eColor2)

        if (tipoProceso == idVoltaje):

            window['-visorEditorNotas-'].update(informacionVoltaje)

        elif (tipoProceso == idPotencia):

            window['-visorEditorNotas-'].update(informacionPotencia)

        elif (tipoProceso == idArmonicos):

            window['-visorEditorNotas-'].update(informacionArmonicos)

    # ************************************************************************************************************************

    def descartarGrabacion(tipoProceso):

        botonEditarNota.update(disabled=False)
        botonGrabarNota.update(disabled=True)
        botonDescartarGrabacion.update(disabled=True)
        visorEditor.update(disabled=True)
        visorEditor.update(background_color=eColor2)
 
        if (tipoProceso == idVoltaje):

            window['-visorEditorNotas-'].update(informacionVoltaje)

        elif (tipoProceso == idPotencia):

            window['-visorEditorNotas-'].update(informacionPotencia)

        elif (tipoProceso == idArmonicos):

            window['-visorEditorNotas-'].update(informacionArmonicos)

    # ************************************************************************************************************************
