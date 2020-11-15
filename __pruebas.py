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

rutaLogoPrincipal = 'imagenes/logo_texto_2020.png'
rutaIconoPrincipal = 'imagenes/logo_2020.ico'

extensionesPlantillas = (("Excel", "*.xls*"),)
barraEstado = 'SENA - CDITI - TEINNOVA - Semillero de Energías. Todos los derechos reservados. (C) 2020'

eColor1 = 'black'
eColor2 = '#F2F2F2'
eColores1 = ('black', '#CDCDCD')

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
                        sg.Input(key='-SELECCION PLANTILLA-', visible=True, enable_events=True, size=(85,1), font=("Consolas",9), readonly=True, pad=((10,0),(5,5))),
                        sg.FileBrowse(button_text='Explorar', key='-BTN PLANTILLA-', size=(10,1), button_color=eColores1, file_types=extensionesPlantillas)
                    ],
                    [
                        sg.Text('Ruta:', key='-LRUTA PLANTILLA-', size=(6,1), text_color=eColor1, background_color=eColor2),
                        sg.Text('---', key='-VRUTA PLANTILLA-' , size=(80,1), text_color=eColor1, background_color=eColor2, font=("Consolas",9)+('bold',))
                    ],
                    [
                        sg.Text('Archivo:', key='-LARCHIVO PLANTILLA-', size=(6,1), text_color=eColor1, background_color=eColor2),
                        sg.Text('---', key='-VARCHIVO PLANTILLA-' , size=(80,1), text_color=eColor1, background_color=eColor2, font=("Consolas",9)+('bold',))
                    ]
                ]

barraMenuPrincipal = sg.Menu(menuPrincipal1, key='-MENU PRINCIPAL-')
frameSelectorPlantilla = sg.Frame('  Seleccionar plantilla de origen de datos  ', frameLayout1, pad=((15,15),(0,0)), title_color=eColor1, background_color=eColor2)
logoPrincipal = sg.Image(filename=rutaLogoPrincipal, background_color=eColor2, size=(600,100), key='-LOGO PRINCIPAL-')
statusBarPrincipal = sg.StatusBar(text=barraEstado, size=(1200,1), pad=((50,50),(20,20)), text_color=eColor1, background_color=eColor2, relief=sg.RELIEF_FLAT, justification='center', visible=True, key='status_bar')

# FULL LAYOUT
layout =    [
                #### Barra de Menú superior principal
                [
                    barraMenuPrincipal
                ],
                #### Logo
                [
                    logoPrincipal
                ],
                #### Barra de estado
                [
                    statusBarPrincipal
                ],
                #### Selector de plantilla
                [
                    frameSelectorPlantilla
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
        size=(750,600),
        #element_padding=(0, 0),
        #margins=(10, 10),
        debugger_enabled=False,
        finalize=True,
        font=("Helvetica",11),
        icon=rutaIconoPrincipal
   )

# ************************************************************************************************************************

barraMenuPrincipal.Update(menuPrincipal2)
frameSelectorPlantilla.Update(visible=True)
logoPrincipal.Update(visible=True)
statusBarPrincipal.Update(visible=False)
barraMenuPrincipal.Update(visible=False)
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
    #if event.endswith('-OPC N1-'):

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

# ************************************************************************************************************************
