#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from Efenergy2Globales import *

# ************************************************************************************************************************

class Efenergy2UI():

    def __init__(self):

        #self.datosVoltaje = datosVoltaje
        print()
    
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
                            logoPrincipal,
                        ],
                        #### Barra de estado
                        [
                            statusBarPrincipal,
                        ],
                    ]

        frameLogo = sg.Frame(key='-frameLogoV' + str(idConsecutivo) + '-', 
                             title='', 
                             layout=layoutLogo, 
                             title_color=eColor1, 
                             background_color=eColor2)

        return frameLogo, logoPrincipal, statusBarPrincipal

    # ************************************************************************************************************************

    def generarNavegacion(idConsecutivo):

        # Función especial que genera todo lo necesario para la barra de navegación.
        # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.
        # Se genera la misma estructura pero con id diferente.
        # Se utiliza haciendo un llamado con múltiple asignación de variables en línea.
        # Por ejemplo: frame1Navegacion = generarNavegacion(1)

        botonInicio = sg.Button(key='-botonInicioV' + str(idConsecutivo) + '-', 
                                button_text='Inicio',
                                button_color=eColores1,
                                size=(12,1),
                                pad=((10,5),(15,20)))
 
        layoutNavegacion =  [
                                [
                                    botonInicio,
                                ],
                            ]

        frameNavegacion = sg.Frame(key='-frameNavegacionV' + str(idConsecutivo) + '-',  
                                   title='  Navegación  ', 
                                   layout=layoutNavegacion, 
                                   title_color=eColor1, 
                                   background_color=eColor2)

        return frameNavegacion, botonInicio

    # ************************************************************************************************************************

    def generarNotasRapidas(frameLogo, frameNavegacion):

        # Función especial que genera todo lo necesario para gestionar las notas rápidas sobre las normas.
        # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.

        labelTituloNota = sg.Text(key='-labelTituloNota-', 
                             text='', 
                             size=(15,1), 
                             text_color=eColor1, 
                             background_color=eColor2, 
                             font=fontTituloNota, 
                             pad=((0,0),(10,10)))                           

        layoutTituloNota =  [
                                #### Título de la sección
                                [
                                    labelTituloNota,
                                ],
                             ]
        
        frameTituloNota = sg.Frame(key='-frameTituloNota-', 
                                   title='', 
                                   layout=layoutTituloNota, 
                                   title_color=eColor1, 
                                   background_color=eColor2,
                                   element_justification='center',
                                   vertical_alignment='center')

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
                                visorEditor,
                            ],
                            #### Gestión de notas rápidas
                            [
                                botonEditarNota, botonGrabarNota, botonDescartarGrabacion,
                            ],
                         ]

        frameNota = sg.Frame(key='-frameNotaRapida-', 
                             title='  Gestión de Notas Rápidas  ', 
                             layout=layoutNotas, 
                             title_color=eColor1, 
                             background_color=eColor2)

        layoutColumna =    [
                               #### Logo + Barra
                               [
                                   #frameLogoV3,
                                   frameLogo,
                               ],
                               #### Título de la nota
                               [
                                   frameTituloNota,
                               ],
                               #### Sección de notas rápidas
                               [
                                   frameNota,
                               ],
                               #### Panel de navegación
                               [
                                   #frameNavegacionV2,
                                   frameNavegacion,
                               ],
                           ]

        columna = sg.Column(key='-columna3-', 
                            layout=layoutColumna, 
                            visible=False, 
                            background_color=eColor2, 
                            size=sizeColumnas)

        return columna, visorEditor, botonEditarNota, botonGrabarNota, botonDescartarGrabacion, frameNota, frameTituloNota, labelTituloNota

    # ************************************************************************************************************************

    def generarGestionNormas(frameLogo, frameNavegacion):

        # Función especial que genera todo lo necesario para gestionar las normas en formato PDF.
        # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.

        labelTituloNorma = sg.Text(key='-labelTituloNorma-', 
                                   text='', 
                                   size=(15,1), 
                                   text_color=eColor1, 
                                   background_color=eColor2, 
                                   font=fontTituloNorma, 
                                   pad=((0,0),(10,10)))
        
        layoutTituloNorma =  [
                                #### Título de la sección
                                [
                                    labelTituloNorma,
                                ],
                             ]

        frameTituloNorma = sg.Frame(key='-frameTituloNorma-', 
                                    title='', 
                                    layout=layoutTituloNorma, 
                                    title_color=eColor1, 
                                    background_color=eColor2,
                                    element_justification='center',
                                    vertical_alignment='center')

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
                                              pad=((10,10),(10,10))),
                            ],
                            #### Gestión de normas en formato PDF
                            [
                                botonVerNorma, botonVerSeleccionado, botonActualizarNorma, botonDescartarGestion,
                            ],
                         ]

        frameNorma = sg.Frame(key='-frameGestionNorma-', 
                              title='  Gestión de la Norma en formato PDF  ', 
                              layout=layoutNormas, 
                              title_color=eColor1, 
                              background_color=eColor2)



        layoutColumna =    [
                               #### Logo + Barra
                               [
                                   frameLogo,
                               ],
                               #### Título de la norma
                               [
                                   frameTituloNorma,
                               ],
                               #### Sección de notas rápidas
                               [
                                   frameNorma,
                               ],
                               #### Panel de navegación
                               [
                                   frameNavegacion,
                               ],
                           ]

        columna = sg.Column(key='-columna4-', 
                            layout=layoutColumna, 
                            visible=False, 
                            background_color=eColor2, 
                            size=sizeColumnas)

        return columna, botonVerNorma, botonVerSeleccionado, botonActualizarNorma, botonDescartarGestion, frameNorma, frameTituloNorma, labelTituloNorma

    # ************************************************************************************************************************

    def generarAnalisisVoltaje(frameNavegacion):

        # Función especial que genera todo lo necesario para la sección de Análisis de Voltaje.
        # pySimpleGUI presenta restricciones en cuanto a la reutilización de elementos en sus Layouts.

        layoutTabFiltros =  [
                                [
                                    sg.Text(text='Filtros', size=(105,1), visible=True, border_width=0),
                                ],
                            ]

        contenidoTabTabla = sg.Text(text='Acá va la tabla', key="-prueba-")

        layoutTabTabla =    [
                                [
                                    contenidoTabTabla,
                                ]    
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
                                                    background_color=eColor2),
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
                                   frameTituloSeccionVoltaje,
                               ],
                               #### Sección de notas rápidas
                               [
                                   frameSeccionVoltaje,
                               ],
                               #### Panel de navegación
                               [
                                   frameNavegacion,
                               ],
                           ]

        columna = sg.Column(key='-columna5-', 
                             layout=layoutColumna, 
                             visible=False, 
                             background_color=eColor2, 
                             size=sizeColumnas)

        return columna, frameSeccionVoltaje, layoutTabTablaContenido, frameTituloSeccionVoltaje

    # ************************************************************************************************************************

    def generarFiltrosVoltaje():

        # SECCIÓN DE FILTROS PARA VOLTAJE

        labelComboDias = sg.Text(key='-labelComboDias-', 
                                 text='Días:', 
                                 size=(6,1), 
                                 text_color=eColor1, 
                                 background_color=eColor2, 
                                 pad=((10,0),(20,22)),
                                 tooltip='Días disponibles para análisis según plantilla')

        comboDias = sg.Combo(key='-comboDias-', 
                             values=[], 
                             size=(10,1),
                             auto_size_text=False,
                             background_color=eColor3,
                             text_color=eColor1,
                             font=fontCombos,
                             disabled=True)

        labelComboVoltaje = sg.Text(key='-labelComboVoltaje-', 
                                    text='Voltaje:', 
                                    size=(6,1), 
                                    text_color=eColor1, 
                                    background_color=eColor2, 
                                    pad=((80,0),(20,22)),
                                    tooltip='Rangos a ser analizados conforme al límite de variación establecido')

        comboVoltaje = sg.Combo(key='-comboVoltaje-', 
                                values=filtroVoltaje, 
                                size=(10,1),
                                auto_size_text=False,
                                background_color=eColor3,
                                text_color=eColor1,
                                font=fontCombos,
                                disabled=True)

        labelComboFases = sg.Text(key='-labelComboFases-', 
                                  text='Fase:', 
                                  size=(6,1), 
                                  text_color=eColor1, 
                                  background_color=eColor2, 
                                  pad=((80,0),(20,22)))

        comboFases = sg.Combo(key='-comboFases-', 
                              values=filtroFases, 
                              size=(10,1),
                              auto_size_text=False,
                              background_color=eColor3,
                              text_color=eColor1,
                              font=fontCombos,
                              disabled=True)

        label1Variacion = sg.Text(key='-label1Variacion-', 
                                  text='Límites:', 
                                  size=(6,1), 
                                  text_color=eColor1,
                                  background_color=eColor2, 
                                  pad=((100,0),(20,22)))

        label2Variacion = sg.Text(key='-label2Variacion-',
                                  text='-{0:.0f}%'.format(porcentajeLimiteInferior*100),
                                  text_color=eColor1, 
                                  background_color=eColor2, 
                                  pad=((10,5),(20,22)))

        label3Variacion = sg.Text(key='-label3Variacion-', 
                                  text='+{0:.0f}%'.format(porcentajeLimiteSuperior*100),
                                  text_color=eColor1, 
                                  background_color=eColor2, 
                                  pad=((5,20),(20,22)))

        inputVariacion = sg.Input(key='-inputVariacion-', 
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
                                    labelComboDias, comboDias,
                                    #### Voltaje MENOR, RANGO, MAYOR
                                    labelComboVoltaje, comboVoltaje,
                                    #### Fase A, B, C
                                    labelComboFases, comboFases,
                                    #### Límite variaciones redes eléctricas -10% 120 +10%
                                    label1Variacion, label2Variacion, inputVariacion, label3Variacion,
                                ],
                            ]

        frameFiltros = sg.Frame(key='-frameFiltros-', 
                                title='  Filtros  ', 
                                layout=layoutFiltros, 
                                title_color=eColor1, 
                                background_color=eColor2)

        return frameFiltros, comboDias, comboVoltaje, comboFases, inputVariacion

    # ************************************************************************************************************************

    def generarUIPrincipal(frameLogo, frameFiltros):

        # BARRA DE MENÚ PRINCIPAL

        barraMenuPrincipal = sg.Menu(key='-menuPrincipal-', 
                                     menu_definition=menuPrincipal1,
                                     text_color=eColor1,
                                     background_color=eColor2,
                                     font=fontMenuPrincipal)

        # SELECTOR DE PLANTILLAS DE ORIGEN DE DATOS

        botonCargarPlantilla = sg.Button(key='-botonCargarPlantilla-', 
                                         button_text='Cargar',
                                         button_color=eColores1,
                                         disabled=True,
                                         size=(9,1),
                                         pad=((10,5),(15,20)))

        inputSeleccionPlantilla = sg.Input(key='-inputSeleccionPlantilla-', 
                                           visible=True, 
                                           enable_events=True, 
                                           size=(122,1), 
                                           font=fontRutaTotal, 
                                           readonly=True, 
                                           pad=((10,0),(5,5)))
        
        botonPlantilla = sg.FileBrowse(key='-botonPlantilla-', 
                                       button_text='Seleccionar', 
                                       button_color=eColores1, 
                                       file_types=extensionesPlantillas, 
                                       pad=((10,10),(10,10)))
        
        labelRutaPlantilla = sg.Text(key='-labelRutaPlantilla-', 
                                     text='Ruta:', 
                                     size=(8,1), 
                                     text_color=eColor1, 
                                     background_color=eColor2, 
                                     pad=((10,0),(0,10)))

        valorRutaPlantilla = sg.Text(key='-valorRutaPlantilla-', 
                                     text='---', 
                                     size=(78,1), 
                                     text_color=eColor1, 
                                     background_color=eColor2, 
                                     font=fontRutaPartes, 
                                     pad=((10,0),(0,10)))

        labelArchivoPlantilla = sg.Text(key='-labelArchivoPlantilla-', 
                                        text='Plantilla:', 
                                        size=(8,1), 
                                        text_color=eColor1, 
                                        background_color=eColor2, 
                                        pad=((10,0),(0,10)))

        valorArchivoPlantilla = sg.Text(key='-valorArchivoPlantilla-', 
                                        text='---', 
                                        size=(78,1), 
                                        text_color=eColor1, 
                                        background_color=eColor2, 
                                        font=fontRutaPartes, 
                                        pad=((10,0),(0,10)))

        #### PROGRESSBAR PARA INDICAR DE MANERA ASÍNCRONA LA CARGA DEL ARCHIVO DE ORIGEN DE DATOS

        labelProgressBar = sg.Text(key='-labelProgressBar-', 
                                   text='Carga:', 
                                   size=(8,1), 
                                   text_color=eColor1, 
                                   background_color=eColor2, 
                                   pad=((10,0),(0,10)))   
                        
        progressBar =  sg.ProgressBar(key='-progressBar-', 
                                      max_value=100, 
                                      size=(59,15), 
                                      orientation='h',
                                      border_width=1,
                                      bar_color=eColores2,
                                      pad=((10,0),(0,10)))

        layoutOrigenDatos = [
                                [
                                    inputSeleccionPlantilla, botonPlantilla,
                                ],
                                [
                                    labelRutaPlantilla, valorRutaPlantilla,
                                ],
                                [
                                    labelArchivoPlantilla, valorArchivoPlantilla,
                                ],
                                [
                                    labelProgressBar, progressBar, botonCargarPlantilla,
                                ],
                            ]

        frameSelectorPlantilla = sg.Frame(key='-frameSelectorPlantilla-', 
                                          title='  Plantilla de origen de datos  ', 
                                          layout=layoutOrigenDatos, 
                                          title_color=eColor1,
                                          background_color=eColor2)

        layoutColumna = [
                            #### Logo + Barra
                            [
                                frameLogo,
                            ],
                            #### Selector de plantilla
                            [
                                frameSelectorPlantilla,
                            ],
                            #### Sección de filtros
                            [
                                frameFiltros,
                            ],
                        ]

        columna = sg.Column(key='-columna1-', 
                            layout=layoutColumna, 
                            visible=True, 
                            background_color=eColor2, 
                            size=sizeColumnas)

        return columna, barraMenuPrincipal, frameSelectorPlantilla, inputSeleccionPlantilla, botonPlantilla, botonCargarPlantilla

    # ************************************************************************************************************************

    def generarAcercaDe(frameLogo, frameNavegacion):

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

        labelDesarrolladores = sg.Text(key='-labelDesarrolladores-',
                                       text='Desarrolladores:',
                                       text_color=eColor1, 
                                       background_color=eColor2, 
                                       font=fontAcercaDe,
                                       pad=((10,5),(15,20)))

        acercaDeDesarrolladores = sg.Text(key='-textoDesarrolladores-',
                                          text=desarrolladores,
                                          text_color=eColor1, 
                                          background_color=eColor2, 
                                          pad=((10,5),(15,20)))

        # Información de los instructores y asesores

        labelInstructores = sg.Text(key='-labelInstructores-',
                                    text='Instructores y Asesores:',
                                    text_color=eColor1, 
                                    background_color=eColor2,
                                    font=fontAcercaDe,
                                    pad=((10,5),(15,20)))

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
                                acercaDeDescripcion, acercaDeCopyright,
                            ],
                            [   
                                labelDesarrolladores, acercaDeDesarrolladores, labelInstructores, acercaDeInstructores,
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
                                    frameLogo,
                                ],
                                #### Selector de plantilla
                                [
                                    frameAcercaDe,
                                ],
                                #### Panel de navegación
                                [
                                    frameNavegacion,
                                ],
                            ]

        columna = sg.Column(key='-columna2-', 
                            layout=layoutColumna2, 
                            visible=False, 
                            background_color=eColor2, 
                            size=sizeColumnas)

        return columna, frameAcercaDe

    # ************************************************************************************************************************



