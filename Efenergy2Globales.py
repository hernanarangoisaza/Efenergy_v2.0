# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Efenergy2Funciones
from pathlib import Path

# ************************************************************************************************************************

global window, event, values

global layoutPrincipal

global columna1, barraMenuPrincipal, frameSelectorPlantilla, inputSeleccionPlantilla, sbotonCargarPlantilla
global columna2, frameAcercaDe
global columna3, visorEditor, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, frameNota, frameTituloNota, labelTituloNota
global columna4, botonVerNorma, botonVerSeleccionado, botonActualizarNorma, botonDescartarGestion, frameNorma, frameTituloNorma, labelTituloNorma
global columna5, frameSeccionVoltaje, frameTituloSeccionVoltaje

global frameFiltrosVoltaje, comboDias, comboVoltaje, comboFases

global frameLogoV1, logoPrincipalV1, statusBarPrincipalV1
global frameLogoV2, logoPrincipalV2, statusBarPrincipalV2
global frameLogoV3, logoPrincipalV3, statusBarPrincipalV3
global frameLogoV4, logoPrincipalV4, statusBarPrincipalV4
global frameLogoV5, logoPrincipalV5, statusBarPrincipalV5

global frameNavegacionV1, botonInicioV1
global frameNavegacionV2, botonInicioV2
global frameNavegacionV3, botonInicioV3
global frameNavegacionV4, botonInicioV4

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
ecolor7 = '#4B7CBA' # Azul 1
ecolor8 = '#428EAE' # Azul 2
ecolor9 = '#0096D6' # Azul 3
eColores1 = (eColor1,eColor5) 
eColores2 = (eColor4,eColor2) 
eColores3 = (eColor3,ecolor7) 

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
fontCantidadRegistros = ('Helvetica',12)+('bold',)

rutaLogoPrincipal = 'imagenes\\logo_texto_2020.png'
rutaIconoPrincipal = 'imagenes\\logo_2020.ico'

extensionesPlantillas = (('Excel','*.xls*'),)
extensionPdf = (('Archivo PDF','*.pdf'),)

barraEstado = 'SENA - CDITI - TEINNOVA - Semillero de Energías. Todos los derechos reservados. (C) 2020'

# Ubicaciones y nombre de archivo a procesar como plantilla

rutaPlantilla = None
archivoPlantilla = None
rutaPlantillaPreliminar = None

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

# Carga los textos descriptivos para las notas

errorPersonalizadoNotasLeer = 'Ocurrió un problema al leer el archivo de texto de Notas Rápidas.'

informacionVoltaje = Efenergy2Funciones.leerArchivo(rutaInformacionVoltaje, errorPersonalizadoNotasLeer)
informacionPotencia = Efenergy2Funciones.leerArchivo(rutaInformacionPotencia, errorPersonalizadoNotasLeer)
informacionArmonicos = Efenergy2Funciones.leerArchivo(rutaInformacionArmonicos, errorPersonalizadoNotasLeer)

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
