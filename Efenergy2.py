# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

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

MENU_DISABLED_CHARACTER = '!'
MENU_KEY_SEPARATOR = '::'
SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

# Identificadores de los tipos de procesos

idGeneral = 0
idVoltaje = 1
idPotencia = 2
idArmonicos = 3

idOtroPDF = 0

idProcesoActual = None

tituloNorma = None
tituloNota = None

# Variables contenedoras del procesamiento de la plantilla con la librería Panda 

datosPreliminares = None
datosVoltaje = None
datosPotencia = None
datosArmonicos = None

# Valores para límites de variación del Voltaje

valorVariacion = 120
porcentajeLimiteInferior = 0.1 # 10%
porcentajeLimiteSuperior = 0.1 # 10%
voltajeLimiteInferior = None
voltajeLimiteSuperior = None
rangoMenor = None
rangoMayor = None

dataTable = [['','',''],]

# Contenidos para filtros presentados con el componente Combo

filtroVoltaje = ['MENOR','RANGO','MAYOR']
filtroFases = ['A','B','C']

eColor1 = '#000000' # Negro
eColor2 = '#F2F2F2' # Gris fondo ventana
eColor3 = '#FFFFFF' # Blanco
eColor4 = '#F8AF26' # Naranja
eColor5 = '#CDCDCD' # Gris botones
eColor6 = '#F2EDEA' # Gris popup
eColores1 = (eColor1,eColor5) 
eColores2 = (eColor4,eColor2) 

# Paleta colores datatables en grises y amarillo

eColor10a = '#E8E9EB' # Gris oscuro
eColor10b = '#FCFCFC' # Gris claro
eColor10c = '#F9F9F9' # Gris intermedio
eColor10d = '#FFFFEE' # Amarillo campo activo
eColor10e = '#333333' # Negro/Gris disimulado
eColor10f = '#AAAAAA' # Gris bordes campo

sizeFrmPrincipal = (1030,600) # Tamaño de la ventana principal
sizeColumnas = (1000,580) # Tamaño de las columnas que simulan ventanas ocultas
sizeSelectorPlantilla = (1000,580) # Tamaño del Input para mostrar la ruta completa de la plantilla

fontRutaPartes = ('Consolas',10)+('bold',)
fontRutaTotal = ('Consolas',10)
fontMenuPrincipal = ('Helvetica',11)
fontCombos = ('Helvetica',11)
fontAcercaDe = ('Helvetica',10)+('bold',)
fontTituloNorma = ('Helvetica',15)+('bold',)
fontTituloNota = ('Helvetica',15)+('bold',)

rutaLogoPrincipal = 'imagenes\\logo_texto_2020.png'
rutaIconoPrincipal = 'imagenes\\logo_2020.ico'

extensionesPlantillas = (('Excel','*.xls*'),)
extensionPdf = (('Archivo PDF','*.pdf'),)

barraEstado = 'SENA - CDITI - TEINNOVA - Semillero de Energías. Todos los derechos reservados. (C) 2020'

# Ubicaciones y nombre de archivo a procesar como plantilla

rutaPlantilla = None
archivoPlantilla = None
rutaPlantillaPreliminar = None

# Variables contenedoras para los textos descriptivos de las normas

informacionVoltaje = None
informacionPotencia = None
informacionArmonicos = None

# Variables globales para control de ejecución de Hilos (Threads)

t1 = None # Hilo para carga y procesamiento con la libreria Panda
t2 = None # Hilo para representación gráfica del progreso de carga de plantillas

# Rutas de archivos de apoyo con información de contexto

# Rutas relativas

rutaInformacionVoltaje = 'archivos\\InformaciónVoltaje.txt'
rutaInformacionPotencia = 'archivos\\InformaciónPotencia.txt'
rutaInformacionArmonicos = 'archivos\\InformaciónArmónicos.txt'

# Rutas absolutas

rutaPdfVoltaje = str(Path().absolute()) + '\\archivos\\NormaVoltaje.pdf'
rutaPdfPotencia = str(Path().absolute()) + '\\archivos\\NormaPotencia.pdf'
rutaPdfArmonicos = str(Path().absolute()) + '\\archivos\\NormaArmónicos.pdf'

clave = '1234' # Clave para edición de la norma

# Información para Acerca De...

descripcion = 'Efenergy es un programa diseñado para funcionar bajo Windows el cual usted podrá utilizar en el análisis de la información y presentación oportuna de informes para el control de la eficiencia energética.\n\nDiversos estándares sobre \"Calidad de Energía Eléctrica\" convergen en la necesidad de realizar mediciones con la ayuda de herramientas TRUE RMS y analizar los  datos  recolectados mediante herramientas digitales con finalidad específica como Efenergy.'
instructores = 'Semillero Energías\nViviana Ramírez Ramírez\nAndrés Tafur Piedrahita\nYuely Adriana Arce Arias'
desarrolladores = 'Hernán Arango Isaza\nWendy Vanessa Mejía Agudelo\nDiego Alexander Sepúlveda García'
copyright = '(C) 2020\nSENA - CDITI\nDosquebradas (Risaralda)'

# ************************************************************************************************************************

# BARRA DE MENÚ PRINCIPAL TODO ACTIVO

menuPrincipal1 =     [
                        [ 'Opciones', [ 'Acerca de...::-opcAcercaDe-', '---', 'Salir' ] ],
                        [ 'Voltaje',
                            [ 'Analizar Voltaje::-opcV1-' ]
                        ],
                        [ 'Potencia',
                            ['Analizar Factor de Potencia::-opcP1-', 'Analizar Potencia Reactiva::-opcP2-' ]
                        ],
                        [ 'Armónicos',
                            [ 'Analizar Armónicos de Tensión::-opcA1-', 'Analizar Armónicos de Corriente::-opcA2-', '---', 'Analizar Distorsión Armónica::-opcA3-' ],
                        ],
                        [ 'Normatividad',
                            [ 'Ver norma sobre Voltaje::-opcN1-', 'Ver norma sobre Potencia::-opcN2-', 'Ver norma sobre Armónicos::-opcN3-', 
                                '---', 'Gestión de Normas',
                                [ 'Voltaje::-opcN4-', 'Potencia::-opcN5-', 'Armónicos::-opcN6-' ],
                                '---', 'Gestión de Notas rápidas',
                                [ 'Voltaje::-opcN7-', 'Potencia::-opcN8-', 'Armónicos::-opcN9-' ],
                            ],
                        ],
                    ]

# BARRA DE MENÚ PRINCIPAL ITEMS BLOQUEADOS

menuPrincipal2 =     [
                        [ 'Opciones', [ 'Acerca de...::-opcAcercaDe-', '---', 'Salir' ] ],
                        [ '!Voltaje',
                            [ 'Analizar Voltaje::-opcV1-' ]
                        ],
                        [ '!Potencia',
                            ['Analizar Factor de Potencia::-opcP1-', 'Analizar Potencia Reactiva::-opcP2-' ]
                        ],
                        [ '!Armónicos',
                            [ 'Analizar Armónicos de Tensión::-opcA1-', 'Analizar Armónicos de Corriente::-opcA2-', '---', 'Analizar Distorsión Armónica::-opcA3-'  ],
                        ],
                        [ 'Normatividad',
                            [ 'Ver norma sobre Voltaje::-opcN1-', 'Ver norma sobre Potencia::-opcN2-', 'Ver norma sobre Armónicos::-opcN3-', 
                                '---', 'Gestión de Normas',
                                [ 'Voltaje::-opcN4-', 'Potencia::-opcN5-', 'Armónicos::-opcN6-' ],
                                '---', 'Gestión de Notas rápidas',
                                [ 'Voltaje::-opcN7-', 'Potencia::-opcN8-', 'Armónicos::-opcN9-' ],
                            ],
                        ],
                    ]

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

def definirTituloNota(tipoProceso):

    if tipoProceso == idVoltaje:

        tituloNota = 'VOLTAJE'

    elif tipoProceso == idPotencia:

        tituloNota = 'POTENCIA'

    elif tipoProceso == idArmonicos:

        tituloNota = 'ARMÓNICOS'

    window['-labelTituloNota-'].update(tituloNota)

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

def botonesGestionarNorma(estado):

    botonActualizarNorma.update(disabled=estado)
    botonDescartarGestion.update(disabled=estado)
    botonVerSeleccionado.update(disabled=estado)

# ************************************************************************************************************************

def calcularRangoVariacion():

    global voltajeLimiteInferior
    global voltajeLimiteSuperior

    try:

        intVariacion = float(window['-variacion-'].get())
        voltajeLimiteInferior = intVariacion * (1 - porcentajeLimiteInferior)
        voltajeLimiteSuperior = intVariacion * (1 + porcentajeLimiteSuperior)
        nuevoTooltip = '  El rango establecido para análisis es [ {0:.2f} - {1:.2f} ]  '.format(voltajeLimiteInferior,voltajeLimiteSuperior)
        inputVariacion.set_tooltip(nuevoTooltip)

    except ValueError:

        # Validar que la representación del string corresponde a un número
        
        window['-variacion-'].update(''.join([i for i in window['-variacion-'].get() if i.isdigit()])) 
        
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

    rutaPlantilla = values['-seleccionPlantilla-']
    archivoPlantilla = rutaPlantilla.split('/')[-1]
    window['-valorRutaPlantilla-'].Update(rutaPlantilla.rpartition('/')[0])
    window['-valorArchivoPlantilla-'].Update(archivoPlantilla)
    barraMenuPrincipal.Update(menuPrincipal1)

# ************************************************************************************************************************

def cargarDatosPreliminares(tipoProceso):

    if (tipoProceso == idGeneral):

        rutaPlantillaPreliminar = values['-seleccionPlantilla-']
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

def generarNavegacion(idConsecutivo):

    # Función especial que genera todo lo necesario para la barra de navegación.
    # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.
    # Se genera la misma estructura pero con id diferente.
    # Se utiliza haciendo un llamado con múltiple asignación de variables en línea.
    # Por ejemplo: frame1Navegacion = generarNavegacion(1)

    layoutNavegacion =  [
                            [
                                sg.Button(key='-botonInicioV' + str(idConsecutivo) + '-', 
                                          button_text='Inicio',
                                          button_color=eColores1,
                                          size=(12,1),
                                          pad=((10,5),(15,20)))
                            ],
                        ]

    globals()['frame' + str(idConsecutivo) + 'Navegacion'] = sg.Frame(key='-frameNavegacionV' + str(idConsecutivo) + '-',  
                                                                      title='  Navegación  ', 
                                                                      layout=layoutNavegacion, 
                                                                      title_color=eColor1, 
                                                                      background_color=eColor2)

# ************************************************************************************************************************

def generarLogo(idConsecutivo):

    # Función especial que genera todo lo necesario para presentar el logo en las páginas que lo requieran.
    # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.
    # Se genera la misma estructura pero con id diferente.
    # Se utiliza haciendo un llamado con múltiple asignación de variables en línea.
    # Por ejemplo: frame1Logo = generarLogo(1)

    logoPrincipal = sg.Image(key='-logoPrincipalV' + str(idConsecutivo) + '-', 
                             filename=rutaLogoPrincipal, 
                             background_color=eColor2, 
                             size=(965,100))

    statusBarPrincipal = sg.StatusBar(key='-statusBarV' + str(idConsecutivo) + '-', 
                                      text=barraEstado, 
                                      size=(1,1), 
                                      pad=((0,0),(20,20)), 
                                      text_color=eColor1, 
                                      background_color=eColor2, 
                                      relief=sg.RELIEF_FLAT, 
                                      justification='center', 
                                      visible=True)

    layoutLogo = [
                    #### Logo
                    [
                        logoPrincipal
                    ],
                    #### Barra de estado
                    [
                        statusBarPrincipal
                    ],
                ]

    globals()['frame' + str(idConsecutivo) + 'Logo'] = sg.Frame(key='-frameLogoV' + str(idConsecutivo) + '-', 
                                                                title='', 
                                                                layout=layoutLogo, 
                                                                title_color=eColor1, 
                                                                background_color=eColor2)

# ************************************************************************************************************************

def generarNotasRapidas():

    # Función especial que genera todo lo necesario para gestionar las notas rápidas sobre las normas.
    # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.

    global visorEditor
    global botonEditarNota
    global botonGrabarNota
    global botonDescartarGrabacion
    global frameNota
    global frameTituloNota
    global columna3

    visorEditor = sg.Multiline(key='-visorEditorNotas-',
                               default_text=None, 
                               size=(90,7), 
                               text_color=eColor1, 
                               background_color=eColor2, 
                               border_width=1,
                               autoscroll=False,
                               write_only=False,
                               auto_refresh=True,
                               auto_size_text=False,
                               disabled=True,
                               pad=((15,15),(15,0)))

    botonEditarNota = sg.Button(key='-botonEditarNota-',
                                button_text='Editar',
                                button_color=eColores1,
                                size=(12,1),
                                pad=((10,5),(15,20)))

    botonGrabarNota = sg.Button(key='-botonGrabarNota-',
                                button_text='Grabar',
                                button_color=eColores1,
                                size=(12,1),
                                disabled=True,
                                pad=((10,5),(15,20)))

    botonDescartarGrabacion = sg.Button(key='-botonDescartarGrabacion-',
                                        button_text='Descartar',
                                        button_color=eColores1,
                                        size=(12,1),
                                        disabled=True,
                                        pad=((10,5),(15,20)))

    layoutNotas =   [
                        #### Visor / Editor de notas rápidas
                        [
                            visorEditor
                        ],
                        #### Gestión de notas rápidas
                        [
                            botonEditarNota, botonGrabarNota, botonDescartarGrabacion
                        ],
                     ]

    layoutTituloNota =  [
                            #### Título de la sección
                            [
                                sg.Text(key='-labelTituloNota-', 
                                        text=tituloNota, 
                                        size=(15,1), 
                                        text_color=eColor1, 
                                        background_color=eColor2, 
                                        font=fontTituloNota, 
                                        pad=((0,0),(10,10))),                            
                            ],
                         ]

    frameNota = sg.Frame(key='-frameNotaRapida-', 
                         title='  Gestión de Notas Rápidas  ', 
                         layout=layoutNotas, 
                         title_color=eColor1, 
                         background_color=eColor2)

    frameTituloNota = sg.Frame(key='-frameTituloNota-', 
                               title='', 
                               layout=layoutTituloNota, 
                               title_color=eColor1, 
                               background_color=eColor2,
                               element_justification='center',
                               vertical_alignment='center')

    layoutColumna =    [
                           #### Logo + Barra
                           [
                               frame3Logo
                           ],
                           #### Título de la nota
                           [
                               frameTituloNota
                           ],
                           #### Sección de notas rápidas
                           [
                               frameNota
                           ],
                           #### Panel de navegación
                           [
                               frame2Navegacion
                           ],
                       ]

    columna3 = sg.Column(key='-columna3-', 
                         layout=layoutColumna, 
                         visible=False, 
                         background_color=eColor2, 
                         size=sizeColumnas)

# ************************************************************************************************************************

def generarGestionNormas():

    # Función especial que genera todo lo necesario para gestionar las normas en formato PDF.
    # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.

    global botonVerNorma
    global botonVerSeleccionado
    global botonActualizarNorma
    global botonDescartarGestion
    global frameNorma
    global frameTituloNorma
    global columna4

    botonVerNorma = sg.Button(key='-botonVerNorma-',
                              button_text='Ver actual',
                              button_color=eColores1,
                              size=(12,1),
                              pad=((10,5),(15,20)))

    botonVerSeleccionado = sg.Button(key='-botonVerSeleccionado-',
                                     button_text='Ver seleccionado',
                                     button_color=eColores1,
                                     size=(20,1),
                                     disabled=True,
                                     pad=((10,5),(15,20)))

    botonActualizarNorma = sg.Button(key='-botonActualizarNorma-',
                                     button_text='Actualizar',
                                     button_color=eColores1,
                                     size=(12,1),
                                     disabled=True,
                                     pad=((10,5),(15,20)))

    botonDescartarGestion = sg.Button(key='-botonDescartarGestion-',
                                      button_text='Descartar',
                                      button_color=eColores1,
                                      size=(12,1),
                                      disabled=True,
                                      pad=((10,5),(15,20)))

    layoutNormas =  [
                        #### Selector de archivos en formato PDF
                        [
                            sg.Input(key='-seleccionPDF-', 
                                     visible=True, 
                                     enable_events=True, 
                                     size=(122,1), 
                                     font=fontRutaTotal, 
                                     readonly=True, 
                                     pad=((10,0),(5,5))),

                            sg.FileBrowse(key='-botonPDF-', 
                                          button_text='Seleccionar', 
                                          button_color=eColores1, 
                                          file_types=extensionPdf, 
                                          pad=((10,10),(10,10)))
                        ],
                        #### Gestión de normas en formato PDF
                        [
                            botonVerNorma, botonVerSeleccionado, botonActualizarNorma, botonDescartarGestion
                        ],
                     ]

    layoutTituloNorma =  [
                            #### Título de la sección
                            [
                                sg.Text(key='-labelTituloNorma-', 
                                        text=tituloNorma, 
                                        size=(15,1), 
                                        text_color=eColor1, 
                                        background_color=eColor2, 
                                        font=fontTituloNorma, 
                                        pad=((0,0),(10,10))),                            
                            ],
                         ]

    frameNorma = sg.Frame(key='-frameGestionNorma-', 
                          title='  Gestión de la Norma en formato PDF  ', 
                          layout=layoutNormas, 
                          title_color=eColor1, 
                          background_color=eColor2)

    frameTituloNorma = sg.Frame(key='-frameTituloNorma-', 
                                title='', 
                                layout=layoutTituloNorma, 
                                title_color=eColor1, 
                                background_color=eColor2,
                                element_justification='center',
                                vertical_alignment='center')

    layoutColumna =    [
                           #### Logo + Barra
                           [
                               frame4Logo
                           ],
                           #### Título de la norma
                           [
                               frameTituloNorma
                           ],
                           #### Sección de notas rápidas
                           [
                               frameNorma
                           ],
                           #### Panel de navegación
                           [
                               frame3Navegacion
                           ],
                       ]

    columna4 = sg.Column(key='-columna4-', 
                         layout=layoutColumna, 
                         visible=False, 
                         background_color=eColor2, 
                         size=sizeColumnas)

# ************************************************************************************************************************

def generarAnalisisVoltaje():

    # Función especial que genera todo lo necesario para la sección de Análisis de Voltaje.
    # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.

    global layoutTabTablaContenido
    global frameSeccionVoltaje
    global frameTituloSeccionVoltaje
    global columna5

    layoutTabFiltros =  [
                            [
                                sg.Text(text='', size=(105,1), visible=True, border_width=0)
                            ],
                        ]

    layoutTabTablaContenido =  [
                                                [
                                                    # Lugar disponible para insertar la tabla generada desde el análisis de datos.
                                                ],
                                            ]

    layoutTabTabla =    [
                            [
                                #layoutTabTablaContenido,
                            ],
                        ]

    layoutTabGrafica =  [
                            [
                            ]
                        ]   

    layoutTabNotasRapidas = [
                                [
                                ]
                            ]

    layoutTabSeccionVoltaje =   [
                                    [
                                        sg.Tab('     Filtros     ', 
                                               layoutTabFiltros, 
                                               visible=True, 
                                               element_justification="left", 
                                               key='-tabFiltrosVoltaje-',
                                               background_color=eColor10c),

                                        sg.Tab('     Tabla     ', 
                                               layoutTabTabla, 
                                               visible=True, 
                                               element_justification="left", 
                                               key='-tabTablaVoltaje-',
                                               background_color=eColor10c,
                                               border_width=0),

                                        sg.Tab('     Gráfica     ', 
                                               layoutTabGrafica, 
                                               visible=True, 
                                               element_justification="left", 
                                               key='-tabGraficaVoltaje-',
                                               background_color=eColor10c),

                                        sg.Tab('     Notas     ', 
                                               layoutTabNotasRapidas, 
                                               visible=True, 
                                               element_justification="left", 
                                               key='-tabNotasRapidasVoltaje-',
                                               background_color=eColor10c),
                                    ]
                                ]

    layoutSeccionVoltaje =  [
                                #### Diseño por pestañas y tabulación
                                [
                                    sg.TabGroup(layoutTabSeccionVoltaje,
                                                key='-tabSeccionVoltaje-',
                                                enable_events=True,
                                                tab_location='top',
                                                border_width=1,
                                                title_color=eColor1,
                                                tab_background_color=eColor2,
                                                selected_title_color=eColor1,
                                                selected_background_color=eColor10a,
                                                background_color=eColor2)
                                ],
                            ]

    frameSeccionVoltaje = sg.Frame(key='-frameSeccionVoltaje-', 
                                   title='', 
                                   layout=layoutSeccionVoltaje, 
                                   size=(100, 20),
                                   title_color=eColor1, 
                                   background_color=eColor2,
                                   element_justification='left',
                                   vertical_alignment='top')

    layoutTituloSeccionVoltaje =    [
                                        #### Título de la sección
                                        [
                                            sg.Text(key='-labelTituloSeccionVoltaje-', 
                                                    text='ANÁLISIS DE VOLTAJE', 
                                                    size=(19,1), 
                                                    text_color=eColor1, 
                                                    background_color=eColor2, 
                                                    font=fontTituloNota, 
                                                    pad=((0,0),(10,10))),                            
                                        ],
                                    ]

    frameTituloSeccionVoltaje = sg.Frame(key='-frameTituloSeccionVoltaje-', 
                                         title='', 
                                         layout=layoutTituloSeccionVoltaje, 
                                         title_color=eColor1, 
                                         background_color=eColor2,
                                         element_justification='center',
                                         vertical_alignment='center')

    layoutColumna =    [
                           #### Título de la sección
                           [
                               frameTituloSeccionVoltaje
                           ],
                           #### Sección de notas rápidas
                           [
                               frameSeccionVoltaje
                           ],
                           #### Panel de navegación
                           [
                               frame4Navegacion
                           ],
                       ]

    columna5 = sg.Column(key='-columna5-', 
                         layout=layoutColumna, 
                         visible=False, 
                         background_color=eColor2, 
                         size=sizeColumnas)

# ************************************************************************************************************************

# GENERACIÓN DINÁMICA DE FRAMES PARA EL LOGO. DEBE CREARSE UNA POR CADA SIMULACIÓN DE PANTALLA MEDIANTE COLUMNAS.

generarLogo(1)
generarLogo(2)
generarLogo(3)
generarLogo(4)
generarLogo(5)

# GENERACIÓN DINÁMICA DE FRAMES PARA NAVEGACIÓN. DEBE CREARSE UNA POR CADA SIMULACIÓN DE PANTALLA MEDIANTE COLUMNAS.

generarNavegacion(1) # Ventana Acerca de
generarNavegacion(2) # Ventana Notas Rápidas
generarNavegacion(3) # Ventana Notas Rápidas
generarNavegacion(4) # Ventana Análisis de Voltaje

# GENERACIÓN DINÁMICA DEL FRAME PARA NOTAS RÁPIDAS.

generarNotasRapidas()

# GENERACIÓN DINÁMICA DEL FRAME PARA GESTIÓN DE NORMAS.

generarGestionNormas()

# GENERACIÓN DINÁMICA DEL FRAME PARA ANÁLISIS DE VOLTAJE.

generarAnalisisVoltaje()

# ************************************************************************************************************************

# SELECTOR DE PLANTILLAS DE ORIGEN DE DATOS

botonCargarPlantilla = sg.Button(key='-botonCargarPlantilla-', 
                                 button_text='Cargar',
                                 button_color=eColores1,
                                 disabled=True,
                                 size=(9,1),
                                 pad=((10,5),(15,20)))


frameLayout1 =  [
                    [
                        sg.Input(key='-seleccionPlantilla-', 
                                 visible=True, 
                                 enable_events=True, 
                                 size=(122,1), 
                                 font=fontRutaTotal, 
                                 readonly=True, 
                                 pad=((10,0),(5,5))),

                        sg.FileBrowse(key='-botonPlantilla-', 
                                      button_text='Seleccionar', 
                                      button_color=eColores1, 
                                      file_types=extensionesPlantillas, 
                                      pad=((10,10),(10,10)))
                    ],
                    [
                        sg.Text(key='-labelRutaPlantilla-', 
                                text='Ruta:', 
                                size=(8,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),

                        sg.Text(key='-valorRutaPlantilla-', 
                                text='---', 
                                size=(78,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                font=fontRutaPartes, 
                                pad=((10,0),(0,10)))
                    ],
                    [
                        sg.Text(key='-labelArchivoPlantilla-', 
                                text='Plantilla:', 
                                size=(8,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),

                        sg.Text(key='-valorArchivoPlantilla-', 
                                text='---', 
                                size=(78,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                font=fontRutaPartes, 
                                pad=((10,0),(0,10)))
                    ],
                    [
                        #### ProgressBar para indicar de manera asíncrona la carga de la plantilla
                        sg.Text(key='-labelProgressBar-', 
                                text='Carga:', 
                                size=(8,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),    
                        
                        sg.ProgressBar(key='-progressBar-', 
                                        max_value=100, 
                                        size=(59,15), 
                                        orientation='h',
                                        border_width=1,
                                        bar_color=eColores2,
                                        pad=((10,0),(0,10))),

                        botonCargarPlantilla

                    ],
                ]

barraMenuPrincipal = sg.Menu(key='-menuPrincipal-', 
                             menu_definition=menuPrincipal1,
                             text_color=eColor1,
                             background_color=eColor2,
                             font=fontMenuPrincipal)

frameSelectorPlantilla = sg.Frame(key='-frameSelectorPlantilla-', 
                                  title='  Plantilla de origen de datos  ', 
                                  layout=frameLayout1, 
                                  title_color=eColor1,
                                  background_color=eColor2)

comboDias = sg.Combo(key='-comboDias-', 
                     values=[], 
                     size=(10,1),
                     auto_size_text=False,
                     background_color=eColor3,
                     text_color=eColor1,
                     font=fontCombos,
                     disabled=True)

comboVoltaje = sg.Combo(key='-comboVoltaje-', 
                        values=filtroVoltaje, 
                        size=(10,1),
                        auto_size_text=False,
                        background_color=eColor3,
                        text_color=eColor1,
                        font=fontCombos,
                        disabled=True)

comboFases = sg.Combo(key='-comboFases-', 
                      values=filtroFases, 
                      size=(10,1),
                      auto_size_text=False,
                      background_color=eColor3,
                      text_color=eColor1,
                      font=fontCombos,
                      disabled=True)

# FRAME FILTROS

inputVariacion = sg.Input(key='-variacion-', 
                          default_text=valorVariacion,
                          visible=True, 
                          enable_events=True, 
                          size=(4,1), 
                          pad=((0,0),(0,0)), 
                          text_color=eColor1, 
                          background_color=eColor3, 
                          justification='center',
                          tooltip='Límite para análisis de variaciones en redes eléctricas',
                          disabled=False)

layoutFiltros =    [
                        [
                            #### Días disponibles
                            sg.Text(key='-labelComboDias-', 
                                    text='Días:', 
                                    size=(6,1), 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((10,0),(20,22)),
                                    tooltip='Días disponibles para análisis según plantilla'),

                            comboDias,

                            #### Voltaje MENOR, RANGO, MAYOR
                            sg.Text(key='-labelComboVoltaje-', 
                                    text='Voltaje:', 
                                    size=(6,1), 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((80,0),(20,22)),
                                    tooltip='Rangos a ser analizados conforme al límite de variación establecido'),

                            comboVoltaje,

                            #### Fase A, B, C
                            sg.Text(key='-labelComboFases-', 
                                    text='Fase:', 
                                    size=(6,1), 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((80,0),(20,22))),

                            comboFases,

                            #### Límite variaciones redes eléctricas -10% 120 +10%
                            sg.Text(key='-label1Variacion-', 
                                    text='Límites:', 
                                    size=(6,1), 
                                    text_color=eColor1,
                                    background_color=eColor2, 
                                    pad=((100,0),(20,22))),

                            sg.Text(key='-label2Variacion-',
                                    text='-{0:.0f}%'.format(porcentajeLimiteInferior*100),
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((10,5),(20,22))),
                            inputVariacion,

                            sg.Text(key='-label3Variacion-', 
                                    text='+{0:.0f}%'.format(porcentajeLimiteSuperior*100),
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((5,20),(20,22))),
                        ],
                    ]

frameFiltros = sg.Frame(key='-frameFiltros-', 
                        title='  Filtros  ', 
                        layout=layoutFiltros, 
                        title_color=eColor1, 
                        background_color=eColor2)

layoutColumna1 =    [
                        #### Logo + Barra
                        [
                            frame1Logo
                        ],
                        #### Selector de plantilla
                        [
                            frameSelectorPlantilla
                        ],
                        #### Sección de filtros
                        [
                            frameFiltros
                        ],
                    ]

columna1 = sg.Column(key='-columna1-', 
                     layout=layoutColumna1, 
                     visible=True, 
                     background_color=eColor2, 
                     size=sizeColumnas)

# Descripción de la herramienta

acercaDeDescripcion = sg.Multiline(key='-descripcionHerramienta-',
                                   default_text=descripcion, 
                                   size=(90,7), 
                                   text_color=eColor1, 
                                   background_color=eColor2, 
                                   border_width=0,
                                   autoscroll=False,
                                   write_only=True,
                                   auto_size_text=False,
                                   pad=((15,0),(15,0)))

# Información de los desarrolladores

acercaDeDesarrolladores = sg.Text(key='-textoDesarrolladores-',
                                  text=desarrolladores,
                                  text_color=eColor1, 
                                  background_color=eColor2, 
                                  pad=((10,5),(15,20)))

# Información de los instructores y asesores

acercaDeInstructores =  sg.Text(key='-textoInstructores-',
                                text=instructores,
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,5),(15,20)))

# Información del copyright

acercaDeCopyright = sg.Text(key='-textoCopyright-',
                            text=copyright,
                            text_color=eColor1, 
                            background_color=eColor2, 
                            font=fontAcercaDe,
                            pad=((25,5),(15,0)))

layoutAcercaDe = [
                    [
                        acercaDeDescripcion,
                        acercaDeCopyright
                    ],
                    [   
                        sg.Text(key='-labelDesarrolladores-',
                                    text='Desarrolladores:',
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    font=fontAcercaDe,
                                    pad=((10,5),(15,20))),

                        acercaDeDesarrolladores,

                        sg.Text(key='-labelInstructores-',
                                    text='Instructores y Asesores:',
                                    text_color=eColor1, 
                                    background_color=eColor2,
                                    font=fontAcercaDe,
                                    pad=((10,5),(15,20))),

                        acercaDeInstructores
                    ],
                ]

frameAcercaDe = sg.Frame(key='-frameAcercaDe-', 
                         title='  Acerca de Efenergy v2.0  ', 
                         layout=layoutAcercaDe, 
                         title_color=eColor1, 
                         background_color=eColor2)

layoutColumna2 =    [
                        #### Logo + Barra
                        [
                            frame2Logo
                        ],
                        #### Selector de plantilla
                        [
                            frameAcercaDe
                        ],
                        #### Panel de navegación
                        [
                            frame1Navegacion
                        ],
                    ]

columna2 = sg.Column(key='-columna2-', 
                     layout=layoutColumna2, 
                     visible=False, 
                     background_color=eColor2, 
                     size=sizeColumnas)

# FULL LAYOUT

layout =    [
                #### Barra de Menú superior principal
                [
                    barraMenuPrincipal
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
                   layout,
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

frameFiltros.expand(expand_x=True)
frameAcercaDe.expand(expand_x=True)
frameNota.expand(expand_x=True)
frameNorma.expand(expand_x=True)
frameTituloNorma.expand(expand_x=True)
frameTituloNota.expand(expand_x=True)
visorEditor.expand(expand_x=True)
frameSeccionVoltaje.expand(expand_x=True)
frameTituloSeccionVoltaje.expand(expand_x=True)
frame1Navegacion.expand(expand_x=True)
frame2Navegacion.expand(expand_x=True)
frame3Navegacion.expand(expand_x=True)
frame4Navegacion.expand(expand_x=True)

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
    
    elif event == '-seleccionPlantilla-': # Seleccionar plantilla de origen de datos

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
                             values['-comboVoltaje-'],
                             layoutTabTablaContenido)

		# 'límites de variaciones de\nredes eléctricas\n\nEn el rango de 127-10% - 127+10% \nMayor a 127+10% \nMenor a 127-10%'



    elif event == '-ThreadDone-': # Mensaje recibido desde los hilos al momento de haber finalizado las acciones que toman más tiempo

        actualizarFiltrosPlantilla()

    elif event == '-variacion-': # Rango de variación
    
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
        gestionarNota(idProcesoActual)

    elif event.endswith('-opcN8-'): # Gestionar nota rápida para Potencia

        idProcesoActual = idPotencia
        gestionarNota(idProcesoActual)

    elif event.endswith('-opcN9-'): # Gestionar nota rápida para Armónicos

        idProcesoActual = idArmonicos
        gestionarNota(idProcesoActual)

    elif event == '-botonEditarNota-': # Habilitar la zona de edición de texto de las Notas Rápidas

        editarNota()

    elif event == '-botonGrabarNota-': # Actualizar los archivos en disco con el contenido de la zona de edición de las Notas Rápidas

        grabarNota(idProcesoActual)

    elif event == '-botonDescartarGrabacion-': # Descartar el contenido de la zona de edición de las Notas Rápidas y no grabarlo

        descartarGrabacion(idProcesoActual)

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

# https://www.programiz.com/python-programming
# size(width,height)
# pad=((left,right), (top,bottom))
# if event.startswith('-XXXX-'):
# if event.endswith('-XXXX-'): --> Necesario para identicar los key en las opciones de menús --> (option::-KEY-)
# menuPrincipal[1][0] = '!' + menuPrincipal[1][0]
# window['-logoPrincipal-'].hide_row()
# window['-logoPrincipal-'].unhide_row()
# bkSizeLogo = logoPrincipal.get_size()
# logoPrincipal.set_size((1,None))
# window.refresh()
# window['-COLUMNA 2'].Update(visible=False)
# print("File      Path:", Path(__file__).absolute())
# print("Directory Path:", Path().absolute()) 
# globals()["layoutLogo" + str(idConsecutivo)] =


# ************************************************************************************************************************
