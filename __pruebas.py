#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

import os.path


SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

opened1 = True
opened2 = True
opened3 = True

def collapse( layout, key ):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this seciton visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin( sg.Column( layout, key=key, background_color='#F2F2F2', pad=( 0, ( 0, 0 ) ) ) )

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
  
# VOLTAJE
seccion1 =  [ 
                [ 
                    sg.Button( button_text='Analizar voltaje', key='-BTN VOLTAJE1-', button_color=('black', '#CDCDCD') ),
                    sg.Button( button_text='Ver norma de referencia', key='-BTN VOLTAJE2-', button_color=('black', '#CDCDCD') ) 
                ] 
            ]

# POTENCIA
seccion2 =  [ 
                [ 
                    sg.Button( button_text='Analizar factor de potencia', key='-BTN POTENCIA1-', button_color=('black', '#CDCDCD') ),
                    sg.Button( button_text='Potencia reactiva', key='-BTN POTENCIA2-', button_color=('black', '#CDCDCD') ),
                    sg.Button( button_text='Ver norma de referencia', key='-BTN POTENCIA3-', button_color=('black', '#CDCDCD') ) 
                ] 
            ]

# ARMÓNICOS
seccion3 =  [ 
                [ 
                    sg.Button( button_text='Analizar armónicos de tensión', key='-BTN ARMONICOS1-', button_color=('black', '#CDCDCD') ),
                    sg.Button( button_text='Analizar armónicos de corriente', key='-BTN ARMONICOS2-', button_color=('black', '#CDCDCD') ),
                    sg.Button( button_text='Ver norma de referencia', key='-BTN ARMONICOS3-', button_color=('black', '#CDCDCD') ) 
                ] 
            ]

# GESTIÓN DE LAS NORMAS DE REFERENCIA
seccion4 =  [ 
                [ 
                    sg.Button( button_text='Norma para voltaje', key='-BTN NORMA1-', button_color=('black', '#CDCDCD') ),
                    sg.Button( button_text='Norma para potencia', key='-BTN NORMA2-', button_color=('black', '#CDCDCD') ),
                    sg.Button( button_text='Norma para armónicos', key='-BTN NORMA3-', button_color=('black', '#CDCDCD') ) 
                ] 
            ]

columna1 =  [
                #### Selector de plantilla
                [ sg.Text( text='Seleccionar plantilla de origen de datos', background_color='#F2F2F2', text_color='black' ) ],
                [ sg.Input( key='-ARCHIVO PLANTILLA-', visible=True, enable_events=True ), 
                  sg.FileBrowse( button_text='Buscar', button_color=('black', '#CDCDCD') ) ],
                #### Sección 1 ####
                [ sg.Text( text=SYMBOL_DOWN, enable_events=True, key='-OPEN SEC1-', background_color='#F2F2F2', text_color='black' ), 
                  sg.Text( text='VOLTAJE', enable_events=True, key='-OPEN SEC1-TEXT', background_color='#F2F2F2', text_color='black' ) ],
                [ collapse( seccion1, '-SEC1-' ) ],
                #### Sección 2 ####
                [ sg.Text( text=SYMBOL_DOWN, enable_events=True, key='-OPEN SEC2-', background_color='#F2F2F2', text_color='black' ),
                  sg.Text( text='POTENCIA', enable_events=True, key='-OPEN SEC2-TEXT', background_color='#F2F2F2', text_color='black' )],
                [ collapse(seccion2, '-SEC2-') ],
                #### Sección 3 ####
                [ sg.Text( text=SYMBOL_DOWN, enable_events=True, key='-OPEN SEC3-', background_color='#F2F2F2', text_color='black' ),
                  sg.Text( text='ARMÓNICOS', enable_events=True, key='-OPEN SEC3-TEXT', background_color='#F2F2F2', text_color='black' )],
                [ collapse(seccion3, '-SEC3-') ],
                #### Botones de la parte inferior ####
                [ sg.Button( button_text='Salir', key='-BTN SALIR-', button_color=('black', '#CDCDCD') ), 
                  sg.Button( button_text='Acerca de...', key='-BTN ACERCADE-', button_color=('black', '#CDCDCD') ) ] 
            ]

columna2 =  [
                #### Selector de plantilla
                [ sg.Text( 'Lorem Ipsum Lorem Ipsum' ) ]
            ]

# FULL LAYOUT
layout =    [
    [

        sg.Column( columna1, size=(600, 600), background_color='#F2F2F2', vertical_alignment='center', pad=((0, 0), 0) ),
        sg.Column( columna2, size=(600, 600), background_color='#F2F2F2' ),
    ]
]

# Cambiar al tema personalizado 
sg.theme('TemaEfenergyV2') 

window = sg.Window(
        'Efenergy v2.0',
        layout,
        use_default_focus=True,
        size=( 1200, 700 ),
        #element_padding=( 0, 0 ),
        #margins=( 10, 10 ),
        debugger_enabled=False,
        finalize=True 
    )


# Run the Event Loop
while True:
    
    event, values = window.read()
    
    # Salir de la aplicación
    if event == '-BTN SALIR-' or event == sg.WIN_CLOSED:

        break
    
    # Sección 1 Visible/Invisible
    if event.startswith( '-OPEN SEC1-' ):

        opened1 = not opened1
        window[ '-OPEN SEC1-' ].update( SYMBOL_DOWN if opened1 else SYMBOL_UP )
        window[ '-SEC1-' ].update( visible=opened1 )

    # Sección 2 Visible/Invisible
    if event.startswith( '-OPEN SEC2-' ):

        opened2 = not opened2
        window[ '-OPEN SEC2-' ].update( SYMBOL_DOWN if opened2 else SYMBOL_UP )
        window[ '-SEC2-' ].update( visible=opened2 )

    # Sección 3 Visible/Invisible
    if event.startswith( '-OPEN SEC3-' ):

        opened3 = not opened3
        window[ '-OPEN SEC3-' ].update( SYMBOL_DOWN if opened3 else SYMBOL_UP )
        window[ '-SEC3-' ].update( visible=opened3 )


window.close()