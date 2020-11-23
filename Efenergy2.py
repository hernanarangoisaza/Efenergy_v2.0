# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import sys
import os.path
import ctypes
from pathlib import Path

from Efenergy2Globales import *
import Efenergy2UI
import Efenergy2NotasRapidas
import Efenergy2Normas
import Efenergy2Funciones
from Efenergy2AnalisisVoltaje import Efenergy2AnalisisVoltaje




#import wx
#import wx.grid



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

frameFiltrosVoltaje, comboDias, comboVoltaje, comboFases = Efenergy2UI.generarFiltrosVoltaje()
columna5, frameSeccionVoltaje, frameTituloSeccionVoltaje = Efenergy2UI.generarAnalisisVoltaje(frameNavegacionV4, frameFiltrosVoltaje)
 
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

window['-inputVariacion-'].update = valorVariacion

# Habilitar barra de menú con opciones deshabilitadas.

window['-menuPrincipal-'].update(menuPrincipal2)

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

        Efenergy2Funciones.seleccionarPlantilla(values, window)
        window['-botonCargarPlantilla-'].update(disabled=False)

    elif event == '-botonCargarPlantilla-': # Cargar plantilla de origen de datos

        Efenergy2Funciones.cargarDatosPreliminares(idGeneral, values, window)

    elif event.endswith('-opcV1-'): # Analizar Voltaje

        idProcesoActual = idVoltaje
        window['-columna1-'].update(visible=False)
        window['-columna5-'].update(visible=True)

        datosVoltaje = Efenergy2Funciones.asignarDatosPreliminares()

        voltajeLimiteInferior, voltajeLimiteSuperior = Efenergy2Funciones.calcularRangoVariacion(window, values)

        Efenergy2AnalisisVoltaje(datosVoltaje, 
                                 voltajeLimiteInferior, 
                                 voltajeLimiteSuperior, 
                                 values['-comboDias-'], 
                                 values['-comboFases-'],
                                 values['-comboVoltaje-'],
                                 window)

        window['-tablaVoltaje-'].expand(expand_x=True)

        window['-visorTabNotasRapidas-'].update(value=informacionVoltaje)
        window['-visorTabNotasRapidas-'].expand(expand_x=True, expand_y=True)

		# 'límites de variaciones de\nredes eléctricas\n\nEn el rango de 127-10% - 127+10% \nMayor a 127+10% \nMenor a 127-10%'

    elif event == '-ThreadDone-': # Mensaje recibido desde los hilos al momento de haber finalizado las acciones que toman más tiempo

        window['-menuPrincipal-'].update(menuPrincipal1)
        Efenergy2Funciones.actualizarFiltrosPlantilla(window)

    elif event == '-inputVariacion-': # Rango de variación
    
        voltajeLimiteInferior, voltajeLimiteSuperior = Efenergy2Funciones.calcularRangoVariacion(window, values)
        window['-botonFiltrarTablaVoltajes-'].update(disabled=False)

    elif event.endswith('-opcAcercaDe-'): # Ventana Acerca de

        window['-columna1-'].update(visible=False)
        window['-columna2-'].update(visible=True)

    elif event == '-botonInicioV1-': # Boton INICIO desde la ventana Acerca de

        window['-columna1-'].update(visible=True)
        window['-columna2-'].update(visible=False)

    elif event == '-botonInicioV2-': # Boton INICIO desde la ventana Notas Rápidas

        window['-columna1-'].update(visible=True)
        window['-columna3-'].update(visible=False)

    elif event == '-botonInicioV3-': # Boton INICIO desde la ventana Notas Rápidas

        window['-columna1-'].update(visible=True)
        window['-columna4-'].update(visible=False)

    elif event == '-botonInicioV4-': # Boton INICIO desde la ventana Análisis de Voltaje

        window['-columna1-'].update(visible=True)
        window['-columna5-'].update(visible=False)

    elif event.endswith('-opcN7-'): # Gestionar nota rápida para Voltaje

        idProcesoActual = idVoltaje
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual, window, informacionVoltaje)

    elif event.endswith('-opcN8-'): # Gestionar nota rápida para Potencia

        idProcesoActual = idPotencia
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual, window, informacionPotencia)

    elif event.endswith('-opcN9-'): # Gestionar nota rápida para Armónicos

        idProcesoActual = idArmonicos
        Efenergy2NotasRapidas.gestionarNota(idProcesoActual, window, informacionArmonicos)

    elif event == '-botonEditarNota-': # Habilitar la zona de edición de texto de las Notas Rápidas

        Efenergy2NotasRapidas.editarNota(window)

    elif event == '-botonGrabarNota-': # Actualizar los archivos en disco con el contenido de la zona de edición de las Notas Rápidas

        txtVisorEditor = values['-visorEditorNotas-']

        if (idProcesoActual == idVoltaje):

            informacionVoltaje = Efenergy2NotasRapidas.grabarNota(idProcesoActual, rutaInformacionVoltaje, txtVisorEditor, window)

        elif (idProcesoActual == idPotencia):

            informacionPotencia = Efenergy2NotasRapidas.grabarNota(idProcesoActual, rutaInformacionPotencia, txtVisorEditor, window)

        elif (idProcesoActual == idArmonicos):

            informacionArmonicos = Efenergy2NotasRapidas.grabarNota(idProcesoActual, rutaInformacionArmonicos, txtVisorEditor, window)

    elif event == '-botonDescartarGrabacion-': # Descartar el contenido de la zona de edición de las Notas Rápidas y no grabarlo

        if (idProcesoActual == idVoltaje):

            Efenergy2NotasRapidas.descartarGrabacion(informacionVoltaje, window)

        elif (idProcesoActual == idPotencia):

            Efenergy2NotasRapidas.descartarGrabacion(informacionPotencia, window)

        elif (idProcesoActual == idArmonicos):

            Efenergy2NotasRapidas.descartarGrabacion(informacionArmonicos, window)

    elif event.endswith('-opcN1-'): # Ver norma Pdf para Voltaje

        idProcesoActual = idVoltaje
        Efenergy2Normas.visualizarNorma(idProcesoActual, values)

    elif event.endswith('-opcN2-'): # Ver norma Pdf para Potencia

        idProcesoActual = idPotencia
        Efenergy2Normas.visualizarNorma(idProcesoActual, values)

    elif event.endswith('-opcN3-'): # Ver norma Pdf para Armónicos

        idProcesoActual = idArmonicos
        Efenergy2Normas.visualizarNorma(idProcesoActual, values)

    elif event.endswith('-opcN4-'): # Gestionar norma Pdf para Voltaje

        idProcesoActual = idVoltaje
        Efenergy2Normas.definirTituloNorma(idProcesoActual, labelTituloNorma, window)

    elif event.endswith('-opcN5-'): # Gestionar norma Pdf para Potencia

        idProcesoActual = idPotencia
        Efenergy2Normas.definirTituloNorma(idProcesoActual, labelTituloNorma, window)

    elif event.endswith('-opcN6-'): # Gestionar norma Pdf para Armónicos

        idProcesoActual = idArmonicos
        Efenergy2Normas.definirTituloNorma(idProcesoActual, labelTituloNorma, window)

    elif event == ('-inputSeleccionPDF-'): # Control de la barra de botones para la gestión de normas

        Efenergy2Normas.botonesGestionarNorma(False, window)


    elif event == ('-botonVerNorma-'): # Ver archivo PDF para el contenido de la norma actual

        Efenergy2Normas.visualizarNorma(idProcesoActual, values)
 
    elif event == ('-botonVerSeleccionado-'): # Ver archivo PDF para el contenido de la nueva norma seleccionada

        Efenergy2Normas.visualizarNorma(idOtroPDF, values)

    elif event == ('-botonDescartarGestion-'): # Control de la barra de botones para la gestión de normas

        Efenergy2Normas.botonesGestionarNorma(True, window)
        window['-inputSeleccionPDF-'].update('')

    elif event == ('-botonActualizarNorma-'): # Sustituir el archivo PDF actual de la norma con el contenido del nuevo recién seleccionado

        Efenergy2Normas.sustituirNorma(idProcesoActual, window, values)

    elif event == ('-comboDias-') or event == ('-comboVoltaje-') or event == ('-comboFases-'): # Habilitar el botón para filtros de Voltaje

        window['-botonFiltrarTablaVoltajes-'].update(disabled=False)

    elif event == ('-botonFiltrarTablaVoltajes-'): # Aplicar el filtro vigente representado por el estado de los combo y el rango del voltaje.
    
        datosVoltaje = Efenergy2Funciones.asignarDatosPreliminares()

        voltajeLimiteInferior, voltajeLimiteSuperior = Efenergy2Funciones.calcularRangoVariacion(window, values)

        Efenergy2AnalisisVoltaje(datosVoltaje, 
                                 voltajeLimiteInferior, 
                                 voltajeLimiteSuperior, 
                                 values['-comboDias-'], 
                                 values['-comboFases-'],
                                 values['-comboVoltaje-'],
                                 window)

        window['-tablaVoltaje-'].expand(expand_x=True)

    window.refresh() # Actualizar cambios en componentes de la GUI

window.close()
    