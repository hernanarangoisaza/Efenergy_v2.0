# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import threading
import pandas

import os.path
import ctypes

#from AnalisisDatosVoltaje import AnalisisDatosVoltaje
#from AnalisisDatosPotencia import AnalisisDatosPotencia
#from AnalisisDatosPotenciaReactiva import AnalisisDatosPotenciaReactiva
#from AnalisisDatosArmonicos import AnalisisDatosArmonicos
#from AnalisisDatosArmonicosCorriente import AnalisisDatosArmonicosCorriente
#from EditarInformacion import EditarInformacion

# ************************************************************************************************************************

def cargarPlantilla(window, plantilla, identificador):

    if (identificador == idVoltaje):
        global archivoVoltaje
        archivoVoltaje = pandas.ExcelFile(plantilla)

    elif (identificador == idPotencia):
        global archivoPotencia
        archivoPotencia = pandas.ExcelFile(plantilla)

    elif (identificador == idArmonicos):
        global archivoArmonicos
        archivoArmonicos = pandas.ExcelFile(plantilla)

    window.write_event_value('-ThreadDone-','')

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

def hiloCargarPlantilla(plantilla, identificador):

    global t1
    t1 = threading.Thread(target=cargarPlantilla, args=(window,plantilla,identificador), daemon=True)
    t1.name = 't1'
    t1.start()

def hiloIndicadorCarga():

    global t2 
    t2 = threading.Thread(target=indicadorCarga, args=(window,), daemon=True)
    t2.name = 't2'
    t2.start()

# ************************************************************************************************************************

def leerArchivo(file):

	archivo = open(file, "r")
	contenido = archivo.read()
	archivo.close()
	return contenido

def escribirArchivo(file, contenido):

	archivo = open(file, "w")
	for texto in contenido:
		archivo.write(texto)
	archivo.close()

# ************************************************************************************************************************

MENU_DISABLED_CHARACTER = '!'
MENU_KEY_SEPARATOR = '::'
SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

# Identificadores de los tipos de procesos

idVoltaje = 1
idPotencia = 2
idArmonicos = 3

# Valores para límites de variación del Voltaje

valorVariacion = 120
porcentajeLimiteInferior = 0.1 # 10%
porcentajeLimiteSuperior = 0.1 # 10%

# Contenidos para filtros presentados con el componente Combo

filtroVoltaje = ['MENOR','RANGO','MAYOR']
filtroFases = ['A','B','C']

sizeFrmPrincipal = (1030,600) # Tamaño de la ventana principal
sizeColumnas = (1000,580) # Tamaño de las columnas que simulan ventanas ocultas
sizeSelectorPlantilla = (1000,580) # Tamaño del Input para mostrar la ruta completa de la plantilla

fontRutaPartes = ('Consolas',10)+('bold',)
fontRutaTotal = ('Consolas',10)
fontMenuPrincipal = ('Helvetica',11)
fontCombos = ('Helvetica',11)
fontAcercaDe = ('Helvetica',10)+('bold',)

rutaLogoPrincipal = 'imagenes\\logo_texto_2020.png'
rutaIconoPrincipal = 'imagenes\\logo_2020.ico'

extensionesPlantillas = (('Excel','*.xls*'),)
extensionPdf = (('Archivo PDF','*.pdf'),)

barraEstado = 'SENA - CDITI - TEINNOVA - Semillero de Energías. Todos los derechos reservados. (C) 2020'

eColor1 = '#000000' # Negro
eColor2 = '#F2F2F2' # Gris fondo ventana
eColor3 = '#FFFFFF' # Blanco
eColor4 = '#F8AF26' # Naranja
eColor5 = '#CDCDCD' # Gris botones
eColores1 = (eColor1,eColor5) 
eColores2 = (eColor4,eColor2) 

# Ubicaciones y nombre de archivo a procesar como plantilla

rutaPlantilla = None
archivoPlantilla = None

# Variables contenedoras del procesamiento de la plantilla con la librería Panda 

archivoVoltaje = None
archivoPotencia = None
archivoArmonicos = None

# Variables globales para control de ejecución de Hilos (Threads)

t1 = None # Hilo para carga y procesamiento con la libreria Panda
t2 = None # Hilo para representación gráfica del progreso de carga de plantillas

clave = '1234' # Clave para edición de la norma

rutaInformacionVoltaje = 'archivo\\InformaciónVoltaje.txt'
rutaInformacionPotencia = 'archivo\\InformaciónPotencia.txt'
rutaInformacionArmonicos = 'archivo\\InformaciónArmónicos.txt'

rutaPdfVoltaje = 'archivo\\NormaVoltaje.pdf'
rutaPdfPotencia = 'archivo\\NormaPotencia.pdf'
rutaPdfArmonicos = 'archivo\\NormaArmónicos.pdf'

# Carga los textos descriptivos para las normas

informacionVoltaje = leerArchivo(rutaInformacionVoltaje)
informacionPotencia = leerArchivo(rutaInformacionPotencia)
informacionArmonicos = leerArchivo(rutaInformacionArmonicos)

# Información para Acerca De...

descripcion = 'Efenergy es un programa diseñado para funcionar bajo Windows el cual usted podrá utilizar en el análisis de la información y presentación oportuna de informes para el control de la eficiencia energética.\n\nDiversos estándares sobre \"Calidad de Energía Eléctrica\" convergen en la necesidad de realizar mediciones con la ayuda de herramientas TRUE RMS y analizar los  datos  recolectados mediante herramientas digitales con finalidad específica como Efenergy.'
instructores = 'Semillero Energías\nViviana Ramírez Ramírez\nAndrés Tafur Piedrahita\nYuely Adriana Arce Arias'
desarrolladores = 'Hernán Arango Isaza\nWendy Vanessa Mejía Agudelo\nDiego Alexander Sepúlveda García'
copyright = '(C) 2020\nSENA - CDITI\nDosquebradas (Risaralda)'

# ************************************************************************************************************************

def generarNavegacion(idConsecutivo):

    # Función especial que genera todo lo necesario para la barra de navegación.
    # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.
    # Se genera la misma estructura pero con id diferente.
    # Se utiliza haciendo un llamado con múltiple asignación de variables en línea.
    # Por ejemplo: layout1Navegacion, frame1Navegacion = generarNavegacion(1)

    layoutNavegacion =  [
                            [
                                sg.Button(key='-botonInicioV' + str(idConsecutivo) + '-', 
                                          button_text='Inicio',
                                          button_color=eColores1,
                                          size=(12,1),
                                          pad=((10,5),(15,20)))
                            ],
                        ]

    frameNavegacion = sg.Frame(key='-frameNavegacionV' + str(idConsecutivo) + '-',  
                               title='  Navegación  ', 
                               layout=layoutNavegacion, 
                               title_color=eColor1, 
                               background_color=eColor2)

    return layoutNavegacion, frameNavegacion

# ************************************************************************************************************************

def generarLogo(idConsecutivo):

    # Función especial que genera todo lo necesario para presentar el logo en las páginas que lo requieran.
    # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.
    # Se genera la misma estructura pero con id diferente.
    # Se utiliza haciendo un llamado con múltiple asignación de variables en línea.
    # Por ejemplo: logo1Principal, statusBar1Principal, layout1Logo, frame1Logo = generarLogo(1)

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

    frameLogo = sg.Frame(key='-frameLogoV' + str(idConsecutivo) + '-', 
                          title='', 
                          layout=layoutLogo, 
                          title_color=eColor1, 
                          background_color=eColor2)


    return logoPrincipal, statusBarPrincipal, layoutLogo, frameLogo

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
                            [ 'Ver norma sobre Voltaje::-opcN1-', 'Ver norma sobre Potencia::-opcN2-', 'Ver norma sobre Armónicos::-opcN3-', '---', 'Gestión de Normas',
                                [ 'Voltaje::-opcN4-', 'Potencia::-opcN5-', 'Armónicos::-opcN6-' ]
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
                            [ 'Ver norma sobre Voltaje::-opcN1-', 'Ver norma sobre Potencia::-opcN2-', 'Ver norma sobre Armónicos::-opcN3-', '---', 'Gestión de Normas',
                                [ 'Voltaje::-opcN4-', 'Potencia::-opcN5-', 'Armónicos::-opcN6-' ]
                            ],
                        ],
                    ]

# GENERACIÓN DINÁMICA DE FRAMES PARA EL LOGO. DEBE CREARSE UNA POR CADA SIMULACIÓN DE PANTALLA MEDIANTE COLUMNAS.

logo1Principal, statusBar1Principal, layout1Logo, frame1Logo = generarLogo(1)
logo2Principal, statusBar2Principal, layout2Logo, frame2Logo = generarLogo(2)

# SELECTOR DE PLANTILLAS DE ORIGEN DE DATOS

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
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),
                        sg.Text(key='-valorRutaPlantilla-', 
                                text='---', 
                                size=(80,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                font=fontRutaPartes, 
                                pad=((10,0),(0,10)))
                    ],
                    [
                        sg.Text(key='-labelArchivoPlantilla-', 
                                text='Archivo:', 
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),
                        sg.Text(key='-valorArchivoPlantilla-', 
                                text='---', 
                                size=(80,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                font=fontRutaPartes, 
                                pad=((10,0),(0,10)))
                    ],
                    [
                        #### ProgressBar para indicar de manera asíncrona la carga de la plantilla
                        sg.Text(key='-labelProgressBar-', 
                                text='Carga:', 
                                size=(6,1), 
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,0),(0,10))),                        
                        sg.ProgressBar(key='-progressBar-', 
                                        max_value=100, 
                                        size=(71,20), 
                                        orientation='h',
                                        border_width=1,
                                        bar_color=eColores2,
                                        pad=((10,0),(0,10)))
                    ],
                ]

barraMenuPrincipal = sg.Menu(key='-menuPrincipal-', 
                             menu_definition=menuPrincipal1,
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

inputVariacion.Update = 120

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

acercaDeDesarrolladores = sg.Text(key='-textoDesarrolladores-',
                                  text=desarrolladores,
                                  text_color=eColor1, 
                                  background_color=eColor2, 
                                  pad=((10,5),(15,20)))

acercaDeInstructores =  sg.Text(key='-textoInstructores-',
                                text=instructores,
                                text_color=eColor1, 
                                background_color=eColor2, 
                                pad=((10,5),(15,20)))

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

# GENERACIÓN DINÁMICA DE FRAMES PARA NAVEGACIÓN. DEBE CREARSE UNA POR CADA SIMULACIÓN DE PANTALLA MEDIANTE COLUMNAS.

layout1Navegacion, frame1Navegacion = generarNavegacion(1)

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
                    columna1, 
                    columna2,
                ],
            ]

# ************************************************************************************************************************

# Cambiar al tema personalizado

sg.theme('Default1')
sg.ChangeLookAndFeel('SystemDefault')

# ************************************************************************************************************************

window = sg.Window('Efenergy v2.0',
                   layout,
                   use_default_focus=True,
                   size=sizeFrmPrincipal,
                   debugger_enabled=False,
                   finalize=True,
                   font=('Helvetica',11),
                   icon=rutaIconoPrincipal)

# ************************************************************************************************************************

# Habilitar barra de menú con opciones deshabilitadas.

barraMenuPrincipal.Update(menuPrincipal2)

# Extender tamaño de algunos Frames para que ocupen el ancho del diseño.

frameFiltros.expand(expand_x=True)
frameAcercaDe.expand(expand_x=True)
frame1Navegacion.expand(expand_x=True)

window.refresh()

# Mejorar la nitidez y resolución de la aplicación. Se ve pequeño en monitores de alta resolución como 4K.

# ctypes.windll.shcore.SetProcessDpiAwareness(2)

# ************************************************************************************************************************

# Run the Event Loop.

while True:

    event, values = window.read()

    print(event)

    # Salir de la aplicación

    if event == sg.WIN_CLOSED or event == 'Salir':

        break

    # Salir de la aplicación

    if event.endswith('-opcSalir-'):

        break

    # Seleccionar plantilla de origen de datos
    
    if event == '-seleccionPlantilla-':

        rutaPlantilla = values['-seleccionPlantilla-']
        archivoPlantilla = rutaPlantilla.split('/')[-1]
        window['-valorRutaPlantilla-'].Update(rutaPlantilla.rpartition('/')[0])
        window['-valorArchivoPlantilla-'].Update(archivoPlantilla)
        barraMenuPrincipal.Update(menuPrincipal1)

    # Analizar Voltaje

    if event.endswith('-opcV1-'):

        idProcesoActual = idVoltaje
        rutaPlantillaVoltaje = values['-seleccionPlantilla-']
        hiloCargarPlantilla(rutaPlantillaVoltaje, idVoltaje)
        hiloIndicadorCarga()
      
    # Mensaje recibido desde los hilos al momento de haber finalizado las acciones que toman más tiempo

    if event == '-ThreadDone-':

        if (idProcesoActual == idVoltaje):
            comboDias.Update(values=archivoVoltaje.sheet_names)

        elif (idProcesoActual == idPotencia):
            comboDias.Update(values=archivoPotencia.sheet_names)

        elif (idProcesoActual == idArmonicos):
            comboDias.Update(values=archivoArmonicos.sheet_names)
        
        comboDias.Update(disabled=False)
        comboDias.Update(readonly=True)
        comboFases.Update(disabled=False)
        comboFases.Update(readonly=True)
        comboVoltaje.Update(disabled=False)
        comboVoltaje.Update(readonly=True)

    # Rango de variación

    if event == '-variacion-': 
    
        try:
            intVariacion = float(window['-variacion-'].get())
            limiteInferior = intVariacion * (1 - porcentajeLimiteInferior)
            limiteSuperior = intVariacion * (1 + porcentajeLimiteSuperior)
            nuevoTooltip = '  El rango establecido para análisis es [ {0:.2f} - {1:.2f} ]  '.format(limiteInferior,limiteSuperior)
            inputVariacion.set_tooltip(nuevoTooltip)
        except ValueError:
            window['-variacion-'].update(''.join([i for i in window['-variacion-'].get() if i.isdigit()]))
            #print('Error controlado por Efenergy v2.0. El valor del Input no corresponde a un número.')

    # Ventana Acerca de

    if event.endswith('-opcAcercaDe-'):

        columna1.Update(visible=False)
        columna2.Update(visible=True)

    # Boton INICIO desde la ventana Acerca de

    if event == '-botonInicioV1-': 

        columna1.Update(visible=True)
        columna2.Update(visible=False)


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
# window['-logoPrincipal-'].hide_row()
# window['-logoPrincipal-'].unhide_row()
# bkSizeLogo = logoPrincipal.get_size()
# logoPrincipal.set_size((1,None))
# window.refresh()
# window['-COLUMNA 2'].Update(visible=False)
# globals()["layoutLogo" + str(idConsecutivo)] =

# ************************************************************************************************************************
