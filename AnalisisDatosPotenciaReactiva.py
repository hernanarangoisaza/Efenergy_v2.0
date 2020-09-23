#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import wx.grid
import math
import pandas as pd
import wx.lib.agw.aquabutton as AB
import wx.lib.agw.gradientbutton as GB
from menu import Menu
from GraficaPotencia import GraficaPotencia

class AnalisisDatosPotenciaReactiva(wx.Frame):

	def __init__(self, id, title, archivo):
		self.archivo_excel = archivo

		self.txt_fase_a = []
		self.txt_fase_b = []
		self.txt_fase_c = []

		self.frame = wx.Frame.__init__(self, None, id, title, size = (1100, 730), style = wx.DEFAULT_FRAME_STYLE )
			#& ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)) # bloquear boton de maximizar

		self.SetIcon(wx.Icon("imagenes/logo.png"))
		self.panel = wx.Panel(self,-1,size=(1200,700),pos=(0,120))
		self.Elementos()
		menu = Menu(5,self.archivo_excel)
		menu.menugeneral(self)
		self.footer()

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
		txt_seleccion_estado_voltage = wx.StaticText(self.panel, wx.ID_ANY,  "Voltaje: ", pos=(520,65))
		txt_seleccion_fase = wx.StaticText(self.panel, wx.ID_ANY,  "Fase: ", pos=(520,95))
		
		#-------------------------------------------------------------------------------------------------	

		dias = self.archivo_excel.sheet_names
		self.choice = wx.Choice(self.panel, choices = dias, pos=(620, 30))
		self.choice.SetSelection(0)	
		
		reglas = ["MAYOR","MENOR"]
		self.reglas_potencia = wx.Choice(self.panel, choices = reglas, pos=(620, 65),size=(100,26))
		self.reglas_potencia.SetSelection(0)	

		lista_fase = ["A", "B", "C"]
		self.Fase = wx.Choice(self.panel, choices = lista_fase, pos=(620, 95),size=(100,26))
		self.Fase.SetSelection(0)	
		
		# -------------------------------------------------------------------------------------------------	
		
		icon_seleccionar_dia = 'imagenes/calendario.png'
		bmp1 = wx.Image(icon_seleccionar_dia, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (585, 30))

		icon_estado_voltage = 'imagenes/potencia1.png'
		bmp1 = wx.Image(icon_estado_voltage, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (585, 65))

		icon_fase = 'imagenes/fase.png'
		bmp1 = wx.Image(icon_fase, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (585, 95))
		# -------------------------------------------------------------------------------------------------	

		btn_listar = wx.Button(self.panel, 7, u"Listar", size=(200,30), pos=(520,130))
		btn_listar.Bind(wx.EVT_BUTTON, self.cargarDatos)

		ico_grafica = wx.Bitmap("imagenes/grafica.png", wx.BITMAP_TYPE_ANY)
		btn_grafica = AB.AquaButton(self.panel, wx.ID_ANY, bitmap=ico_grafica, size=(38,35), pos=(530,180), style=wx.NO_BORDER)
		btn_grafica.SetForegroundColour("red")
		btn_grafica.Bind(wx.EVT_BUTTON, self.cargarGrafica )

		#----------------------------------------------------------------------------------------------------
		
		self.tabla_potencia_reactiva = wx.ListCtrl(self.panel, pos=(25, 25), size=(450,450),
							style=wx.LC_REPORT
							|wx.BORDER_SUNKEN|wx.LC_HRULES|wx.LC_VRULES
							)
		self.tabla_potencia_reactiva.InsertColumn(0, 'Fecha',width=100)
		self.tabla_potencia_reactiva.InsertColumn(1, 'Hora',width=100)
		self.tabla_potencia_reactiva.InsertColumn(2, 'Potencia Activa',width=130)
		self.tabla_potencia_reactiva.InsertColumn(3, 'Potencia Reactiva',width=130)
	
		#----------------------------------------------------------------------------------------------------

		panel_informacion_voltage= wx.Panel(self.panel,-1,size=(300,200),pos=(520,250))
		panel_informacion_voltage.SetBackgroundColour("#FFFFFF")

		txt_rango_aceptable = wx.StaticText(panel_informacion_voltage, -1, "la potencia reactiva debe ser menor\na la mitad de la potencia activa + 1", pos=(30, 30))
		font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		txt_rango_aceptable.SetFont(font)

		decoracion_derecha1_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(200,5),pos=(0,0))
		decoracion_derecha2_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(5,100),pos=(0,0))
		decoracion_izquierda1_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(200,5),pos=(100,195))
		decoracion_izquierda2_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(5,100),pos=(295,100))

		decoracion_derecha1_panel_informacion.SetBackgroundColour("#FFDF49")
		decoracion_derecha2_panel_informacion.SetBackgroundColour("#FFDF49")
		decoracion_izquierda1_panel_informacion.SetBackgroundColour("#7F7856")
		decoracion_izquierda2_panel_informacion.SetBackgroundColour("#7F7856")
		self.Layout()

	''' extraer los datos de el archivo de exel con respecto a la fase y 
		el dia seleccionado en las listas deplegables.si es selecionado 
		uno de los niveles de potencia se llama su respectivo metodo 
	'''
	def cargarDatos(self,event):
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))
		fase =self.Fase.GetString(self.Fase.GetSelection())
		reglas_potencia = self.reglas_potencia.GetString(self.reglas_potencia.GetSelection())

		self.fecha = []
		fecha_larga = df['Fecha']
		for i in fecha_larga:
			self.fecha.append(str(i).rstrip(':0'))
		self.hora = df.Hora.str.slice(0,12) 

		potencia_reactiva = df['Potencia Reactiva %sN Med'%(fase)].values
		potencia_activa = df['Potencia Activa %sN Med'%(fase)].values

		if reglas_potencia == "MAYOR":
			self.determinarPotenciaReactivaMayor(potencia_reactiva,potencia_activa)	
		elif reglas_potencia == "MENOR":
			self.determinarPotenciaReactivaMenor(potencia_reactiva,potencia_activa)
	
	def determinarPotenciaReactivaMayor(self, potencia_reactiva, potencia_activa):
		lista_fecha = []
		lista_hora = []
		lista_potencia_reactiva = []
		lista_potencia_activa = []
		posicion_dato = 0 
		self.tabla_potencia_reactiva.DeleteAllItems()

		for i in range(len(potencia_activa)):
			if potencia_activa[i] < 0:
				calculo = (potencia_activa[i] / 2) - 1
			else:
				calculo = (potencia_activa[i] / 2) + 1

			if potencia_reactiva[i] >= calculo:
				posicion_dato += i
				lista_fecha.append(self.fecha[posicion_dato])
				lista_hora.append(self.hora[posicion_dato])
				lista_potencia_activa.append(potencia_activa[posicion_dato])
				lista_potencia_reactiva.append(potencia_reactiva[i])
				posicion_dato = 0

		self.llenarTablaVoltage(lista_hora, lista_fecha, lista_potencia_activa, lista_potencia_reactiva)

	def determinarPotenciaReactivaMenor(self,potencia_reactiva, potencia_activa ):
		lista_fecha = []
		lista_hora = []
		lista_potencia_reactiva = []
		lista_potencia_activa = []
		posicion_dato = 0	
		self.tabla_potencia_reactiva.DeleteAllItems()

		for i in range(len(potencia_activa)):
			if potencia_activa[i] < 0:
				calculo = (potencia_activa[i] / 2) - 1
			else:
				calculo = (potencia_activa[i] / 2) + 1

			if potencia_reactiva[i] < calculo:
				posicion_dato += i
				lista_fecha.append(self.fecha[posicion_dato])
				lista_hora.append(self.hora[posicion_dato])
				lista_potencia_activa.append(potencia_activa[posicion_dato])
				lista_potencia_reactiva.append(potencia_reactiva[i])
				posicion_dato = 0
		self.llenarTablaVoltage(lista_hora, lista_fecha, lista_potencia_activa,  lista_potencia_reactiva)

	
	def llenarTablaVoltage(self, lista_hora, lista_fecha, lista_potencia_activa, lista_potencia_reactiva):
		numero_item = 0
		for data in range(len(lista_potencia_activa)):
			self.tabla_potencia_reactiva.InsertItem(numero_item, str(lista_fecha[data]))
			self.tabla_potencia_reactiva.SetItem(numero_item, 1, str(lista_hora[data]))
			self.tabla_potencia_reactiva.SetItem(numero_item, 2, str(lista_potencia_activa[data]))
			self.tabla_potencia_reactiva.SetItem(numero_item, 3, str(lista_potencia_reactiva[data]))	
			
			if numero_item % 2:
				self.tabla_potencia_reactiva.SetItemBackgroundColour(numero_item, "#F2F2F2")
			else:
				self.tabla_potencia_reactiva.SetItemBackgroundColour(numero_item, "#ECF2F2")
			numero_item += 1

		if numero_item > 0:
			self.InformacionDatos(numero_item)
		else:
			self.InformacionDatos0()

	def InformacionDatos0(self):
		box = wx.MessageDialog(None, 'No se encontro nigun dato', 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def InformacionDatos(self, cont):
		box = wx.MessageDialog(None, ('Se encontro %d datos'% cont), 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def cargarGrafica(self,event):
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))
		datos_potencia_reactiva_fase_a = df['Potencia Reactiva AN Med'].values
		datos_potencia_reactiva_fase_b = df['Potencia Reactiva BN Med'].values
		datos_potencia_reactiva_fase_c = df['Potencia Reactiva CN Med'].values 
		ls_hora = df.Hora.str.slice(0,2)
		ls_minuto = df.Hora.str.slice(3,5)
		ls_tiempo = df.Hora.str.slice(9,12)

		grafica = GraficaPotencia()
		grafica.grafica("potencia",ls_hora,ls_minuto,ls_tiempo,datos_potencia_reactiva_fase_a,datos_potencia_reactiva_fase_b,datos_potencia_reactiva_fase_c,'Tiempo(Hora)','Potencia Reactiva')

	def footer(self):
		barra_estado = self.CreateStatusBar(1)
		barra_estado.SetBackgroundColour('#6E7B99')
		barra_estado.SetStatusWidths([-1])
	
		barra_estado_fields = ["Todos los derechos reservados."]
		for i in range(len(barra_estado_fields)):
			barra_estado.SetStatusText(barra_estado_fields[i], i)
