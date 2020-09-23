#!/usr/bin/python3
# -*- coding: utf-8 -*-
import wx
import wx.grid
import pandas as pd
import matplotlib.pyplot as plt
import wx.lib.agw.aquabutton as AB
from matplotlib.widgets import CheckButtons
from menu import Menu

class AnalisisDatosArmonicos(wx.Frame):
	NIVEL123 = 1.0
	NIVEL4 = 2.4

	def __init__(self, id, title, archivo):
		self.archivo_excel = archivo

		self.frame = wx.Frame.__init__(self, None, id, title, size = (1380, 730), style = wx.DEFAULT_FRAME_STYLE)
			#& ~(wx.MAXIMIZE_BOX)) # bloquear boton de maximizar

		menu = Menu(2,self.archivo_excel)
		menu.menugeneral(self)
		menu.opt_armonicos(self)

		self.panel = wx.Panel(self, -1, size=(1500, 730), pos=(0,120))
		# agrega icono a la ventana
		self.SetIcon(wx.Icon(logotipo1))
		self.Elementos()	
		self.footer()

	def salir(self, event):
		self.Destroy()

	def Elementos(self):
		header= wx.Panel(self,-1,size=(1500, 120),pos=(0,0))
		header.SetBackgroundColour("#6E7B99")

		titulo = wx.StaticText(header, wx.ID_ANY, "Efenergy", style=wx.ALIGN_CENTER, pos=(150,25))
		font = wx.Font(40, wx.ROMAN, wx.ITALIC, wx.NORMAL)
		titulo.SetFont(font)

		
		bmp1 = wx.Image(logotipo1, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(header, -1, bmp1, (30,10))

		txt_seleccion_dia = wx.StaticText(self.panel, -1, "Día: ", pos=(440,32))
		dias = self.archivo_excel.sheet_names
		self.choice = wx.Choice(self.panel, choices = dias, pos=(500, 30))
		self.choice.SetSelection(0)

		txt_seleccion_nivel_tension = wx.StaticText(self.panel, -1, "Tension: ", pos=(30,32))
		valores = ['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
		self.nivel_tension= wx.Choice(self.panel, choices = valores, pos=(120, 30),size=(90,26))
		self.nivel_tension.SetSelection(0)
		
		txt_seleccion_fase = wx.StaticText(self.panel, -1, "Fase: ", pos=(250,32))
		lista_fase = ["A", "B", "C"]
		self.Fase = wx.Choice(self.panel, choices = lista_fase, pos=(310, 30),size=(90,26))
		self.Fase.SetSelection(0)	

		btn_listar = wx.Button(self.panel, 7, u"Listar", size=(100,30), pos=(1010,30))
		btn_listar.Bind(wx.EVT_BUTTON, self.AnalisisArmonicos)

		# -------------------------------------------------------------------------------------------------			

		ico_grafica = wx.Bitmap("imagenes/grafica.png", wx.BITMAP_TYPE_ANY)
		button_grafica_faseA = AB.AquaButton(self.panel, 1, bitmap=ico_grafica, size=(35,35),pos=(1150,90))
		button_grafica_faseA.SetForegroundColour("black")
		button_grafica_faseA.Bind(wx.EVT_BUTTON, self.graficaArmonicoVsTiempo )
	
		icon_seleccionar_dia = 'imagenes/calendario.png'
		bmp1 = wx.Image(icon_seleccionar_dia, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (465, 30))

		icon_listar = 'imagenes/listar.png'
		bmp1 = wx.Image(icon_listar, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (975, 30))

		icon_estado_voltaje = 'imagenes/voltaje.png'
		bmp1 = wx.Image(icon_estado_voltaje, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (85, 30))

		icon_fase = 'imagenes/fase.png'
		bmp1 = wx.Image(icon_fase, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (280, 28))

		# -------------------------------------------------------------------------------------------------			

		self.list_ctrl = wx.ListCtrl(self.panel, pos=(30, 70), size=(1080,400),
                         style=wx.LC_REPORT
                         |wx.BORDER_SUNKEN|wx.LC_HRULES|wx.LC_VRULES
                         )
		self.list_ctrl.InsertColumn(0, 'Fecha')
		self.list_ctrl.InsertColumn(1, 'Hora')
		self.list_ctrl.InsertColumn(2, 'THD V')
		self.list_ctrl.InsertColumn(3, '	')
		self.list_ctrl.InsertColumn(4, 'ARM 1')
		self.list_ctrl.InsertColumn(5, 'ARM 2')
		self.list_ctrl.InsertColumn(6, 'ARM 3')
		self.list_ctrl.InsertColumn(7, 'ARM 4')
		self.list_ctrl.InsertColumn(8, 'ARM 5')
		self.list_ctrl.InsertColumn(9, 'ARM 6')
		self.list_ctrl.InsertColumn(10, 'ARM 7')
		self.list_ctrl.InsertColumn(11, 'ARM 8')
		self.list_ctrl.InsertColumn(12, 'ARM 9')
		self.list_ctrl.InsertColumn(13, 'ARM 10')
		self.list_ctrl.InsertColumn(14, 'ARM 11')
	
	
	def cargarDatos(self):
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))

		fecha = []
		fecha_larga = df['Fecha']
		for i in fecha_larga:
			fecha.append(str(i).rstrip(':0'))
		hora = df.Hora.str.slice(0,12) 

		thdv = df[('THD V %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values

		armonico0 = df[('Armónicos Tensión0 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico1 = df[('Armónicos Tensión1 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico2 = df[('Armónicos Tensión2 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico3 = df[('Armónicos Tensión3 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico4 = df[('Armónicos Tensión4 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico5 = df[('Armónicos Tensión5 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico6 = df[('Armónicos Tensión6 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico7 = df[('Armónicos Tensión7 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico8 = df[('Armónicos Tensión8 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico9 = df[('Armónicos Tensión9 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico10 = df[('Armónicos Tensión10 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values
		armonico11 = df[('Armónicos Tensión11 %sN Med')%self.Fase.GetString(self.Fase.GetSelection())].values

		return thdv,fecha,hora,armonico0,armonico1,armonico2,armonico3,armonico4,armonico5,armonico6,armonico7,armonico8,armonico9,armonico10,armonico11

	def AnalisisArmonicos(self, event):
		lista_fecha = []
		lista_hora = []
		lista_thdv = []
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
		pos = 0
		identificador = event.GetId()
		thdv,fecha,hora,armonico0,armonico1,armonico2,armonico3,armonico4,armonico5,armonico6,armonico7,armonico8,armonico9,armonico10,armonico11 = self.cargarDatos()
		self.list_ctrl.DeleteAllItems()
		
		nivel_tension = self.nivel_tension.GetString( self.nivel_tension.GetSelection())

		for i in range(len(thdv)):
			if (nivel_tension == 'Nivel 1') or (nivel_tension == 'Nivel 2') or (nivel_tension == 'Nivel 3'):
				if thdv[i] > self.NIVEL123:
					pos += i
					lista_fecha.append(fecha[pos])
					lista_hora.append(hora[pos])
					lista_thdv.append(thdv[i])
					lista0.append(armonico0[pos])
					lista1.append(armonico1[pos])
					lista2.append(armonico2[pos])
					lista3.append(armonico3[pos])
					lista4.append(armonico4[pos])
					lista5.append(armonico5[pos])
					lista6.append(armonico6[pos])
					lista7.append(armonico7[pos])
					lista8.append(armonico8[pos])
					lista9.append(armonico9[pos])
					lista10.append(armonico10[pos])
					lista11.append(armonico11[pos])
					pos = 0

			elif nivel_tension == 'Nivel 4':
				if thdv[i] > self.NIVEL4:
					pos += i
					lista_fecha.append(fecha[pos])
					lista_hora.append(hora[pos])
					lista_thdv.append(thdv[i])
					lista0.append(armonico0[pos])
					lista1.append(armonico1[pos])
					lista2.append(armonico2[pos])
					lista3.append(armonico3[pos])
					lista4.append(armonico4[pos])
					lista5.append(armonico5[pos])
					lista6.append(armonico6[pos])
					lista7.append(armonico7[pos])
					lista8.append(armonico8[pos])
					lista9.append(armonico9[pos])
					lista10.append(armonico10[pos])
					lista11.append(armonico11[pos])
					pos = 0

		self.llenarTabla(lista_fecha,lista_hora,lista_thdv,lista0,lista1,lista2,lista3,lista4,
			lista5,lista6,lista7,lista8,lista9,lista10,lista11)


	def llenarTabla(self, lista_fecha,lista_hora,lista_thdv,lista0,lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9,lista10,lista11):
		index = 0
		for data in range(len(lista_thdv)):
			self.list_ctrl.InsertItem(index, str(lista_fecha[data]))
			self.list_ctrl.SetItem(index, 1, str(lista_hora[data]))
			self.list_ctrl.SetItem(index, 2, str(lista_thdv[data]))
			self.list_ctrl.SetItem(index, 3, str(lista0[data]))
			self.list_ctrl.SetItem(index, 4, str(lista1[data]))
			self.list_ctrl.SetItem(index, 5, str(lista2[data]))
			self.list_ctrl.SetItem(index, 6, str(lista3[data]))
			self.list_ctrl.SetItem(index, 7, str(lista4[data]))
			self.list_ctrl.SetItem(index, 8, str(lista5[data]))
			self.list_ctrl.SetItem(index, 9, str(lista6[data]))
			self.list_ctrl.SetItem(index, 10, str(lista7[data]))
			self.list_ctrl.SetItem(index, 11, str(lista8[data]))
			self.list_ctrl.SetItem(index, 12, str(lista9[data]))
			self.list_ctrl.SetItem(index, 13, str(lista10[data]))
			self.list_ctrl.SetItem(index, 14, str(lista11[data]))
		
			if index % 2:
				self.list_ctrl.SetItemBackgroundColour(index, "#F2F2F2")
			else:
				self.list_ctrl.SetItemBackgroundColour(index, "#ECF2F2")
			index += 1

		if index > 0:
			self.InformacionDatos(index)
		else:
			self.InformacionDatos0()


	def InformacionDatos0(self):
		box = wx.MessageDialog(None, 'No se encontro nigun dato por encima del valor estipulado', 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def InformacionDatos(self, cont):
		box = wx.MessageDialog(None, ('Se encontro %d datos por encima del valor estipulado'% cont), 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def footer(self):
		barra_estado = self.CreateStatusBar(1) # crear pie de pagina
		barra_estado.SetBackgroundColour('#6E7B99')
		barra_estado.SetStatusWidths([-1])
	
		barra_estado_fields = ["Todos los derechos reservados."]
		for i in range(len(barra_estado_fields)):
			barra_estado.SetStatusText(barra_estado_fields[i], i)


	def graficaArmonicoVsTiempo(self, event):
		identificador = event.GetId()
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))

		fase = ['A','B','C']
		thdv = df[('THD V %sN Med')%fase[identificador - 1]].values
		armonico0 = df[('Armónicos Tensión0 %sN Med')%fase[identificador - 1]].values
		armonico1 = df[('Armónicos Tensión1 %sN Med')%fase[identificador - 1]].values
		armonico2 = df[('Armónicos Tensión2 %sN Med')%fase[identificador - 1]].values
		armonico3 = df[('Armónicos Tensión3 %sN Med')%fase[identificador - 1]].values
		armonico4 = df[('Armónicos Tensión4 %sN Med')%fase[identificador - 1]].values
		armonico5 = df[('Armónicos Tensión5 %sN Med')%fase[identificador - 1]].values
		armonico6 = df[('Armónicos Tensión6 %sN Med')%fase[identificador - 1]].values
		armonico7 = df[('Armónicos Tensión7 %sN Med')%fase[identificador - 1]].values
		armonico8 = df[('Armónicos Tensión8 %sN Med')%fase[identificador - 1]].values
		armonico9 = df[('Armónicos Tensión9 %sN Med')%fase[identificador - 1]].values
		armonico10 = df[('Armónicos Tensión10 %sN Med')%fase[identificador - 1]].values
		armonico11 = df[('Armónicos Tensión11 %sN Med')%fase[identificador - 1]].values
 

		ls_hora = df.Hora.str.slice(0,2)
		ls_minuto = df.Hora.str.slice(3,5)
		ls_tiempo = df.Hora.str.slice(9,12)
	
		lista_hora = []
		lista_thdv = []
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
			lista_thdv.append(thdv[i])
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

		GraficaBarras(2, lista_hora, lista_thdv, lista_armonico0, lista_armonico1, lista_armonico2, lista_armonico3, lista_armonico4, lista_armonico5, lista_armonico6, lista_armonico7, lista_armonico8, lista_armonico9, lista_armonico10, lista_armonico11)
		

