#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

# --------------------------- / -----------------------------------
# COLORES
# --------------------------- / -----------------------------------

gris1 = wx.Colour(252, 252,252) # FCFCFC	
gris2 = wx.Colour(242, 242,242) # F2F2F2
blanco = wx.Colour(255, 255,255) # FFFFFF
naranja = wx.Colour(248, 175,38) # F8AF26

# --------------------------- / -----------------------------------
# ESTILOS DEL FRAME PRINCIPAL
# --------------------------- / -----------------------------------

style1 = (wx.DEFAULT_FRAME_STYLE)
style2 = (wx.CLOSE_BOX|wx.CAPTION)
style3 = (wx.DEFAULT_FRAME_STYLE & ~ (wx.CAPTION))

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

# --------------------------- / -----------------------------------
# MISCELÁNEAS
# --------------------------- / -----------------------------------

logotipo1 = "imagenes/logo_2020.png"
logotipo2 = "imagenes/logo_texto_2020.png"

ruta1 = "archivo\informacion.txt"

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
btn6 = "Seleccionar plantilla de MS-Excel (xls, xlsx)"

icono1 = "imagenes/icono_pdf.png"
icono2 = "imagenes/icono_editar.png"
icono3 = "imagenes/icono_xls.png"

texto_opcion1 = "Salir\tCTRL+Q"
tip_opcion1 = "Salir de Efenergy"

texto_opcion2 = "Acerca de...\tF1"
tip_opcion2 = "Acerca de Efenergy"

texto_opcion3 = "Cerrar ventana"
texto_opcion4 = "Archivo"
texto_opcion5 = "Ayuda"
texto_opcion6 = "Opciones"

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

# --------------------------- / -----------------------------------
