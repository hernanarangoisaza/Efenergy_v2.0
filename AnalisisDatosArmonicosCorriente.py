#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import pandas as pd
import easygui as eg
import matplotlib.pyplot as plt
import numpy as np
import wx.lib.agw.aquabutton as AB
import wx.lib.agw.gradientbutton as GB
from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons
from menu import Menu

class AnalisisDatosArmonicosCorriente(wx.Frame):

	def __init__(self, id, title, archivo):
		self.archivo_excel = archivo

		self.frame = wx.Frame.__init__(self, None, id, title, size = (1300, 730), style = wx.DEFAULT_FRAME_STYLE )
			#& ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)) # bloquear boton de maximizar

		self.SetIcon(wx.Icon("Images/logo.png"))

		self.lista_hora = []

		menu = Menu(1,self.archivo_excel)
		menu.menugeneral(self)
		menu.opt_armonicos(self)

		self.elementos()
		self.footer()

	def elementos(self):
		self.panel = wx.Panel(self, -1, size=(1500, 730), pos=(0,120))

		header= wx.Panel(self,-1,size=(1500, 120),pos=(0,0))
		header.SetBackgroundColour("#6E7B99")

		titulo = wx.StaticText(header, wx.ID_ANY, "Efenergy", style=wx.ALIGN_CENTER, pos=(150,25))
		font = wx.Font(40, wx.ROMAN, wx.ITALIC, wx.NORMAL)
		titulo.SetFont(font)


		logotipo = 'images/logotipo.JPG'
		bmp1 = wx.Image(logotipo, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(header, -1, bmp1, (30,10))

		txt_seleccion_dia = wx.StaticText(self.panel, -1, "Día: ", pos=(30,32))
		dias = self.archivo_excel.sheet_names
		self.choice = wx.Choice(self.panel, choices = dias, pos=(100, 30))
		self.choice.SetSelection(0)

		txt_seleccion_fase = wx.StaticText(self.panel, -1, "Fase: ", pos=(430,32))
		lista_fase = ["A", "B", "C"]
		self.Fase = wx.Choice(self.panel, choices = lista_fase, pos=(500, 30),size=(90,26))
		self.Fase.SetSelection(0)	

		btn_listar = wx.Button(self.panel, 7, u"Listar", size=(100,30), pos=(1010,30))
		btn_listar.Bind(wx.EVT_BUTTON, self.analisisArmonicos)

		# -------------------------------------------------------------------------------------------------			

		ico_grafica = wx.Bitmap("Images/grafica.png", wx.BITMAP_TYPE_ANY)
		button_grafica_faseA = AB.AquaButton(self.panel, 1, bitmap=ico_grafica, size=(35,35),pos=(1150,90))
		button_grafica_faseA.SetForegroundColour("black")
		button_grafica_faseA.Bind(wx.EVT_BUTTON, self.grafica )
	
		icon_seleccionar_dia = 'images/calendario.png'
		bmp1 = wx.Image(icon_seleccionar_dia, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (67, 30))

		icon_listar = 'images/listar.png'
		bmp1 = wx.Image(icon_listar, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (975, 30))
		
		icon_fase = 'images/fase.png'
		bmp1 = wx.Image(icon_fase, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (470, 28))


		self.list_ctrl = wx.ListCtrl(self.panel, pos=(30, 70), size=(1080,400),
                         style=wx.LC_REPORT
                         |wx.BORDER_SUNKEN|wx.LC_HRULES|wx.LC_VRULES
                         )
		self.list_ctrl.InsertColumn(0, 'Fecha')
		self.list_ctrl.InsertColumn(1, 'Hora')
		self.list_ctrl.InsertColumn(2, 'Corr. Fundamental', width=120)
		self.list_ctrl.InsertColumn(3, 'THD A')
		self.list_ctrl.InsertColumn(4, 'ARM 0')
		self.list_ctrl.InsertColumn(5, 'ARM 1')
		self.list_ctrl.InsertColumn(6, 'ARM 2')
		self.list_ctrl.InsertColumn(7, 'ARM 3')
		self.list_ctrl.InsertColumn(8, 'ARM 4')
		self.list_ctrl.InsertColumn(9, 'ARM 5')
		self.list_ctrl.InsertColumn(10, 'ARM 6')
		self.list_ctrl.InsertColumn(11, 'ARM 7')
		self.list_ctrl.InsertColumn(12, 'ARM 8')
		self.list_ctrl.InsertColumn(13, 'ARM 9')
		self.list_ctrl.InsertColumn(14, 'ARM 10')
		self.list_ctrl.InsertColumn(15, 'ARM 11')

	def analisisArmonicos(self, event):
		fase=self.Fase.GetString(self.Fase.GetSelection())
		self.list_ctrl.DeleteAllItems()

		lista_corriente = []
		lista_fecha = []
		self.lista_thda = []
		lista0 = []
		lista1 = []
		lista2 = []
		lista3 = []
		lista4 = []
		lista5 = []
		lista6 = []
		lista7 = []
		lista8 = []
		lista9 = []
		lista10 = []
		lista11 = []
		cont = 0

		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))
		thda = df[('THD A %s Med')%(fase)].values
		fecha = df['Fecha'].values
		hora = df['Hora'].values

		corriente = df[('Corriente Fundamental %s Med')%(fase)].values
		armonico0 = df[('Armónicos Corriente0 %s Med')%(fase)].values
		armonico1 = df[('Armónicos Corriente1 %s Med')%(fase)].values
		armonico2 = df[('Armónicos Corriente2 %s Med')%(fase)].values
		armonico3 = df[('Armónicos Corriente3 %s Med')%(fase)].values
		armonico4 = df[('Armónicos Corriente4 %s Med')%(fase)].values
		armonico5 = df[('Armónicos Corriente5 %s Med')%(fase)].values
		armonico6 = df[('Armónicos Corriente6 %s Med')%(fase)].values
		armonico7 = df[('Armónicos Corriente7 %s Med')%(fase)].values
		armonico8 = df[('Armónicos Corriente8 %s Med')%(fase)].values
		armonico9 = df[('Armónicos Corriente9 %s Med')%(fase)].values
		armonico10 = df[('Armónicos Corriente10 %s Med')%(fase)].values
		armonico11 = df[('Armónicos Corriente11 %s Med')%(fase)].values

		for i in range(len(thda)):
			cont += 1
			lista_fecha.append(fecha[i])
			self.lista_hora.append(hora[i])
			lista_corriente.append(corriente[i])
			self.lista_thda.append(thda[i])
			lista0.append(armonico0[i])
			lista1.append(armonico1[i])
			lista2.append(armonico2[i])
			lista3.append(armonico3[i])
			lista4.append(armonico4[i])
			lista5.append(armonico5[i])
			lista6.append(armonico6[i])
			lista7.append(armonico7[i])
			lista8.append(armonico8[i])
			lista9.append(armonico9[i])
			lista10.append(armonico10[i])
			lista11.append(armonico11[i])
			
		index = 0
		for data in range(len(self.lista_thda)):
			self.list_ctrl.InsertItem(index, str(lista_fecha[data]))
			self.list_ctrl.SetItem(index, 1, str(self.lista_hora[data]))
			self.list_ctrl.SetItem(index, 2, str(lista_corriente[data]))
			self.list_ctrl.SetItem(index, 3, str(self.lista_thda[data]))
			self.list_ctrl.SetItem(index, 4, str(lista0[data]))
			self.list_ctrl.SetItem(index, 5, str(lista1[data]))
			self.list_ctrl.SetItem(index, 6, str(lista2[data]))
			self.list_ctrl.SetItem(index, 7, str(lista3[data]))
			self.list_ctrl.SetItem(index, 8, str(lista4[data]))
			self.list_ctrl.SetItem(index, 9, str(lista5[data]))
			self.list_ctrl.SetItem(index, 10, str(lista6[data]))
			self.list_ctrl.SetItem(index, 11, str(lista7[data]))
			self.list_ctrl.SetItem(index, 12, str(lista8[data]))
			self.list_ctrl.SetItem(index, 13, str(lista9[data]))
			self.list_ctrl.SetItem(index, 14, str(lista10[data]))
			self.list_ctrl.SetItem(index, 15, str(lista11[data]))

			if index % 2:
				self.list_ctrl.SetItemBackgroundColour(index, "#F2F2F2")
			else:
				self.list_ctrl.SetItemBackgroundColour(index, "#ECF2F2")
			index += 1

		if cont > 0:
			self.informacionDatos(cont)
		else:
			self.informacionDatosNone()

	def grafica(self, event):
		fase=self.Fase.GetString(self.Fase.GetSelection())
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))
		
		thda = df['THD A %s Med'%(fase)].values
		armonico0 = df['Armónicos Corriente0 %s Med'%(fase)].values
		armonico1 = df['Armónicos Corriente1 %s Med'%(fase)].values
		armonico2 = df['Armónicos Corriente2 %s Med'%(fase)].values
		armonico3 = df['Armónicos Corriente3 %s Med'%(fase)].values
		armonico4 = df['Armónicos Corriente4 %s Med'%(fase)].values
		armonico5 = df['Armónicos Corriente5 %s Med'%(fase)].values
		armonico6 = df['Armónicos Corriente6 %s Med'%(fase)].values
		armonico7 = df['Armónicos Corriente7 %s Med'%(fase)].values
		armonico8 = df['Armónicos Corriente8 %s Med'%(fase)].values
		armonico9 = df['Armónicos Corriente9 %s Med'%(fase)].values
		armonico10 = df['Armónicos Corriente10 %s Med'%(fase)].values
		armonico11 = df['Armónicos Corriente11 %s Med'%(fase)].values 

		ls_hora = df.Hora.str.slice(0,2)
		ls_minuto = df.Hora.str.slice(3,5)
		ls_tiempo = df.Hora.str.slice(9,12)
	
		lista_hora = []
		lista_thda = []
		lista_armonico0 = []
		lista_armonico1 = []
		lista_armonico2 = []
		lista_armonico3 = []
		lista_armonico4 = []
		lista_armonico5 = []
		lista_armonico6 = []
		lista_armonico7 = []
		lista_armonico8 = []
		lista_armonico9 = []
		lista_armonico10 = []
		lista_armonico11 = []

		for i in range(len(ls_hora)):
			lista_hora.append(ls_hora[i]+":"+ls_minuto[i]+ls_tiempo[i])
			lista_thda.append(thda[i])
			lista_armonico0.append(armonico0[i])
			lista_armonico1.append(armonico1[i])
			lista_armonico2.append(armonico2[i])
			lista_armonico3.append(armonico3[i])
			lista_armonico4.append(armonico4[i])
			lista_armonico5.append(armonico5[i])
			lista_armonico6.append(armonico6[i])
			lista_armonico7.append(armonico7[i])
			lista_armonico8.append(armonico8[i])
			lista_armonico9.append(armonico9[i])
			lista_armonico10.append(armonico10[i])
			lista_armonico11.append(armonico11[i])
			

		from GraficaBarras import GraficaBarras

		GraficaBarras(1, lista_hora, lista_thda, lista_armonico0, lista_armonico1, lista_armonico2, lista_armonico3, lista_armonico4, lista_armonico5, lista_armonico6, lista_armonico7, lista_armonico8, lista_armonico9, lista_armonico10, lista_armonico11)
		

	def salir(self,event):
		self.Destroy()

	
	def informacionDatosNone(self):
		box = wx.MessageDialog(None, 'No se encontro nigun dato por encima del valor estipulado', 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def informacionDatos(self, cont):
		box = wx.MessageDialog(None, ('Se encontro %d datos'% cont), 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()


	def footer(self):
		barra_estado = self.CreateStatusBar(1) # crear pie de pagina
		barra_estado.SetBackgroundColour('#6E7B99')
		barra_estado.SetStatusWidths([-1])
	
		barra_estado_fields = ["Todos los derechos reservados."]
		for i in range(len(barra_estado_fields)):
			barra_estado.SetStatusText(barra_estado_fields[i], i)


	
