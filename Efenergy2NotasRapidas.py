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

def grabarNota(tipoProceso, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, rutaInformacion, txtVisorEditor):

    global informacionVoltaje
    global informacionPotencia
    global informacionArmonicos

    #listOfGlobals = globals()

    botonEditarNota.update(disabled=False)
    botonGrabarNota.update(disabled=True)
    botonDescartarGrabacion.update(disabled=True)
    visorEditor.update(disabled=True)
    visorEditor.update(background_color=eColor2)

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

# ************************************************************************************************************************

def editarNota(botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor):

    botonEditarNota.update(disabled=True)
    botonGrabarNota.update(disabled=False)
    botonDescartarGrabacion.update(disabled=False)
    visorEditor.update(disabled=False)
    visorEditor.update(background_color=eColor3)

# ************************************************************************************************************************

def gestionarNota(tipoProceso, window, columna1, columna3, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacion):

    definirTituloNota(tipoProceso, window)
    columna1.Update(visible=False)
    columna3.Update(visible=True)
    botonEditarNota.update(disabled=False)
    botonGrabarNota.update(disabled=True)
    botonDescartarGrabacion.update(disabled=True)
    visorEditor.update(disabled=True)
    visorEditor.update(background_color=eColor2)
    visorEditor.update(informacion)
    
# ************************************************************************************************************************

def descartarGrabacion(botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacion):

    botonEditarNota.update(disabled=False)
    botonGrabarNota.update(disabled=True)
    botonDescartarGrabacion.update(disabled=True)
    visorEditor.update(disabled=True)
    visorEditor.update(background_color=eColor2)
    visorEditor.update(informacion)

# ************************************************************************************************************************
