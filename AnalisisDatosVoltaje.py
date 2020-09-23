#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import wx.grid
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy      
from menu import Menu 
import wx.lib.agw.aquabutton as AB    
from GraficaPotencia import GraficaPotencia
from matplotlib.widgets import CheckButtons
from NuevoArchivoVoltajeReglas import NuevoArchivoVoltajeReglas

class AnalisisDatosVoltaje(wx.Frame):

	def __init__(self, id, title, archivo,):
		self.archivo_excel = archivo

		self.txt_fase_a = []
		self.txt_fase_b = []
		self.txt_fase_c = []

		self.frame = wx.Frame.__init__(self, None, id, title, size = (1200,730), style = wx.DEFAULT_FRAME_STYLE 
			& ~(wx.MAXIMIZE_BOX)) 

		self.SetIcon(wx.Icon("imagenes/logo.png"))
		self.panel = wx.Panel(self,-1,size=(1200,700),pos=(0,120))
		
		self.Elementos()
		self.menu()
		self.footer()

	def menu(self):
		self.panel_menu = Menu(3,self.archivo_excel)
		self.panel_menu.menugeneral(self)
		menugrafica = self.panel_menu.opt_grafica_voltaje()

		menuItem2 = wx.MenuItem(menugrafica, wx.ID_ANY, u"Ver Grafica1\tCTRL+G", u"Ver representación grafica de los datos en porcentaje (%) por hora", wx.ITEM_NORMAL )
		menuItem2.SetBitmap(wx.Bitmap(u"imagenes/grafica1.png", wx.BITMAP_TYPE_ANY ))
		menugrafica.Append(menuItem2)
		self.Bind(wx.EVT_MENU, self.graficaVolageVsTiempo, id = menuItem2.GetId() )

	def salir(self, event):
		self.Destroy()

	def Elementos(self):
		header= wx.Panel(self,-1,size=(1200,120),pos=(0,0))
		header.SetBackgroundColour('#6E7B99')

		titulo = wx.StaticText(header, wx.ID_ANY, "Efenergy", style=wx.ALIGN_CENTER, pos=(150,25))
		font = wx.Font(40, wx.ROMAN, wx.ITALIC, wx.NORMAL)
		titulo.SetFont(font)

		logotipo = 'imagenes/logotipo.JPG'
		bmp1 = wx.Image(logotipo, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(header, -1, bmp1, (30,10))

		txt_seleccion_dia = wx.StaticText(self.panel, -1, "Día: ", pos=(520,30))
		txt_seleccion_estado_voltaje = wx.StaticText(self.panel, wx.ID_ANY,  "Voltaje: ", pos=(520,65))
		txt_seleccion_fase = wx.StaticText(self.panel, wx.ID_ANY,  "Fase: ", pos=(520,95))
		
		txt_repote = wx.StaticText(self.panel, -1, "Reporte ", pos=(628,220))
		txt_grafica = wx.StaticText(self.panel, -1, "Grafica ", pos=(550,220))
		#-------------------------------------------------------------------------------------------------	

		dias = self.archivo_excel.sheet_names
		self.choice = wx.Choice(self.panel, choices = dias, pos=(620, 30))
		self.choice.SetSelection(0)	
		
		reglas = ["RANGO", "MAYOR", "MENOR"]
		self.reglas_voltaje = wx.Choice(self.panel, choices = reglas, pos=(620, 65),size=(100,26))
		self.reglas_voltaje.SetSelection(0)	

		lista_fase = ["A", "B", "C"]
		self.Fase = wx.Choice(self.panel, choices = lista_fase, pos=(620, 95),size=(100,26))
		self.Fase.SetSelection(0)	
		
		# -------------------------------------------------------------------------------------------------	
		 
		bmp1 = wx.Image('imagenes/calendario.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		icon_seleccionar_dia = wx.StaticBitmap(self.panel, -1, bmp1, (585, 30))

		bmp1 = wx.Image('imagenes/voltaje.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		icon_estado_voltaje = wx.StaticBitmap(self.panel, -1, bmp1, (585, 65))

		bmp1 = wx.Image('imagenes/fase.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		icon_fase = wx.StaticBitmap(self.panel, -1, bmp1, (585, 95))
		# -------------------------------------------------------------------------------------------------	

		btn_listar = wx.Button(self.panel, 7, u"Listar", size=(200,30), pos=(520,130))
		btn_listar.Bind(wx.EVT_BUTTON, self.cargarDatos)

		ico_grafica = wx.Bitmap("imagenes/grafica.png", wx.BITMAP_TYPE_ANY)
		button_grafica_faseA = AB.AquaButton(self.panel, 1, bitmap=ico_grafica, size=(38,35),pos=(560,180))
		button_grafica_faseA.SetForegroundColour("red")
		button_grafica_faseA.Bind(wx.EVT_BUTTON, self.graficaVolageVsTiempo )

		ico_repote = wx.Bitmap("imagenes/reporte6.png", wx.BITMAP_TYPE_ANY)
		button_reportar= AB.AquaButton(self.panel, 1, bitmap=ico_repote, size=(38,35),pos=(630,180))
		button_reportar.SetForegroundColour("black")
		button_reportar.Bind(wx.EVT_BUTTON, self.reporteAnalisis )


		self.Layout()	

		#----------------------------------------------------------------------------------------------------
		
		self.list_ctrl = wx.ListCtrl(self.panel, pos=(25, 25), size=(450,450),
							style=wx.LC_REPORT
							|wx.BORDER_SUNKEN|wx.LC_HRULES|wx.LC_VRULES
							)
		self.list_ctrl.InsertColumn(0, 'Fecha',width=150)
		self.list_ctrl.InsertColumn(1, 'Hora',width=150)
		self.list_ctrl.InsertColumn(2, 'Voltaje',width=150)	
	
		#----------------------------------------------------------------------------------------------------

		panel_informacion_voltaje= wx.Panel(self.panel,-1,size=(400,200),pos=(520,250))
		panel_informacion_voltaje.SetBackgroundColour("#FFFFFF")

		txt_rango_aceptable = wx.StaticText(panel_informacion_voltaje, -1, "límites de variaciones de\nredes eléctricas\n\nEn el rango de 127-10% - 127+10% \nMayor a 127+10% \nMenor a 127-10%", pos=(30, 35))
		font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		txt_rango_aceptable.SetFont(font)

		decoracion_derecha1_panel_informacion= wx.Panel(panel_informacion_voltaje,-1,size=(200,5),pos=(0,0))
		decoracion_derecha1_panel_informacion.SetBackgroundColour("#FFDF49")

		decoracion_derecha2_panel_informacion= wx.Panel(panel_informacion_voltaje,-1,size=(5,100),pos=(0,0))
		decoracion_derecha2_panel_informacion.SetBackgroundColour("#FFDF49")
		
		decoracion_izquierda1_panel_informacion= wx.Panel(panel_informacion_voltaje,-1,size=(200,5),pos=(200,195))
		decoracion_izquierda1_panel_informacion.SetBackgroundColour("#7F7856")

		decoracion_izquierda2_panel_informacion= wx.Panel(panel_informacion_voltaje,-1,size=(5,100),pos=(395,100))
		decoracion_izquierda2_panel_informacion.SetBackgroundColour("#7F7856")

	def cargarDatos(self,event):
		self.rango_mayor = float(127 + (127 * (10 / 100)))
		self.rango_menor = float(127 - (127 * (10 / 100))) 

		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))
		
		self.fecha = []
		fecha_larga = df['Fecha']
		for i in fecha_larga:
			self.fecha.append(str(i).rstrip(':0'))

		self.hora = df.Hora.str.slice(0,12) 
		
		voltaje= df[('Vrms ph-n %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
		estado_voltaje = self.reglas_voltaje.GetString(self.reglas_voltaje.GetSelection())

		if estado_voltaje == "RANGO":
			lista_rango, lista_hora, lista_fecha = self.pruebaRango(voltaje)	
		elif estado_voltaje == "MAYOR":
			lista_rango, lista_hora, lista_fecha = self.pruebaMayor(voltaje)
		elif estado_voltaje == "MENOR":
			lista_rango, lista_hora, lista_fecha =self.pruebaMenor(voltaje)

	def reporteAnalisis(self,event):
		try:
			estado_voltaje = self.reglas_voltaje.GetString(self.reglas_voltaje.GetSelection())
			crear = NuevoArchivoVoltajeReglas()
			crear.CrearArchivo(self.archivo_excel,estado_voltaje)
			self.msgInformacion("Archivo Guardado")

		except Exception:
			self.msgError("Error al guardar el archivo")

	def pruebaRango(self, voltaje_fase):
		lista_fecha = []
		lista_hora = []
		lista_rango = []
		pos = 0
		self.list_ctrl.DeleteAllItems()
		for i in range(len(voltaje_fase)):
			if voltaje_fase[i] < self.rango_mayor and voltaje_fase[i] > self.rango_menor:
				pos += i
				lista_rango.append(voltaje_fase[pos])
				lista_fecha.append(self.fecha[pos])
				lista_hora.append(self.hora[pos])
				pos = 0
		self.llenarTablavoltaje(lista_rango, lista_hora, lista_fecha)
		return lista_rango, lista_hora, lista_fecha
	
	def pruebaMenor(self,voltaje_fase):
		lista_fecha = []
		lista_hora = []
		lista_menores = []
		pos = 0
		self.list_ctrl.DeleteAllItems()
		for i in range(len(voltaje_fase)):
			if voltaje_fase[i] < self.rango_menor:
				pos += i
				lista_menores.append(voltaje_fase[pos])
				lista_fecha.append(self.fecha[pos])
				lista_hora.append(self.hora[pos])
				pos = 0
		self.llenarTablavoltaje(lista_menores, lista_hora, lista_fecha)
			
	def pruebaMayor(self,voltaje_fase):
		lista_fecha = []
		lista_hora = []
		lista_mayores = []
		pos = 0
		self.list_ctrl.DeleteAllItems()
		for i in range(len(voltaje_fase)):
			if voltaje_fase[i] > self.rango_mayor:
				pos += i
				lista_mayores.append(voltaje_fase[pos])
				lista_fecha.append(self.fecha[pos])
				lista_hora.append(self.hora[pos])
				pos = 0
		self.llenarTablavoltaje(lista_mayores, lista_hora, lista_fecha) 
		
	def llenarTablavoltaje(self,datovoltaje,lista_hora,lista_fecha):
		index = 0
		for data in range(len(datovoltaje)):
			self.list_ctrl.InsertItem(index, str(lista_fecha[data]))
			self.list_ctrl.SetItem(index, 1, str(lista_hora[data]))
			self.list_ctrl.SetItem(index, 2, str(datovoltaje[data]))	

			if index % 2:
				self.list_ctrl.SetItemBackgroundColour(index, "#F2F2F2")
			else:
				self.list_ctrl.SetItemBackgroundColour(index, "#ECF2F2")
			index += 1

		if index > 0:
			self.msgInformacion("Se encontro %d datos"% index)
		else:
			self.msgInformacion("No se encontro nigun dato")

	def msgInformacion(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'Informacion', wx.ICON_INFORMATION|wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def msgError(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'Error', wx.ICON_ERROR|wx.OK)
		answer = box.ShowModal()
		box.Destroy()


	def graficaVolageVsTiempo(self, event):
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))

		datos_voltaje_fase_a = df['Vrms ph-n AN Med'].values
		datos_voltaje_fase_b = df['Vrms ph-n BN Med'].values
		datos_voltaje_fase_c = df['Vrms ph-n CN Med'].values 

		ls_hora = df.Hora.str.slice(0,2)
		ls_minuto = df.Hora.str.slice(3,5)
		ls_tiempo = df.Hora.str.slice(9,12)

		grafica = GraficaPotencia()
		grafica.grafica("voltaje",ls_hora,ls_minuto,ls_tiempo,datos_voltaje_fase_a,datos_voltaje_fase_b,datos_voltaje_fase_c,'Tiempo(Hora)','Voltaje')

	def footer(self):
		barra_estado = self.CreateStatusBar(1) # crear pie de pagina
		barra_estado.SetBackgroundColour('#6E7B99')
		barra_estado.SetStatusWidths([-1])
	
		barra_estado_fields = ["Todos los derechos reservados."]
		for i in range(len(barra_estado_fields)):
			barra_estado.SetStatusText(barra_estado_fields[i], i)