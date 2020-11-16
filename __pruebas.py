# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

import os.path

# ************************************************************************************************************************

MENU_DISABLED_CHARACTER = '!'
MENU_KEY_SEPARATOR = '::'

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

sizeFrmPrincipal = (1030,600)
sizeColumnas = (1000,580)
sizeSelectorPlantilla = (1000,580)

filtroVoltaje = ['MENOR','RANGO','MAYOR']
filtroFases = ['A','B','C']

fontRutaPartes = ("Consolas",10)+('bold',)
fontRutaTotal = ("Consolas",10)

rutaLogoPrincipal = 'imagenes/logo_texto_2020.png'
rutaIconoPrincipal = 'imagenes/logo_2020.ico'

extensionesPlantillas = (("Excel","*.xls*"),)
barraEstado = 'SENA - CDITI - TEINNOVA - Semillero de Energías. Todos los derechos reservados. (C) 2020'

eColor1 = 'black'
eColor2 = '#F2F2F2'
eColor3 = 'white'
eColores1 = ('black','#CDCDCD')

rutaPlantilla = None
archivoPlantilla = None

# ************************************************************************************************************************

# BARRA DE MENÚ PRINCIPAL TODO ACTIVO
menuPrincipal1 =     [
                        [ 'Opciones', [ 'Acerca de...::-OPC ACERCADE-', '---', 'Salir' ] ],
                        [ 'Voltaje',
                            [ 'Analizar Voltaje::-OPC V1-' ]
                        ],
                        [ 'Potencia',
                            ['Analizar Factor de Potencia::-OPC P1-', 'Potencia Reactiva::-OPC P2-' ]
                        ],
                        [ 'Armónicos',
                            [ 'Analizar Armónicos de Tensión::-OPC A1-', 'Analizar Armónicos de Corriente::-OPC A2-' ],
                        ],
                        [ 'Normatividad',
                            [ 'Ver norma sobre Voltaje::-OPC N1-', 'Ver norma sobre Potencia::-OPC N2-', 'Ver norma sobre Armónicos::-OPC N3-', '---', 'Gestión de Normas',
                                [ 'Voltaje::-OPC N4-', 'Potencia::-OPC N5-', 'Armónicos::-OPC N6-' ]
                            ],
                        ],
                    ]

# BARRA DE MENÚ PRINCIPAL ITEMS BLOQUEADOS
menuPrincipal2 =     [
                        [ 'Opciones', [ 'Acerca de...::-OPC ACERCADE-', '---', 'Salir' ] ],
                        [ '!Voltaje',
                            [ 'Analizar Voltaje::-OPC V1-' ]
                        ],
                        [ '!Potencia',
                            ['Analizar Factor de Potencia::-OPC P1-', 'Potencia Reactiva::-OPC P2-' ]
                        ],
                        [ '!Armónicos',
                            [ 'Analizar Armónicos de Tensión::-OPC A1-', 'Analizar Armónicos de Corriente::-OPC A2-' ],
                        ],
                        [ 'Normatividad',
                            [ 'Ver norma sobre Voltaje::-OPC N1-', 'Ver norma sobre Potencia::-OPC N2-', 'Ver norma sobre Armónicos::-OPC N3-', '---', 'Gestión de Normas',
                                [ 'Voltaje::-OPC N4-', 'Potencia::-OPC N5-', 'Armónicos::-OPC N6-' ]
                            ],
                        ],
                    ]

# SELECTOR DE PLANTILLAS DE ORIGEN DE DATOS
frameLayout1 =  [
                    [
                        sg.Input(key='-SELECCION PLANTILLA-', 
                                 visible=True, 
                                 enable_events=True, 
                                 size=(121,1), 
                                 font=fontRutaTotal, 
                                 readonly=True, 
                                 pad=((10,0),(5,5))),
                        sg.FileBrowse(key='-BTN PLANTILLA-', 
                                      button_text='Explorar', 
                                      size=(10,1), 
                                      button_color=eColores1, 
                                      file_types=extensionesPlantillas, 
                                      pad=((10,10),(10,10)))
                    ],
                    [
                        sg.Text(key='-LRUTA PLANTILLA-', 
                                text='Ruta:', 
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),
                        sg.Text(key='-VRUTA PLANTILLA-', 
                                text='---', 
                                size=(80,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                font=fontRutaPartes, 
                                pad=((10,0),(0,10)))
                    ],
                    [
                        sg.Text(key='-LARCHIVO PLANTILLA-', 
                                text='Archivo:', 
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),
                        sg.Text(key='-VARCHIVO PLANTILLA-', 
                                text='---', 
                                size=(80,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                font=fontRutaPartes, 
                                pad=((10,0),(0,10)))
                    ]
                ]

logoPrincipal = sg.Image(key='-LOGO PRINCIPAL-', 
                         filename=rutaLogoPrincipal, 
                         background_color=eColor2, 
                         size=(965,100))

statusBarPrincipal = sg.StatusBar(key='-STATUS BAR-', 
                                  text=barraEstado, 
                                  size=(1,1), 
                                  pad=((0,0),(20,20)), 
                                  text_color=eColor1, 
                                  background_color=eColor2, 
                                  relief=sg.RELIEF_FLAT, 
                                  justification='center', 
                                  visible=True)

# FRAME LOGO
layoutLogo =    [
                    #### Logo
                    [
                        logoPrincipal
                    ],
                    #### Barra de estado
                    [
                        statusBarPrincipal
                    ],
                ]

frameLogo = sg.Frame(key='-FRAME LOGO', 
                     title='', 
                     layout=layoutLogo, 
                     title_color=eColor1, 
                     background_color=eColor2)

barraMenuPrincipal = sg.Menu(key='-MENU PRINCIPAL-', menu_definition=menuPrincipal1)

frameSelectorPlantilla = sg.Frame(key='-FRAME SELECTORPLANTILLA', 
                                  title='  Seleccionar plantilla de origen de datos  ', 
                                  layout=frameLayout1, 
                                  title_color=eColor1,
                                  background_color=eColor2)

comboboxDias = sg.Combo(key='-COMBOBOX DIAS', 
                        values=[], 
                        size=(10,1),
                        auto_size_text=False,
                        background_color=eColor3,
                        text_color=eColor1)

comboboxVoltaje = sg.Combo(key='-COMBOBOX VOLTAJE', 
                         values=filtroVoltaje, 
                         size=(10,1),
                         auto_size_text=False,
                         background_color=eColor3,
                         text_color=eColor1)

comboboxFases = sg.Combo(key='-COMBOBOX FASES', 
                         values=filtroFases, 
                         size=(10,1),
                         auto_size_text=False,
                         background_color=eColor3,
                         text_color=eColor1)

# FRAME FILTROS
inputVariacion = sg.Input(key='-VARIACION-', 
                          visible=True, 
                          enable_events=True, 
                          size=(4,1), 
                          pad=((10,0),(2,0)), 
                          text_color=eColor1, 
                          background_color=eColor3, 
                          justification='center')
layoutFiltros =    [
                    [
                        #### Días disponibles
                        sg.Text(key='-LCOMBOBOX DIAS-', 
                                text='Días:', 
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(2,10))),
                        comboboxDias,
                        #### Voltaje RANGO, MENOR, MAYOR
                        sg.Text(key='-LCOMBOBOX VOLTAJE-', 
                                text='Voltaje:', 
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(2,10))),
                        comboboxVoltaje,
                        #### Fase A, B, C
                        sg.Text(key='-LCOMBOBOX FASES-', 
                                text='Fases:', 
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(2,10))),
                        comboboxFases,
                        #### Límite variaciones redes eléctricas -10% 120 +10%
                        sg.Text(key='-L1 VARIACION-', 
                                text='Límites:', 
                                size=(6,1), 
                                text_color=eColor1,
                                background_color=eColor2, 
                                pad=((10,0),(2,10))),
                        sg.Text(key='-L2 VARIACION-', 
                                text='-10%', 
                                size=(5,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(2,10))),
                        inputVariacion,
                        sg.Text(key='-L3 VARIACION-', 
                                text='+10%', 
                                size=(5,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,20),(2,10))),
                    ],
                ]

inputVariacion.Update = 120

frameFiltros = sg.Frame(key='-FRAME FILTROS', 
                        title='  Filtros  ', 
                        layout=layoutFiltros, 
                        title_color=eColor1, 
                        background_color=eColor2)

layoutColumna1 =    [
                        #### Logo + Barra
                        [
                            frameLogo
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

columna1 = sg.Column(key='-COLUMNA 1', 
                     layout=layoutColumna1, 
                     visible=True, 
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
                    columna1, 
                    #columna2
                ],
            ]

# ************************************************************************************************************************

# Cambiar al tema personalizado
sg.theme('Default1')
sg.ChangeLookAndFeel('SystemDefault')

# ************************************************************************************************************************

window = sg.Window(
        'Efenergy v2.0',
        layout,
        use_default_focus=True,
        size=sizeFrmPrincipal,
        debugger_enabled=False,
        finalize=True,
        font=("Helvetica",11),
        icon=rutaIconoPrincipal
   )

# ************************************************************************************************************************

# Habilitar barra de menú con opciones deshabilitadas
barraMenuPrincipal.Update(menuPrincipal2)

window.refresh()

# ************************************************************************************************************************

# Run the Event Loop
while True:

    event, values = window.read()

    print(event)

    # Salir de la aplicación
    if event == sg.WIN_CLOSED or event == 'Salir':

        break

    # Salir de la aplicación
    if event.endswith('-OPC SALIR-'):

        break

    if event == '-SELECCION PLANTILLA-':

        rutaPlantilla = values['-SELECCION PLANTILLA-']
        archivoPlantilla = rutaPlantilla.split('/')[-1]
        window['-VRUTA PLANTILLA-'].Update(rutaPlantilla.rpartition('/')[0])
        window['-VARCHIVO PLANTILLA-'].Update(archivoPlantilla)
        barraMenuPrincipal.Update(menuPrincipal1)

    # Analizar Voltaje
    if event.endswith('-OPC V1-'):
        rutaPlantillaVoltaje = values['-SELECCION PLANTILLA-']
        archivo_voltaje = pandas.ExcelFile(rutaPlantillaVoltaje)
        comboboxDias.Update(values=archivo_voltaje.sheet_names)
      

        
        

window.close()

# ************************************************************************************************************************

# https://www.programiz.com/python-programming
# size(width,height)
# pad=((left,right), (top,bottom))
# if event.startswith('-XXXX-'):
# if event.endswith('-XXXX-'): --> Necesario para identicar los key en las opciones de menús --> (option::-KEY-)
# menuPrincipal[1][0] = '!' + menuPrincipal[1][0]
# window['-LOGO PRINCIPAL-'].hide_row()
# window['-LOGO PRINCIPAL-'].unhide_row()
# bkSizeLogo = logoPrincipal.get_size()
# logoPrincipal.set_size((1,None))
# window.refresh()
# window['-COLUMNA 2'].Update(visible=False)

# ************************************************************************************************************************
