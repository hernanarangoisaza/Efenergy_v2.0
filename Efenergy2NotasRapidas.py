# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Efenergy2Globales import *
import Efenergy2UI
import Efenergy2Funciones

# ************************************************************************************************************************

def definirTituloNota(tipoProceso, window):

    if tipoProceso == idVoltaje:

        txtTituloNota = 'VOLTAJE'

    elif tipoProceso == idPotencia:

        txtTituloNota = 'POTENCIA'

    elif tipoProceso == idArmonicos:

        txtTituloNota = 'ARMÓNICOS'

    window['-labelTituloNota-'].update(txtTituloNota)

# ************************************************************************************************************************

def grabarNota(tipoProceso, rutaInformacion, txtVisorEditor, window):

    global informacionVoltaje
    global informacionPotencia
    global informacionArmonicos

    #listOfGlobals = globals()

    window['-botonEditarNota-'].update(disabled=False)
    window['-botonGrabarNota-'].update(disabled=True)
    window['-botonDescartarGrabacion-'].update(disabled=True)
    window['-visorEditorNotas-'].update(disabled=True)
    window['-visorEditorNotas-'].update(background_color=eColor2)

    errorPersonalizadoNotasEscribir = 'Ocurrió un problema al escribir el archivo de texto de Notas Rápidas.'

    if (tipoProceso == idVoltaje):

        #listOfGlobals['informacionVoltaje'] = txtVisorEditor
        informacionVoltaje = txtVisorEditor
        rutaInformacionVoltaje = rutaInformacion
        Efenergy2Funciones.escribirArchivo(rutaInformacionVoltaje, informacionVoltaje, errorPersonalizadoNotasEscribir)

    elif (tipoProceso == idPotencia):

        informacionPotencia = txtVisorEditor
        rutaInformacionPotencia = rutaInformacion
        Efenergy2Funciones.escribirArchivo(rutaInformacionPotencia, informacionPotencia, errorPersonalizadoNotasEscribir)

    elif (tipoProceso == idArmonicos):

        informacionArmonicos = txtVisorEditor
        rutaInformacionArmonicos = rutaInformacion
        Efenergy2Funciones.escribirArchivo(rutaInformacionArmonicos, informacionArmonicos, errorPersonalizadoNotasEscribir)

    return txtVisorEditor

# ************************************************************************************************************************

def editarNota(window):

    window['-botonEditarNota-'].update(disabled=True)
    window['-botonGrabarNota-'].update(disabled=False)
    window['-botonDescartarGrabacion-'].update(disabled=False)
    window['-visorEditorNotas-'].update(disabled=False)
    window['-visorEditorNotas-'].update(background_color=eColor3)

# ************************************************************************************************************************

def gestionarNota(tipoProceso, window, informacion):

    definirTituloNota(tipoProceso, window)
    window['-columna1-'].update(visible=False)
    window['-columna3-'].update(visible=True)
    window['-botonEditarNota-'].update(disabled=False)
    window['-botonGrabarNota-'].update(disabled=True)
    window['-botonDescartarGrabacion-'].update(disabled=True)
    window['-visorEditorNotas-'].update(disabled=True)
    window['-visorEditorNotas-'].update(background_color=eColor2)
    window['-visorEditorNotas-'].update(informacion)
    
# ************************************************************************************************************************

def descartarGrabacion(informacion, window):

    window['-botonEditarNota-'].update(disabled=False)
    window['-botonGrabarNota-'].update(disabled=True)
    window['-botonDescartarGrabacion-'].update(disabled=True)
    window['-visorEditorNotas-'].update(disabled=True)
    window['-visorEditorNotas-'].update(background_color=eColor2)
    window['-visorEditorNotas-'].update(informacion)

# ************************************************************************************************************************
