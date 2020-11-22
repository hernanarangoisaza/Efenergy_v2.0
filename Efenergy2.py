# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

from Efenergy2UI import *
from Efenergy2Globales import *
from Efenergy2NotasRapidas import *

import os.path
import ctypes
from pathlib import Path
import webbrowser
import shutil

#import wx
import wx.grid

from AnalisisDatosVoltaje import AnalisisDatosVoltaje

#from AnalisisDatosPotencia import AnalisisDatosPotencia
#from AnalisisDatosPotenciaReactiva import AnalisisDatosPotenciaReactiva
#from AnalisisDatosArmonicos import AnalisisDatosArmonicos
#from AnalisisDatosArmonicosCorriente import AnalisisDatosArmonicosCorriente
#from EditarInformacion import EditarInformacion

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

def hiloCargarPlantilla(rutaPlantilla, tipoProceso):

    global t1

    t1 = threading.Thread(target=cargarPlantilla, args=(window,rutaPlantilla,tipoProceso), daemon=True)
    t1.name = 't1'
    t1.start()

# ************************************************************************************************************************

def hiloIndicadorCarga():

    global t2 

    t2 = threading.Thread(target=indicadorCarga, args=(window,), daemon=True)
    t2.name = 't2'
    t2.start()

# ************************************************************************************************************************

def visualizarNorma(tipoProceso):

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

def definirTituloNorma(tipoProceso):

    columna1.Update(visible=False)
    columna4.Update(visible=True)

    if tipoProceso == idVoltaje:

        tituloNorma = 'VOLTAJE'

    elif tipoProceso == idPotencia:

        tituloNorma = 'POTENCIA'

    elif tipoProceso == idArmonicos:

        tituloNorma = 'ARMÓNICOS'

    window['-labelTituloNorma-'].update(tituloNorma)

# ************************************************************************************************************************

def sustituirNorma(tipoProceso):

    try:

        if tipoProceso == idVoltaje:

            shutil.copy(values['-seleccionPDF-'], rutaPdfVoltaje)

        elif tipoProceso == idPotencia:

            shutil.copy(values['-seleccionPDF-'], rutaPdfPotencia)

        elif tipoProceso == idArmonicos:

            shutil.copy(values['-seleccionPDF-'], rutaPdfArmonicos)

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

def botonesGestionarNorma(estado):

    botonActualizarNorma.update(disabled=estado)
    botonDescartarGestion.update(disabled=estado)
    botonVerSeleccionado.update(disabled=estado)

# ************************************************************************************************************************

def calcularRangoVariacion():

    global voltajeLimiteInferior
    global voltajeLimiteSuperior

    try:

        intVariacion = float(window['-inputVariacion-'].get())
        voltajeLimiteInferior = intVariacion * (1 - porcentajeLimiteInferior)
        voltajeLimiteSuperior = intVariacion * (1 + porcentajeLimiteSuperior)
        nuevoTooltip = '  El rango establecido para análisis es [ {0:.2f} - {1:.2f} ]  '.format(voltajeLimiteInferior,voltajeLimiteSuperior)
        inputVariacion.set_tooltip(nuevoTooltip)

    except ValueError:

        # Validar que la representación del string corresponde a un número
        
        window['-inputVariacion-'].update(''.join([i for i in window['-inputVariacion-'].get() if i.isdigit()])) 
        
# ************************************************************************************************************************

def actualizarFiltrosPlantilla():

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

def seleccionarPlantilla():

    rutaPlantilla = values['-inputSeleccionPlantilla-']
    archivoPlantilla = rutaPlantilla.split('/')[-1]
    window['-valorRutaPlantilla-'].Update(rutaPlantilla.rpartition('/')[0])
    window['-valorArchivoPlantilla-'].Update(archivoPlantilla)
    barraMenuPrincipal.Update(menuPrincipal1)

# ************************************************************************************************************************

def cargarDatosPreliminares(tipoProceso):

    if (tipoProceso == idGeneral):

        rutaPlantillaPreliminar = values['-inputSeleccionPlantilla-']
        hiloCargarPlantilla(rutaPlantillaPreliminar, tipoProceso)

    hiloIndicadorCarga()

# ************************************************************************************************************************

def asignarDatosPreliminares(tipoProceso):

    global datosVoltaje
    global datosPotencia
    global datosArmonicos

    if (tipoProceso == idVoltaje):

        datosVoltaje = datosPreliminares

    elif (tipoProceso == idPotencia):

        datosPotencia = datosPreliminares

    elif (tipoProceso == idArmonicos):

        datosArmonicos = datosPreliminares

# ************************************************************************************************************************

# GENERACIÓN DINÁMICA DE FRAMES PARA EL LOGO. DEBE CREARSE UNA POR CADA SIMULACIÓN DE PANTALLA MEDIANTE COLUMNAS.

frameLogoV1, logoPrincipalV1, statusBarPrincipalV1 = Efenergy2UI.generarLogo(1)
frameLogoV2, logoPrincipalV2, statusBarPrincipalV2 = Efenergy2UI.generarLogo(2)
frameLogoV3, logoPrincipalV3, statusBarPrincipalV3 = Efenergy2UI.generarLogo(3)
frameLogoV4, logoPrincipalV4, statusBarPrincipalV4 = Efenergy2UI.generarLogo(4)
frameLogoV5, logoPrincipalV5, statusBarPrincipalV5 = Efenergy2UI.generarLogo(5)

# GENERACIÓN DINÁMICA DE FRAMES PARA NAVEGACIÓN. DEBE CREARSE UNA POR CADA SIMULACIÓN DE PANTALLA MEDIANTE COLUMNAS.

frameNavegacionV1, botonInicioV1 = Efenergy2UI.generarNavegacion(1) # Ventana Acerca de
frameNavegacionV2, botonInicioV2 = Efenergy2UI.generarNavegacion(2) # Ventana Notas Rápidas
frameNavegacionV3, botonInicioV3 = Efenergy2UI.generarNavegacion(3) # Ventana Notas Rápidas
frameNavegacionV4, botonInicioV4 = Efenergy2UI.generarNavegacion(4) # Ventana Análisis de Voltaje

# GENERACIÓN DINÁMICA DEL FRAME PARA NOTAS RÁPIDAS.

columna3, visorEditor, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, frameNota, frameTituloNota, labelTituloNota = Efenergy2UI.generarNotasRapidas(frameLogoV3, frameNavegacionV2)

# GENERACIÓN DINÁMICA DEL FRAME PARA GESTIÓN DE NORMAS.

columna4, botonVerNorma, botonVerSeleccionado, botonActualizarNorma, botonDescartarGestion, frameNorma, frameTituloNorma, labelTituloNorma = Efenergy2UI.generarGestionNormas(frameLogoV4, frameNavegacionV3)

# GENERACIÓN DINÁMICA DEL FRAME PARA ANÁLISIS DE VOLTAJE.

columna5, frameSeccionVoltaje, layoutTabTablaContenido, frameTituloSeccionVoltaje = Efenergy2UI.generarAnalisisVoltaje(frameNavegacionV4)

# ************************************************************************************************************************

# GENERACIÓN DE LA INTERFAZ DE USUARIO PRINCIPAL

frameFiltrosVoltaje, comboDias, comboVoltaje, comboFases, inputVariacion = Efenergy2UI.generarFiltrosVoltaje()
columna1, barraMenuPrincipal, frameSelectorPlantilla, inputSeleccionPlantilla, botonPlantilla, botonCargarPlantilla = Efenergy2UI.generarUIPrincipal(frameLogoV1, frameFiltrosVoltaje)
columna2, frameAcercaDe = Efenergy2UI.generarAcercaDe(frameLogoV2, frameNavegacionV1)

# ************************************************************************************************************************

# FULL LAYOUT

layoutPrincipal =   [
                        #### Barra de Menú superior principal
                        [
                            barraMenuPrincipal,
                        ],
                        #### Columnas ocultables para simular pantallas
                        [
                            columna1, # Inicio
                            columna2, # Acerca de
                            columna3, # Gestionar Notas Rápidas
                            columna4, # Gestionar Normas PDF
                            columna5, # Análisis de Voltaje
                        ],
                    ]

# ************************************************************************************************************************

# Ventana principal y ajustes personalizados

sg.theme('Default1')
sg.ChangeLookAndFeel('SystemDefault')

window = sg.Window('Efenergy v2.0',
                   layout=layoutPrincipal,
                   use_default_focus=True,
                   size=sizeFrmPrincipal,
                   debugger_enabled=False,
                   finalize=True,
                   font=('Helvetica',11),
                   icon=rutaIconoPrincipal)

# Establecer en la ventana de filtros el valor base para la Variación.

inputVariacion.Update = valorVariacion

# Habilitar barra de menú con opciones deshabilitadas.

barraMenuPrincipal.Update(menuPrincipal2)

# Carga los textos descriptivos para las normas

informacionVoltaje = leerArchivo(rutaInformacionVoltaje)
informacionPotencia = leerArchivo(rutaInformacionPotencia)
informacionArmonicos = leerArchivo(rutaInformacionArmonicos)

# Extender tamaño de algunos Frames para que ocupen el ancho del diseño.

frameFiltrosVoltaje.expand(expand_x=True)
frameAcercaDe.expand(expand_x=True)
frameNota.expand(expand_x=True)
frameNorma.expand(expand_x=True)
visorEditor.expand(expand_x=True)
frameSeccionVoltaje.expand(expand_x=True)

frameTituloNota.expand(expand_x=True)
frameTituloNorma.expand(expand_x=True)
frameTituloSeccionVoltaje.expand(expand_x=True)

frameNavegacionV1.expand(expand_x=True)
frameNavegacionV2.expand(expand_x=True)
frameNavegacionV3.expand(expand_x=True)
frameNavegacionV4.expand(expand_x=True)

window.refresh()

# Mejorar la nitidez y resolución de la aplicación. Se ve pequeño en monitores de alta resolución como 4K.

# ctypes.windll.shcore.SetProcessDpiAwareness(2)

# ************************************************************************************************************************

# Run the Event Loop.

while True:

    event, values = window.read()

    print(event)

    if event == sg.WIN_CLOSED or event == 'Salir': # Salir de la aplicación

        break
    
    elif event == '-inputSeleccionPlantilla-': # Seleccionar plantilla de origen de datos

        seleccionarPlantilla()
        botonCargarPlantilla.update(disabled=False)

    elif event == '-botonCargarPlantilla-': # Cargar plantilla de origen de datos

        cargarDatosPreliminares(idGeneral)

    elif event.endswith('-opcV1-'): # Analizar Voltaje

        idProcesoActual = idVoltaje
        columna1.Update(visible=False)
        columna5.Update(visible=True)

        asignarDatosPreliminares(idVoltaje)

        calcularRangoVariacion()

        AnalisisDatosVoltaje(datosVoltaje, 
                             float(voltajeLimiteInferior), 
                             float(voltajeLimiteSuperior), 
                             values['-comboDias-'], 
                             values['-comboFases-'],
                             values['-comboVoltaje-'])

		# 'límites de variaciones de\nredes eléctricas\n\nEn el rango de 127-10% - 127+10% \nMayor a 127+10% \nMenor a 127-10%'



    elif event == '-ThreadDone-': # Mensaje recibido desde los hilos al momento de haber finalizado las acciones que toman más tiempo

        actualizarFiltrosPlantilla()

    elif event == '-inputVariacion-': # Rango de variación
    
        calcularRangoVariacion()

    elif event.endswith('-opcAcercaDe-'): # Ventana Acerca de

        columna1.Update(visible=False)
        columna2.Update(visible=True)

    elif event == '-botonInicioV1-': # Boton INICIO desde la ventana Acerca de

        columna1.Update(visible=True)
        columna2.Update(visible=False)

    elif event == '-botonInicioV2-': # Boton INICIO desde la ventana Notas Rápidas

        columna1.Update(visible=True)
        columna3.Update(visible=False)

    elif event == '-botonInicioV3-': # Boton INICIO desde la ventana Notas Rápidas

        columna1.Update(visible=True)
        columna4.Update(visible=False)

    elif event == '-botonInicioV4-': # Boton INICIO desde la ventana Análisis de Voltaje

        columna1.Update(visible=True)
        columna5.Update(visible=False)

    elif event.endswith('-opcN7-'): # Gestionar nota rápida para Voltaje

        idProcesoActual = idVoltaje
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual)

    elif event.endswith('-opcN8-'): # Gestionar nota rápida para Potencia

        idProcesoActual = idPotencia
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual)

    elif event.endswith('-opcN9-'): # Gestionar nota rápida para Armónicos

        idProcesoActual = idArmonicos
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual)

    elif event == '-botonEditarNota-': # Habilitar la zona de edición de texto de las Notas Rápidas

        Efenergy2NotasRapidas.editarNota()

    elif event == '-botonGrabarNota-': # Actualizar los archivos en disco con el contenido de la zona de edición de las Notas Rápidas

        Efenergy2NotasRapidas.grabarNota(idProcesoActual)

    elif event == '-botonDescartarGrabacion-': # Descartar el contenido de la zona de edición de las Notas Rápidas y no grabarlo

        Efenergy2NotasRapidas.descartarGrabacion(idProcesoActual)

    elif event.endswith('-opcN1-'): # Ver norma Pdf para Voltaje

        idProcesoActual = idVoltaje
        visualizarNorma(idProcesoActual)

    elif event.endswith('-opcN2-'): # Ver norma Pdf para Potencia

        idProcesoActual = idPotencia
        visualizarNorma(idProcesoActual)

    elif event.endswith('-opcN3-'): # Ver norma Pdf para Armónicos

        idProcesoActual = idArmonicos
        visualizarNorma(idProcesoActual)

    elif event.endswith('-opcN4-'): # Gestionar norma Pdf para Voltaje

        idProcesoActual = idVoltaje
        definirTituloNorma(idProcesoActual)

    elif event.endswith('-opcN5-'): # Gestionar norma Pdf para Potencia

        idProcesoActual = idPotencia
        definirTituloNorma(idProcesoActual)

    elif event.endswith('-opcN6-'): # Gestionar norma Pdf para Armónicos

        idProcesoActual = idArmonicos
        definirTituloNorma(idProcesoActual)

    elif event == ('-seleccionPDF-'): # Control de la barra de botones para la gestión de normas

        botonesGestionarNorma(False)

    elif event == ('-botonVerNorma-'): # Ver archivo PDF para el contenido de la norma actual

        visualizarNorma(idProcesoActual)
 
    elif event == ('-botonVerSeleccionado-'): # Ver archivo PDF para el contenido de la nueva norma seleccionada

        visualizarNorma(idOtroPDF)

    elif event == ('-botonDescartarGestion-'): # Control de la barra de botones para la gestión de normas

        botonesGestionarNorma(True)
        window['-seleccionPDF-'].update('')

    elif event == ('-botonActualizarNorma-'): # Sustituir el archivo PDF actual de la norma con el contenido del nuevo recién seleccionado

        sustituirNorma(idProcesoActual)
   

    window.refresh() # Actualizar cambios en componentes de la GUI
        
window.close()

# ************************************************************************************************************************

