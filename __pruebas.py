#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

import os.path

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

rutaLogoPrincipal = 'imagenes/logo_texto_2020.png'

eColor1 = 'black'
eColor2 = '#F2F2F2'
eColores1 = ( 'black', '#CDCDCD' )

opened1 = True
opened2 = True
opened3 = True
openedCol1 = True
openedCol2 = True



def collapse( layout, key, visible ):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this seciton visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin( elem=sg.Column( layout, key=key, background_color=eColor2, pad=( 0, ( 0, 0 ) ), visible=visible ), shrink=True)

# Add your new theme colors and settings 
sg.LOOK_AND_FEEL_TABLE[ 'TemaEfenergyV2' ] = {  'BACKGROUND': '#FCFCFC', 
                                                'TEXT': '', 
                                                'INPUT': '', 
                                                'TEXT_INPUT': '', 
                                                'SCROLL': '', 
                                                'BUTTON': ( '', '' ), 
                                                'PROGRESS': ( '', '' ), 
                                                'BORDER': 1, 
                                                'SLIDER_DEPTH': 0,  
                                                'PROGRESS_DEPTH': 0, } 


menuPrincipal =     [
                        [ 'Opciones', [ 'Acerca de...', '---', 'Salir' ] ],                    
                        [ 'Voltaje', 
                            [ 'Analizar Voltaje' ]
                        ],
                        [ 'Potencia', 
                            ['Analizar Factor de Potencia', 'Potencia Reactiva' ]
                        ],
                        [ 'Armónicos',
                            [ 'Analizar Armónicos de Tensión', 'Analizar Armónicos de Corriente' ],
                        ],
                        [ 'Normatividad',
                            [ 'Ver norma sobre Voltaje', 'Ver norma sobre Potencia', 'Ver norma sobre Armónicos', '---', 'Gestión de Normas',
                                [ 'Voltaje', 'Potencia', 'Armónicos' ]
                            ],
                        ],
                    ]

# BARRA DE MENÚ PRINCIPAL
menu1 =     [
                [ 'Opciones', [ 'Acerca de...', 'Salir' ] ],
            ]

# VOLTAJE
seccion1 =  [ 
                [ 
                    sg.Button( button_text='Analizar voltaje', key='-BTN VOLTAJE1-', button_color=eColores1 ),
                    sg.Button( button_text='Ver norma de referencia', key='-BTN VOLTAJE2-', button_color=eColores1 ) 
                ] 
            ]

# POTENCIA
seccion2 =  [ 
                [ 
                    sg.Button( button_text='Analizar factor de potencia', key='-BTN POTENCIA1-', button_color=eColores1 ),
                    sg.Button( button_text='Potencia reactiva', key='-BTN POTENCIA2-', button_color=eColores1 ),
                    sg.Button( button_text='Ver norma de referencia', key='-BTN POTENCIA3-', button_color=eColores1 ) 
                ] 
            ]

# ARMÓNICOS
seccion3 =  [ 
                [ 
                    sg.Button( button_text='Analizar armónicos de tensión', key='-BTN ARMONICOS1-', button_color=eColores1 ),
                    sg.Button( button_text='Analizar armónicos de corriente', key='-BTN ARMONICOS2-', button_color=eColores1 ),
                    sg.Button( button_text='Ver norma de referencia', key='-BTN ARMONICOS3-', button_color=eColores1 ) 
                ] 
            ]

# GESTIÓN DE LAS NORMAS DE REFERENCIA
seccion4 =  [ 
                [ 
                    sg.Button( button_text='Norma para voltaje', key='-BTN NORMA1-', button_color=eColores1 ),
                    sg.Button( button_text='Norma para potencia', key='-BTN NORMA2-', button_color=eColores1 ),
                    sg.Button( button_text='Norma para armónicos', key='-BTN NORMA3-', button_color=eColores1 ) 
                ] 
            ]

columna1 =  [
                #### Logo
                [ sg.Image( filename=rutaLogoPrincipal, background_color=eColor2, size=( 600, 100 ) ) ],
                [],
                #### Selector de plantilla
                [ sg.Text( text='Seleccionar plantilla de origen de datos', background_color=eColor2, text_color=eColor1 ) ],
                [ sg.Input( key='-ARCHIVO PLANTILLA-', visible=True, enable_events=True, size=( 68, 1 ) ), 
                  sg.FileBrowse( button_text='Buscar', button_color=eColores1 ) ],
                [],
                #### Sección 1 ####
                [ sg.Text( text=SYMBOL_DOWN, enable_events=True, key='-OPEN SEC1-', background_color=eColor2, text_color=eColor1 ), 
                  sg.Text( text='VOLTAJE', enable_events=True, key='-OPEN SEC1-TEXT', background_color=eColor2, text_color=eColor1 ) ],
                [ collapse( seccion1, '-SEC1-', visible=True ) ],
                [],
                #### Sección 2 ####
                [ sg.Text( text=SYMBOL_DOWN, enable_events=True, key='-OPEN SEC2-', background_color=eColor2, text_color=eColor1 ),
                  sg.Text( text='POTENCIA', enable_events=True, key='-OPEN SEC2-TEXT', background_color=eColor2, text_color=eColor1 )],
                [ collapse( seccion2, '-SEC2-', visible=True ) ],
                [],
                #### Sección 3 ####
                [ sg.Text( text=SYMBOL_DOWN, enable_events=True, key='-OPEN SEC3-', background_color=eColor2, text_color=eColor1 ),
                  sg.Text( text='ARMÓNICOS', enable_events=True, key='-OPEN SEC3-TEXT', background_color=eColor2, text_color=eColor1 )],
                [ collapse( seccion3, '-SEC3-', visible=True ) ],
            ]

            # SYMBOL_DOWN SE CONFIGURA CON VISIBLE=TRUE Y OPENED=TRUE
            # SYMBOL_UP SE CONFIGURA CON VISIBLE=FALSE Y OPENED=FALSE

columna2 =  [
                #### Selector de plantilla
                [ sg.Text( 'Lorem Ipsum Lorem Ipsum' ) ]
            ]

# FULL LAYOUT
layout =    [
                [
                    sg.Menu( menuPrincipal, tearoff=False, pad=( 0, 0) ),
                    sg.Column( columna1, size=( 650, 575 ), background_color=eColor2, vertical_alignment='center', pad=(( 0, 0 ), ( 0, 0 ) ), key='-COL1-' ),
                    sg.Column( columna2, size=( 550, 575 ), background_color=eColor2, pad=(( 0, 0 ), ( 0, 0 ) ), key='-COL2-' ),
                ]
            ]

# Cambiar al tema personalizado 
sg.theme('TemaEfenergyV2') 

window = sg.Window(
        'Efenergy v2.0',
        layout,
        use_default_focus=True,
        size=( 1200, 600 ),
        #element_padding=( 0, 0 ),
        #margins=( 10, 10 ),
        debugger_enabled=False,
        finalize=True,
        font=("Helvetica", 11)
    )

# Run the Event Loop
while True:
    
    event, values = window.read()
    
    # Salir de la aplicación
    if event == '-BTN SALIR-' or event == sg.WIN_CLOSED or event == 'Salir':

        break
    
    # Sección 1 Visible/Invisible
    if event == '-OPEN SEC1-':

        opened1 = not opened1
        window[ '-OPEN SEC1-' ].update( SYMBOL_DOWN if opened1 else SYMBOL_UP )
        window[ '-SEC1-' ].update( visible=opened1 )

    # Sección 2 Visible/Invisible
    if event == '-OPEN SEC2-':

        opened2 = not opened2
        window[ '-OPEN SEC2-' ].update( SYMBOL_DOWN if opened2 else SYMBOL_UP )
        window[ '-SEC2-' ].update( visible=opened2 )

    # Sección 3 Visible/Invisible
    if event == '-OPEN SEC3-':

        opened3 = not opened3
        window[ '-OPEN SEC3-' ].update( SYMBOL_DOWN if opened3 else SYMBOL_UP )
        window[ '-SEC3-' ].update( visible=opened3 )

    if event == '-BTN VOLTAJE1-':

        #window[ '-COL1-' ].Update( visible=False )
        window[ '-COL1-' ].set_size( ( 0, 0 ) )
        window[ '-COL2-' ].set_size( ( 1200, 572 ) )
        window.refresh()

window.close()

# ************************************************************************************************************************

# size(width, height)
# pad=((left, right), (top, bottom))
# if event.startswith('-XXXX-'):

# ************************************************************************************************************************
