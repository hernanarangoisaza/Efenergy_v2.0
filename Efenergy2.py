# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import sys



#from Efenergy2UI import *
#import Efenergy2Globales

from Efenergy2Globales import *
import Efenergy2UI
import Efenergy2NotasRapidas
import Efenergy2Normas
import Efenergy2Funciones

import os.path
import ctypes
from pathlib import Path

#import wx
import wx.grid

from AnalisisDatosVoltaje import AnalisisDatosVoltaje

#from AnalisisDatosPotencia import AnalisisDatosPotencia
#from AnalisisDatosPotenciaReactiva import AnalisisDatosPotenciaReactiva
#from AnalisisDatosArmonicos import AnalisisDatosArmonicos
#from AnalisisDatosArmonicosCorriente import AnalisisDatosArmonicosCorriente
#from EditarInformacion import EditarInformacion

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

frameFiltrosVoltaje, comboDias, comboVoltaje, comboFases, inputVariacion = Efenergy2UI.generarFiltrosVoltaje()
columna5, frameSeccionVoltaje, frameTituloSeccionVoltaje, tablaVoltaje = Efenergy2UI.generarAnalisisVoltaje(frameNavegacionV4, frameFiltrosVoltaje)
 
# ************************************************************************************************************************

# GENERACIÓN DE LA INTERFAZ DE USUARIO PRINCIPAL

columna1, barraMenuPrincipal, frameSelectorPlantilla, inputSeleccionPlantilla, botonCargarPlantilla = Efenergy2UI.generarUIPrincipal(frameLogoV1)
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

# Carga los textos descriptivos para las notas

errorPersonalizadoNotasLeer = 'Ocurrió un problema al leer el archivo de texto de Notas Rápidas.'

informacionVoltaje = Efenergy2Funciones.leerArchivo(rutaInformacionVoltaje, errorPersonalizadoNotasLeer)
informacionPotencia = Efenergy2Funciones.leerArchivo(rutaInformacionPotencia, errorPersonalizadoNotasLeer)
informacionArmonicos = Efenergy2Funciones.leerArchivo(rutaInformacionArmonicos, errorPersonalizadoNotasLeer)

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

# Run the Event Loop.

while True:

    event, values = window.read()

    print(event)

    if event == sg.WIN_CLOSED or event == 'Salir': # Salir de la aplicación

        break
    
    elif event == '-inputSeleccionPlantilla-': # Seleccionar plantilla de origen de datos

        Efenergy2Funciones.seleccionarPlantilla(values, window, barraMenuPrincipal)
        botonCargarPlantilla.update(disabled=False)

    elif event == '-botonCargarPlantilla-': # Cargar plantilla de origen de datos

        Efenergy2Funciones.cargarDatosPreliminares(idGeneral, values, window)

    elif event.endswith('-opcV1-'): # Analizar Voltaje

        idProcesoActual = idVoltaje
        columna1.Update(visible=False)
        columna5.Update(visible=True)

        datosVoltaje = Efenergy2Funciones.asignarDatosPreliminares()

        voltajeLimiteInferior, voltajeLimiteSuperior = Efenergy2Funciones.calcularRangoVariacion(window, values, inputVariacion)

        AnalisisDatosVoltaje(datosVoltaje, 
                             voltajeLimiteInferior, 
                             voltajeLimiteSuperior, 
                             values['-comboDias-'], 
                             values['-comboFases-'],
                             values['-comboVoltaje-'],
                             window,
                             tablaVoltaje)

        tablaVoltaje.expand(expand_x=True)

		# 'límites de variaciones de\nredes eléctricas\n\nEn el rango de 127-10% - 127+10% \nMayor a 127+10% \nMenor a 127-10%'

    elif event == '-ThreadDone-': # Mensaje recibido desde los hilos al momento de haber finalizado las acciones que toman más tiempo

        Efenergy2Funciones.actualizarFiltrosPlantilla(comboDias, comboFases, comboVoltaje)

    elif event == '-inputVariacion-': # Rango de variación
    
        voltajeLimiteInferior, voltajeLimiteSuperior = Efenergy2Funciones.calcularRangoVariacion(window, values, inputVariacion)

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
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual, window, columna1, columna3, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacionVoltaje)

    elif event.endswith('-opcN8-'): # Gestionar nota rápida para Potencia

        idProcesoActual = idPotencia
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual, window, columna1, columna3, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacionPotencia)

    elif event.endswith('-opcN9-'): # Gestionar nota rápida para Armónicos

        idProcesoActual = idArmonicos
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual, window, columna1, columna3, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacionArmonicos)

    elif event == '-botonEditarNota-': # Habilitar la zona de edición de texto de las Notas Rápidas

        Efenergy2NotasRapidas.editarNota(botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor)

    elif event == '-botonGrabarNota-': # Actualizar los archivos en disco con el contenido de la zona de edición de las Notas Rápidas

        txtVisorEditor = values['-visorEditorNotas-']

        if (idProcesoActual == idVoltaje):

            informacionVoltaje = Efenergy2NotasRapidas.grabarNota(idProcesoActual, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, rutaInformacionVoltaje, txtVisorEditor)

        elif (idProcesoActual == idPotencia):

            informacionPotencia = Efenergy2NotasRapidas.grabarNota(idProcesoActual, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, rutaInformacionPotencia, txtVisorEditor)

        elif (idProcesoActual == idArmonicos):

            informacionArmonicos = Efenergy2NotasRapidas.grabarNota(idProcesoActual, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, rutaInformacionArmonicos, txtVisorEditor)

    elif event == '-botonDescartarGrabacion-': # Descartar el contenido de la zona de edición de las Notas Rápidas y no grabarlo

        if (idProcesoActual == idVoltaje):

            Efenergy2NotasRapidas.descartarGrabacion(botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacionVoltaje)

        elif (idProcesoActual == idPotencia):

            Efenergy2NotasRapidas.descartarGrabacion(botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacionPotencia)

        elif (idProcesoActual == idArmonicos):

            Efenergy2NotasRapidas.descartarGrabacion(botonEditarNota, botonGrabarNota, botonDescartarGrabacion, visorEditor, informacionArmonicos)

    elif event.endswith('-opcN1-'): # Ver norma Pdf para Voltaje

        idProcesoActual = idVoltaje
        Efenergy2Normas.visualizarNorma(idProcesoActual)

    elif event.endswith('-opcN2-'): # Ver norma Pdf para Potencia

        idProcesoActual = idPotencia
        Efenergy2Normas.visualizarNorma(idProcesoActual)

    elif event.endswith('-opcN3-'): # Ver norma Pdf para Armónicos

        idProcesoActual = idArmonicos
        Efenergy2Normas.visualizarNorma(idProcesoActual)

    elif event.endswith('-opcN4-'): # Gestionar norma Pdf para Voltaje

        idProcesoActual = idVoltaje
        Efenergy2Normas.definirTituloNorma(idProcesoActual, columna1, columna4, labelTituloNorma)

    elif event.endswith('-opcN5-'): # Gestionar norma Pdf para Potencia

        idProcesoActual = idPotencia
        Efenergy2Normas.definirTituloNorma(idProcesoActual, columna1, columna4, labelTituloNorma)

    elif event.endswith('-opcN6-'): # Gestionar norma Pdf para Armónicos

        idProcesoActual = idArmonicos
        Efenergy2Normas.definirTituloNorma(idProcesoActual, columna1, columna4, labelTituloNorma)

    elif event == ('-inputSeleccionPDF-'): # Control de la barra de botones para la gestión de normas

        Efenergy2Normas.botonesGestionarNorma(False, botonActualizarNorma, botonDescartarGestion, botonVerSeleccionado)

    elif event == ('-botonVerNorma-'): # Ver archivo PDF para el contenido de la norma actual

        Efenergy2Normas.visualizarNorma(idProcesoActual, values)
 
    elif event == ('-botonVerSeleccionado-'): # Ver archivo PDF para el contenido de la nueva norma seleccionada

        Efenergy2Normas.visualizarNorma(idOtroPDF, values)

    elif event == ('-botonDescartarGestion-'): # Control de la barra de botones para la gestión de normas

        Efenergy2Normas.botonesGestionarNorma(True, botonActualizarNorma, botonDescartarGestion, botonVerSeleccionado)
        window['-inputSeleccionPDF-'].update('')

    elif event == ('-botonActualizarNorma-'): # Sustituir el archivo PDF actual de la norma con el contenido del nuevo recién seleccionado

        Efenergy2Normas.sustituirNorma(idProcesoActual, botonActualizarNorma, botonDescartarGestion, botonVerSeleccionado, window, values)

    window.refresh() # Actualizar cambios en componentes de la GUI

window.close()
    