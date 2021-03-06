﻿# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

# ************************************************************************************************************************

MENU_DISABLED_CHARACTER = '!'
MENU_KEY_SEPARATOR = '::'
SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

# Identificadores de los tipos de procesos

idPreliminar = 0
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
