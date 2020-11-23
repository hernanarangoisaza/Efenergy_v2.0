﻿#!/usr/bin/python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import pandas
import threading

from Efenergy2Globales import *
import Efenergy2UI

# ************************************************************************************************************************

def cargarPlantilla(window, rutaPlantilla, tipoProceso):

    global datosPreliminares

    if (tipoProceso == idGeneral):

        datosPreliminares = pandas.ExcelFile(rutaPlantilla)

    window.write_event_value('-ThreadDone-','')

# ************************************************************************************************************************

def indicadorCarga(window):

    limite = 100
    i = 0
    window['-progressBar-'].update_bar(0,0)

    while (t1.is_alive()):

        window['-progressBar-'].update_bar(i,limite)
        i = i + 1
        if (i==(limite-1)):
            i = 0
            window['-progressBar-'].update_bar(0,0)

    window['-progressBar-'].update_bar(limite,limite)

# ************************************************************************************************************************

def hiloCargarPlantilla(rutaPlantilla, tipoProceso, window):

    global t1

    t1 = threading.Thread(target=cargarPlantilla, args=(window,rutaPlantilla,tipoProceso), daemon=True)
    t1.name = 't1'
    t1.start()

# ************************************************************************************************************************

def hiloIndicadorCarga(window):

    global t2 

    t2 = threading.Thread(target=indicadorCarga, args=(window,), daemon=True)
    t2.name = 't2'
    t2.start()

# ************************************************************************************************************************

def calcularRangoVariacion(window, values, inputVariacion):

    try:

        intVariacion = float(values['-inputVariacion-'])
        voltajeLimiteInferior = intVariacion * (1 - porcentajeLimiteInferior)
        voltajeLimiteSuperior = intVariacion * (1 + porcentajeLimiteSuperior)
        nuevoTooltip = '  El rango establecido para análisis es [ {0:.2f} - {1:.2f} ]  '.format(voltajeLimiteInferior,voltajeLimiteSuperior)
        inputVariacion.set_tooltip(nuevoTooltip)

        return voltajeLimiteInferior, voltajeLimiteSuperior

    except ValueError:

        # Validar que la representación del string corresponde a un número
        
        inputVariacion.update(''.join([i for i in values['-inputVariacion-'] if i.isdigit()])) 
        
# ************************************************************************************************************************

def actualizarFiltrosPlantilla(comboDias, comboFases, comboVoltaje):

    comboDias.Update(values=datosPreliminares.sheet_names)
    comboDias.Update(disabled=False)
    comboDias.Update(readonly=True)
    comboDias.Update(set_to_index=0)

    comboFases.Update(disabled=False)
    comboFases.Update(readonly=True)
    comboFases.Update(set_to_index=0)

    comboVoltaje.Update(disabled=False)
    comboVoltaje.Update(readonly=True)
    comboVoltaje.Update(set_to_index=1)

# ************************************************************************************************************************

def seleccionarPlantilla(values, window, barraMenuPrincipal):

    rutaPlantilla = values['-inputSeleccionPlantilla-']
    archivoPlantilla = rutaPlantilla.split('/')[-1]
    window['-valorRutaPlantilla-'].Update(rutaPlantilla.rpartition('/')[0])
    window['-valorArchivoPlantilla-'].Update(archivoPlantilla)
    barraMenuPrincipal.Update(menuPrincipal1)

# ************************************************************************************************************************

def cargarDatosPreliminares(tipoProceso, values, window):

    if (tipoProceso == idGeneral):

        rutaPlantillaPreliminar = values['-inputSeleccionPlantilla-']
        hiloCargarPlantilla(rutaPlantillaPreliminar, tipoProceso, window)

    hiloIndicadorCarga(window)

# ************************************************************************************************************************

def asignarDatosPreliminares():

    return datosPreliminares

# ************************************************************************************************************************

def leerArchivo(file, errorPersonalizado):

    try:

        archivo = open(file, "r", encoding="utf8", errors='ignore')
        contenido = archivo.read()

        return contenido

    except:

        sg.Popup('ERROR', 
                  errorPersonalizado,
                  text_color=eColor1, 
                  background_color=eColor6,
                  button_color=eColores1,
                  keep_on_top=True,
                  no_titlebar=False)
    
    finally:
    
        archivo.close()

# ************************************************************************************************************************

def escribirArchivo(file, contenido, errorPersonalizado):

    try:

        archivo = open(file, "w", encoding="utf8", errors='ignore')
        archivo.write(contenido)

    except:

        sg.Popup('ERROR', 
                 errorPersonalizado,   
                 text_color=eColor1, 
                 background_color=eColor6,
                 button_color=eColores1,
                 keep_on_top=True,
                 no_titlebar=False)

    finally:
        
        archivo.close()

# ************************************************************************************************************************