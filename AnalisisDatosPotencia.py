#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import wx.grid
import pandas as pd
import math
import matplotlib.pyplot as plt
import wx.lib.agw.aquabutton as AB
import wx.lib.agw.gradientbutton as GB
from matplotlib.widgets import CheckButtons
from GraficaPotencia import GraficaPotencia
from cycler import cycler
from menu import Menu

class AnalisisDatosPotencia(wx.Frame):

	def __init__(self, id, title, archivo):
		self.archivo_excel = archivo
		self.txt_fase_a = []
		self.txt_fase_b = []
		self.txt_fase_c = []

		self.frame = wx.Frame.__init__(self, None, id, title, size = (1100, 730), style = wx.DEFAULT_FRAME_STYLE )
			#& ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)) # bloquear boton de maximizar

		self.SetIcon(wx.Icon(logotipo1))
		self.panel = wx.Panel(self,-1,size=(1200,700),pos=(0,120))

		self.Elementos()
		menu = Menu(4,self.archivo_excel)
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

		
		bmp1 = wx.Image(logotipo1, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(header, -1, bmp1, (30,10))

		txt_seleccion_dia = wx.StaticText(self.panel, -1, "Día: ", pos=(520,38))
		txt_seleccion_estado_voltage = wx.StaticText(self.panel, wx.ID_ANY,  "Potencia: ", pos=(520,68))
		txt_seleccion_fase = wx.StaticText(self.panel, wx.ID_ANY,  "Fase: ", pos=(520,100))
		
		txt_grafica = wx.StaticText(self.panel, -1, "Grafica ", pos=(558,220))
		
		#-------------------------------------------------------------------------------------------------	

		dias = self.archivo_excel.sheet_names
		self.choice = wx.Choice(self.panel, choices = dias, pos=(620, 30))
		self.choice.SetSelection(0)	
		
		reglas = ["RANGO","MENOR"]
		self.reglas_potencia = wx.Choice(self.panel, choices = reglas, pos=(620, 65),size=(100,26))
		self.reglas_potencia.SetSelection(0)	

		lista_fase = ["A", "B", "C"]
		self.Fase = wx.Choice(self.panel, choices = lista_fase, pos=(620, 95),size=(100,26))
		self.Fase.SetSelection(0)	
		
		# -------------------------------------------------------------------------------------------------	
		
		bmp1 = wx.Image('imagenes/calendario.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		icon_seleccionar_dia = wx.StaticBitmap(self.panel, -1, bmp1, (585, 30))

		bmp2 = wx.Image( 'imagenes/potencia1.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		icon_estado_voltage = wx.StaticBitmap(self.panel, -1, bmp2, (585, 65))

		bmp3 = wx.Image('imagenes/fase.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		icon_fase = wx.StaticBitmap(self.panel, -1, bmp3, (585, 95))
		# -------------------------------------------------------------------------------------------------	

		btn_listar = wx.Button(self.panel, 7, u"Listar", size=(200,30), pos=(520,130))
		btn_listar.Bind(wx.EVT_BUTTON, self.cargarDatos)

		ico_grafica = wx.Bitmap("imagenes/grafica.png", wx.BITMAP_TYPE_ANY)
		button_grafica_faseA = AB.AquaButton(self.panel, 1, bitmap=ico_grafica, size=(38,35),pos=(560,180))
		button_grafica_faseA.SetForegroundColour("red")
		button_grafica_faseA.Bind(wx.EVT_BUTTON, self.graficaFactorPotencia )

		self.Layout()	

		#----------------------------------------------------------------------------------------------------		
		self.list_ctrl = wx.ListCtrl(self.panel, pos=(25, 25), size=(450,450),
							style=wx.LC_REPORT
							|wx.BORDER_SUNKEN|wx.LC_HRULES|wx.LC_VRULES
							)
		self.list_ctrl.InsertColumn(0, 'Fecha',width=150)
		self.list_ctrl.InsertColumn(1, 'Hora',width=150)
		self.list_ctrl.InsertColumn(2, 'Factor de Potencia',width=200)	
		#----------------------------------------------------------------------------------------------------

		panel_informacion_voltage= wx.Panel(self.panel,-1,size=(300,200),pos=(520,250))

		txt_rango_aceptable = wx.StaticText(panel_informacion_voltage, -1, "El factor de potencia debe estar\nentre 0.9 y 1.0", pos=(30, 30))
		font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		txt_rango_aceptable.SetFont(font)

		decoracion_derecha1_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(200,5),pos=(0,0))
		decoracion_derecha2_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(5,100),pos=(0,0))
		decoracion_izquierda1_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(200,5),pos=(100,195))
		decoracion_izquierda2_panel_informacion= wx.Panel(panel_informacion_voltage,-1,size=(5,100),pos=(295,100))

		decoracion_izquierda2_panel_informacion.SetBackgroundColour("#7F7856")
		decoracion_derecha1_panel_informacion.SetBackgroundColour("#FFDF49")
		decoracion_derecha2_panel_informacion.SetBackgroundColour("#FFDF49")
		decoracion_izquierda1_panel_informacion.SetBackgroundColour("#7F7856")
		panel_informacion_voltage.SetBackgroundColour("#FFFFFF")

		#----------------------------------------------------------------------------------------------------

	def cargarDatos(self,event):
		rango_mayor = 1
		rango_menor = 0.9 
		
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))
		fase =self.Fase.GetString(self.Fase.GetSelection())
		
		self.fecha = []
		fecha_larga = df['Fecha']
		for i in fecha_larga:
			self.fecha.append(str(i).rstrip(':0'))

		self.hora = df.Hora.str.slice(0,12) 
		potencia = df[('Factor de Potencia %sN Med')%(fase)].values
		reglas_potencia = self.reglas_potencia.GetString(self.reglas_potencia.GetSelection())
		
		if reglas_potencia == "RANGO":
			self.pruebaRango(potencia,rango_mayor,rango_menor)	

		elif reglas_potencia == "MENOR":
			self.pruebaMenor(potencia,rango_mayor,rango_menor)

	def pruebaRango(self,potencia_fase, rango_mayor, rango_menor):
		lista_fecha = []
		lista_hora = []
		lista_rango = []
		pos = 0
		self.list_ctrl.DeleteAllItems()
		for i in range(len(potencia_fase)):
			if potencia_fase[i] >= rango_menor and potencia_fase[i] <= rango_mayor:
				pos += i
				lista_rango.append(potencia_fase[i])
				lista_fecha.append(self.fecha[pos])
				lista_hora.append(self.hora[pos])
				pos = 0
		self.llenarTablaVoltage(lista_rango, lista_hora, lista_fecha)
	
	def pruebaMenor(self,potencia_fase, rango_mayor, rango_menor):
		lista_fecha = []
		lista_hora = []
		lista_menores = []
		pos = 0
		self.list_ctrl.DeleteAllItems()
		for i in range(len(potencia_fase)):
			if potencia_fase[i] < rango_menor:
				pos += i
				lista_menores.append(potencia_fase[i])
				lista_fecha.append(self.fecha[pos])
				lista_hora.append(self.hora[pos])
				pos = 0
		self.llenarTablaVoltage(lista_menores, lista_hora, lista_fecha)

	def llenarTablaVoltage(self, datoVoltage,lista_hora,lista_fecha):
		dato_voltaje = []
		numero_item = 0
		for data in range(len(datoVoltage)):
			dato_voltaje.append(math.fabs(datoVoltage[data]))
			self.list_ctrl.InsertItem(numero_item, str(lista_fecha[data]))
			self.list_ctrl.SetItem(numero_item, 1, str(lista_hora[data]))
			self.list_ctrl.SetItem(numero_item, 2, str(dato_voltaje[data]))	
			
			if numero_item % 2:
				self.list_ctrl.SetItemBackgroundColour(numero_item, "#F2F2F2")
			else:
				self.list_ctrl.SetItemBackgroundColour(numero_item, "#ECF2F2")
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

	def graficaFactorPotencia(self, event):
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))

		datos_factor_potencia_fase_a = df['Factor de Potencia AN Med'].values
		datos_factor_potencia_fase_b = df['Factor de Potencia BN Med'].values
		datos_factor_potencia_fase_c = df['Factor de Potencia CN Med'].values 

		ls_hora = df.Hora.str.slice(0,2)
		ls_minuto = df.Hora.str.slice(3,5)
		ls_tiempo = df.Hora.str.slice(9,12)
		
		grafica = GraficaPotencia()
		grafica.grafica("potencia",ls_hora,ls_minuto,ls_tiempo,datos_factor_potencia_fase_a,datos_factor_potencia_fase_b,datos_factor_potencia_fase_c,'Tiempo(Hora)','Factor de Potencia')

	def footer(self):
		barra_estado = self.CreateStatusBar(1)
		barra_estado.SetBackgroundColour('#6E7B99')
		barra_estado.SetStatusWidths([-1])
	
		barra_estado_fields = ["Todos los derechos reservados."]
		for i in range(len(barra_estado_fields)):
			barra_estado.SetStatusText(barra_estado_fields[i], i)