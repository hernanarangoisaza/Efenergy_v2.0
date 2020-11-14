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

# BARRA DE MENÚ PRINCIPAL
menuPrincipal =     [
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

# SELECCIONADOR DE PLANTILLAS
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

# FULL LAYOUT
layout =    [
                #### Barra de Menú superior principal
                [ 
                    sg.Menu(menuPrincipal, tearoff=False) 
                ],
                #### Logo
                [ 
                    sg.Image(filename=rutaLogoPrincipal, background_color=eColor2, size=(600,100)) 
                ],
                #### Barra de estado
                [ 
                    sg.StatusBar(text=barraEstado, size=(1200,1), pad=((50,50),(20,20)), text_color=eColor1, background_color=eColor2, relief=sg.RELIEF_FLAT, justification='center', visible=True, key='status_bar')
                ],
                #### Selector de plantilla
                [ 
                    sg.Frame('  Seleccionar plantilla de origen de datos  ', frameLayout1, pad=((15,15),(0,0)), title_color=eColor1, background_color=eColor2)
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

        rutaPlantilla = values[ '-SELECCION PLANTILLA-' ]
        archivoPlantilla = rutaPlantilla.split('/')[-1]
        window['-VRUTA PLANTILLA-'].Update(rutaPlantilla.rpartition('/')[0])
        window['-VARCHIVO PLANTILLA-'].Update(archivoPlantilla)

    # Analizar Voltaje
    if event.endswith('-OPC V1-'):

        break

window.close()

# ************************************************************************************************************************

# https://www.programiz.com/python-programming
# size(width,height)
# pad=((left,right), (top,bottom))
# if event.startswith('-XXXX-'):
# if event.endswith('-XXXX-'): --> Necesario para identicar los key en las opciones de menús --> (option::-KEY-) 

# ************************************************************************************************************************
