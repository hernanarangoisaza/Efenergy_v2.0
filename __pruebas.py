# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

import os.path

# ************************************************************************************************************************

def long_function_thread1(window, plantilla):
    global archivo_voltaje
    archivo_voltaje = pandas.ExcelFile(plantilla)
    window.write_event_value('-THREAD DONE-','')

def long_function_thread2(window):
    limite = 100
    i = 0
    window['-PROGRESSBAR-'].update_bar(0,0)
    while (t1.is_alive()):
        window['-PROGRESSBAR-'].update_bar(i,limite)
        i = i + 1
        if (i==(limite-1)):
            i = 0
            window['-PROGRESSBAR-'].update_bar(0,0)
    window['-PROGRESSBAR-'].update_bar(limite,limite)

def long_function1(plantilla):
    global t1
    t1 = threading.Thread(target=long_function_thread1, args=(window,plantilla), daemon=True)
    t1.name = 't1'
    t1.start()

def long_function2():
    global t2 
    t2 = threading.Thread(target=long_function_thread2, args=(window,), daemon=True)
    t2.name = 't2'
    t2.start()

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
eColor4 = '#FFC000'
eColores1 = ('black','#CDCDCD')

rutaPlantilla = None
archivoPlantilla = None

archivo_voltaje = None

df_xlsx = None
t1 = None
t2 = None

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

comboDias = sg.Combo(key='-COMBO DIAS', 
                     values=[], 
                     size=(10,1),
                     auto_size_text=False,
                     background_color=eColor3,
                     text_color=eColor1,
                     disabled=True)

comboVoltaje = sg.Combo(key='-COMBO VOLTAJE', 
                        values=filtroVoltaje, 
                        size=(10,1),
                        auto_size_text=False,
                        background_color=eColor3,
                        text_color=eColor1,
                        disabled=True)

comboFases = sg.Combo(key='-COMBO FASES', 
                      values=filtroFases, 
                      size=(10,1),
                      auto_size_text=False,
                      background_color=eColor3,
                      text_color=eColor1,
                      disabled=True)

# FRAME FILTROS

inputVariacion = sg.Input(key='-VARIACION-', 
                          default_text='120',
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
                            sg.Text(key='-LCOMBO DIAS-', 
                                    text='Días:', 
                                    size=(6,1), 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((10,0),(20,22)),
                                    tooltip='Días disponibles para análisis según plantilla'),
                            comboDias,
                            #### Voltaje MENOR, RANGO, MAYOR
                            sg.Text(key='-LCOMBO VOLTAJE-', 
                                    text='Voltaje:', 
                                    size=(6,1), 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((80,0),(20,22)),
                                    tooltip='Rangos a ser analizados conforme al límite de variación establecido'),
                            comboVoltaje,
                            #### Fase A, B, C
                            sg.Text(key='-LCOMBO FASES-', 
                                    text='Fase:', 
                                    size=(6,1), 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((80,0),(20,22))),
                            comboFases,
                            #### Límite variaciones redes eléctricas -10% 120 +10%
                            sg.Text(key='-L1 VARIACION-', 
                                    text='Límites:', 
                                    size=(6,1), 
                                    text_color=eColor1,
                                    background_color=eColor2, 
                                    pad=((100,0),(20,22))),
                            sg.Text(key='-L2 VARIACION-', 
                                    text='-10%', 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((10,5),(20,22))),
                            inputVariacion,
                            sg.Text(key='-L3 VARIACION-', 
                                    text='+10%', 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((5,20),(20,22))),
                        ],
                        [
                            #### ProgressBar para indicar de manera asíncrona la carga de la plantilla
                            sg.Text(key='-LABEL PROGRESSBAR-', 
                                    text='Progreso de carga de la planilla:', 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((10,20),(0,22))),                        
                            sg.ProgressBar(key='-PROGRESSBAR-', 
                                           max_value=100, 
                                           size=(65,20), 
                                           orientation='h',
                                           border_width=1,
                                           bar_color=None,
                                           pad=((0,20),(0,22)))
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
frameFiltros.expand(expand_x=True)
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
        long_function1(rutaPlantillaVoltaje)
        long_function2()
        #archivo_voltaje = pandas.ExcelFile(rutaPlantillaVoltaje)
      
    # Mensaje enviado por los hilos al momento de haber finalizado las acciones que toman más tiempo
    if event == '-THREAD DONE-':
        comboDias.Update(disabled=False)
        comboDias.Update(values=archivo_voltaje.sheet_names)
        comboDias.Update(readonly=True)
        comboFases.Update(disabled=False)
        comboFases.Update(readonly=True)
        comboVoltaje.Update(disabled=False)
        comboVoltaje.Update(readonly=True)

    # Rango de variación
    if event.endswith('-VARIACION-'):
        limiteInferior = int(window['-VARIACION-'].get()) * 0.9
        limiteSuperior = int(window['-VARIACION-'].get()) * 1.1
        nuevoTooltip = '  El rango establecido para análisis es [ {0:.2f} - {1:.2f} ]  '.format(limiteInferior,limiteSuperior)
        inputVariacion.set_tooltip(nuevoTooltip)

    # Actualizar cambios en componentes de la GUI
    window.refresh()     
        

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
