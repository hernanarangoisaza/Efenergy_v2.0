#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

# --------------------------- / -----------------------------------
# COLORES
# --------------------------- / -----------------------------------

gris1 = wx.Colour(252, 252, 252)    # FCFCFC	
gris2 = wx.Colour(242, 242, 242)    # F2F2F2
blanco = wx.Colour(255, 255, 255)   # FFFFFF
negro = wx.Colour(0, 0, 0)          # 000000
naranja = wx.Colour(248, 175, 38)   # F8AF26
verde = wx.Colour(93, 165, 92)      #5DA55C
azul = wx.Colour(66, 142, 174)      #428EAE
lila = wx.Colour(167, 94, 143)      #A75E8F
morado = wx.Colour(113, 87, 154)    #71579A

# --------------------------- / -----------------------------------
# ESTILOS DEL FRAME PRINCIPAL
# --------------------------- / -----------------------------------

style1 = (wx.DEFAULT_FRAME_STYLE)
style2 = (wx.CLOSE_BOX|wx.CAPTION)
style3 = (wx.DEFAULT_FRAME_STYLE & ~ (wx.CAPTION))
style4 = (wx.DEFAULT_FRAME_STYLE&~(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX))

# --------------------------- / -----------------------------------
# TAMAÑOS
# --------------------------- / -----------------------------------

size1 = wx.Size(1000, 730) # Ventana principal
size2 = wx.Size(1000, 130) # Header Efenergy + Logo
size3 = wx.Size(1000, 500) # Panel general de pestañas
size4 = wx.Size(970, 500) # Zona pestañas individuales
size5 = wx.Size(880, 200) # Zona para texto explicativo de la norma
size6 = wx.Size(300, 30) # Botón superior para archivos
size7 = wx.Size(300, 30) # Botones inferiores para acciones
size8 = wx.Size(700, 150) # Zona interna con márgenes para explicación de la norma
size9 = wx.Size(878, 360) # Ventana para edición de información de la norma
size10 = wx.Size(878, 60) # Header ventana para edición de información de la norma
size11 = wx.Size(130, 30) # 
size12 = wx.Size(600, 200) #

# --------------------------- / -----------------------------------
# MISCELÁNEAS
# --------------------------- / -----------------------------------

clave = "1234" # Clave de edición de la norma

logotipo1 = "imagenes/logo_2020.png"
logotipo2 = "imagenes/logo_texto_2020.png"

ruta1 = "archivo\informacion.txt"
ruta_pdf_voltaje = "archivo/NormaVoltaje.pdf"
ruta_pdf_potencia = "archivo/NormaPotencia.pdf"
ruta_pdf_armonicos = "archivo/NormaArmónico.pdf"

titulo_ventana = "Efenergy v2.0"
texto_header = "Efenergy"

tab1 = "Voltaje"
tab2 = "Potencia"
tab3 = "Armónicos"

btn1 = "Analizar voltaje"
btn2 = "Analizar factor de potencia"
btn3 = "Analizar potencia reactiva"
btn4 = "Analizar armónicos de tensión"
btn5 = "Analizar armónicos de corriente"
btn6 = "Seleccionar plantilla de origen de datos"

icono1 = "imagenes/icono_pdf.ico"
icono2 = "imagenes/icono_editar.ico"
icono3 = "imagenes/icono_xls.png"
icono_aceptar = "imagenes/icono_aceptar.png"
icono_cancelar = "imagenes/icono_cancelar.png"

texto_opcion1 = "Salir\tCTRL+Q"
tip_opcion1 = "Salir de Efenergy"

texto_opcion2 = "Acerca de...\tF1"
tip_opcion2 = "Acerca de Efenergy"

texto_opcion3 = "Cerrar ventana"
texto_opcion4 = "Archivo"
texto_opcion5 = "Ayuda"
texto_opcion6 = "Opciones"

texto_pdf = "Ver pdf de la norma"
texto_editar = "Editar texto de la norma"

descripcion = """
Efenergy es un programa diseñado para funcionar bajo Windows el 
cual usted podrá utilizar en el análisis de la información y 
presentación oportuna de informes para el control de la eficiencia 
energética. 

Diversos estándares sobre "Calidad de Energía Eléctrica" convergen 
en la necesidad de realizar mediciones con la ayuda de herramientas 
TRUE RMS y analizar los  datos  recolectados mediante  herramientas 
digitales con finalidad específica como Efenergy."""

integrantes_semillero = ["\n\nSemillero Energías - TEINNOVA", "\nViviana Ramírez Ramírez", "\nAndrés Tafur Piedrahita", "\nYuely Adriana Arce Arias"]
copy_right = "(C) 2020\nCentro de Diseño e Innovación Tecnológica Industrial\nSENA - CDITI\nDosquebradas (Risaralda)"
desarrolladores = "\n\nHernán Arango Isaza\nWendy Vanessa Mejía Agudelo\nDiego Alexander Sepúlveda García"
nombre_variable = ["Voltaje","Potencia","Armónicos"]
texto_edicion = "Editar información de %s"
texto_cambiar_pdf = "Cambiar archivo PDF de la norma:"
texto_seleccionar_norma = "Seleccionar archivo"
texto_cargar = "Cargar"
texto_guardar = "Desea guardar la información?"
texto_modificado_ok = "El texto de información para la norma se modificó correctamente"
texto_modificado_error = "Ha ocurrido un error al modificar la información"
texto_seleccionar_pdf = "Seleccionar nuevo PDF"
titulo_norma = "Norma"
texto_seleccionar_pdf_error = "Error al seleccionar el archivo PDF"
texto_cargar_pdf_ok = "Se cargó correctamente el archivo PDF para la norma"
texto_cargar_pdf_error = "Error al cargar el archivo PDF. \nVerifique que el archivo seleccionado sea correcto"
texto_cancelar_operacion = "Desea cancelar esta operación?"
titulo_informacion = "Información"
titulo_error = "Error"
titulo_confirmacion = "Confirmación"

barra_estado_fields = ["   SENA - CDITI - TEINNOVA - Semillero de Energías. Todos los derechos reservados. (C) 2020"]

texto_clave_incorrecta = "Clave incorrecta. No puede editar la información"
texto_clave_error = "Clave incorrecta. Intente de nuevo"
texto_editar_informacion_voltaje = "Editar Información de Voltaje"
texto_editar_informacion_potencia = "Editar Información de Potencia"
texto_editar_informacion_armonicos = "Editar Información de Armónicos"
texto_digitar_clave = "Digite su clave"
titulo_editar_clave = "Clave para edición"

url_voltaje_pdf = "archivo\\NormaVoltaje.pdf"
url_potencia_pdf = "archivo\\NormaPotencia.pdf"
url_armonicos_pdf = "archivo\\NormaArmónico.pdf"

extension_xls = ["*.xlsx","*.xls"]
extension_pdf = ["*.pdf"]
texto_abrir_xls = "Abrir archivo de Excel"
titulo_abrir_xls = "Seleccionar plantilla"

seleccion_archivo_xls_error = "No se seleccionó el archivo"

texto_analizar_voltaje = "Analizar Voltaje"
texto_seleccionar_archivo_error = "Error al seleccionar archivo"
texto_analizar_factor_potencia = "Analizar Factor de Potencia"
texto_analizar_potencia_reactiva = "Analizar Potencia reactiva"
texto_analizar_armonicos_tension = "Analisis armónicos de tensión"
texto_analizar_armonicos_corriente = "Analizar armónicos de corriente"

texto_cargando_archivo = "Cargando Archivo..."

# --------------------------- / -----------------------------------
