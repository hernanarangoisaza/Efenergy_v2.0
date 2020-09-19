#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import wx.grid
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from menu_general import Menu2
import wx.lib.agw.aquabutton as AB
from norma import Norma

class AnalisisDistorcionArmonica(wx.Frame):
	def __init__(self, id, title, archivo,pcc):
		if id == 1:
			self.armonico = "A"
		elif id == 2:
			self.armonico = "V"
		self.archivo_excel = archivo
		self.pcc = pcc

		self.frame = wx.Frame.__init__(self, None, id, title, size = (1200, 730), style = wx.DEFAULT_FRAME_STYLE )
			#& ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)) # bloquear boton de maximizar
		self.bSizer1 = wx.BoxSizer( wx.VERTICAL )
		self.bSizerInformacion = wx.BoxSizer( wx.VERTICAL)
		self.panel = wx.ScrolledWindow( self, wx.ID_ANY, size=(1500,570), pos=(0,120), style=wx.HSCROLL|wx.VSCROLL )
		self.panel.SetScrollRate( 5, 5 )

		self.SetIcon(wx.Icon("Images/logo.png"))
		self.Elementos()
		self.footer()

	def Elementos(self):
		header= wx.Panel(self,-1,size=(1500, 120),pos=(0,0))
		header.SetBackgroundColour("#6E7B99")
		
		titulo = wx.StaticText(header, wx.ID_ANY, "Efenergy", style=wx.ALIGN_CENTER, pos=(150,25))
		font = wx.Font(40, wx.ROMAN, wx.ITALIC, wx.NORMAL)
		titulo.SetFont(font)


		logotipo = 'images/logotipo.JPG'
		bmp1 = wx.Image(logotipo, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(header, -1, bmp1, (30,10))

		txt_seleccion_dia = wx.StaticText(self.panel, -1, "Día: ", pos=(30,30))
		dias = self.archivo_excel.sheet_names
		self.choice = wx.Choice(self.panel, choices = dias, pos=(100, 30))
		self.choice.SetSelection(0)

		# Para Datos en el Rango
		txt_fase = wx.StaticText(self.panel, -1, "Fase: ", pos=(400,30))
		lista_fase = ["A", "B", "C"]
		self.Fase = wx.Choice(self.panel, choices = lista_fase, pos=(480, 30),size=(90,26))
		self.Fase.SetSelection(0)	
		
		txt_armonico = wx.StaticText(self.panel, -1, "Para armónicos: ", pos=(600,30))
		lista_armonico = ["ENTRE 1 Y 10", " MAYORES A 11"]
		self.para_armonicos= wx.Choice(self.panel, choices = lista_armonico, pos=(700, 30),size=(110,26))
		self.para_armonicos.SetSelection(0)	
		
		menu = Menu2()
		menu.menugeneral(self, self.archivo_excel)

		# Tabla de datos voltage  
		self.list_ctrl = wx.ListCtrl(self.panel, pos=(30, 100), size=(1080,400),
						style=wx.LC_REPORT
						|wx.BORDER_SUNKEN|wx.LC_HRULES|wx.LC_VRULES
						)
		self.list_ctrl.InsertColumn(0, 'Fecha')
		self.list_ctrl.InsertColumn(1, 'Hora',width=100)
		self.list_ctrl.InsertColumn(2, ('THD %s Alterado')%self.armonico,width=150)
		self.list_ctrl.InsertColumn(3, 'Distorcion Armonica',width=150)
		self.list_ctrl.InsertColumn(4, 'Msj ',width=150)
		
		#--------------------------------------------------------------------------------------------

		icon_seleccionar_dia = 'images/calendario.png'
		bmp1 = wx.Image(icon_seleccionar_dia, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (70, 30))
		
		icon_fase = 'images/fase.png'
		bmp1 = wx.Image(icon_fase, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (450, 28))

		btn_listar = wx.Button(self.panel, 7, u"Listar", size=(100,30), pos=(1010,30))
		btn_listar.Bind(wx.EVT_BUTTON, self.validacion_entre_armonico_10_11)
		
		icon_listar = 'images/listar.png'
		bmp1 = wx.Image(icon_listar, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (975, 30))
		
		btn_norma = wx.Button(self.panel, 7, u"Norma", size=(100,30), pos=(1200,30))
		btn_norma.Bind(wx.EVT_BUTTON, self.ventanaNorma)

		#self.bSizerInformacion.Add(self.norma, 0, pos=(30, 560), style=wx.EXPAND)
		#self.panel.SetSizer(self.bSizerInformacion)
		#self.bSizer1.Add( self.panel, 1, wx.EXPAND, 5 )
		#self.SetSizer( self.bSizer1 )

		#--------------------------------------------------------------------------------------------
	def ventanaNorma(self,event):
		app = wx.App()
		norma = Norma(-1, 'Norma Distorcion armonica')
		norma.Centre()
		norma.Show()
		app.MainLoop()

	def validacion_entre_armonico_10_11(self,event):
		armonicos =self.para_armonicos.GetString(self.para_armonicos.GetSelection())
		if armonicos == "ENTRE 1 Y 10":
			self.validacionesDistorcionArmonica((4.0),(7.0),(10.0),(12.0),(15.0))
		if armonicos == " MAYORES A 11":
			self.validacionesDistorcionArmonica((2.0),(3.5),(4.5),(5.5),(7.0))

	def validacionesDistorcionArmonica(self,regla1,regla2,regla3,regla4,regla5):
		df = pd.read_excel(self.archivo_excel, self.choice.GetString(self.choice.GetSelection()))
		
		self.fecha = []
		fecha_larga = df['Fecha']
		for i in fecha_larga:
			self.fecha.append(str(i).rstrip(':0'))

		self.hora = df.Hora.str.slice(0,12) 

		lista_thd_alterado = []
		lista_armonico_1= []
		lista_armonico_2= []
		lista_armonico_3= []
		lista_armonico_4= []
		lista_armonico_5= []
		lista_armonico_6= []
		lista_armonico_7= []
		lista_armonico_8= []
		lista_armonico_9= []
		lista_armonico_10= []
		lista_armonico_11= []
		self.cont1 = 0
		
		lista_fecha1 = []
		lista_hora1 = []
		identifica_btn_11 = 0
		distorcion_armonica= []
		distorcion_4 =[]
		pos = 0

		corriente_fundamental = df[('Corriente Fundamental %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
		
		if self.armonico == "A":
			thd_a = df[('THD %s %s Med')%(self.armonico, self.Fase.GetString(self.Fase.GetSelection()))].values
			armonico_1 = df[('Armónicos Corriente1 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_2 = df[('Armónicos Corriente2 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_3 = df[('Armónicos Corriente3 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_4 = df[('Armónicos Corriente4 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_5 = df[('Armónicos Corriente5 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_6 = df[('Armónicos Corriente6 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_7 = df[('Armónicos Corriente7 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_8 = df[('Armónicos Corriente8 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_9 = df[('Armónicos Corriente9 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_10 = df[('Armónicos Corriente10 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			Armonico_11 = df[('Armónicos Corriente11 %s Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			
		if self.armonico == "V":
			thd_a = df[('THD %s %sN Med')%(self.armonico, self.Fase.GetString(self.Fase.GetSelection()))].values
			armonico_1 = df[('Armónicos Tensión1 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_2 = df[('Armónicos Tensión2 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_3 = df[('Armónicos Tensión3 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_4 = df[('Armónicos Tensión4 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_5 = df[('Armónicos Tensión5 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_6 = df[('Armónicos Tensión6 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_7 = df[('Armónicos Tensión7 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_8 = df[('Armónicos Tensión8 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_9 = df[('Armónicos Tensión9 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			armonico_10 = df[('Armónicos Tensión10 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values
			Armonico_11 = df[('Armónicos Tensión11 %sN Med')% self.Fase.GetString(self.Fase.GetSelection())].values

		isc = int(self.pcc)
		mensaje = []
		
		for i in range(len(corriente_fundamental)):
			da = isc/corriente_fundamental[i]
			distorcion_armonica.append(da)

			# Distorcion Armonica < a 20 debe tener un thd a  < 4
			if distorcion_armonica[i] < 20 and thd_a[i] > regla1:
				pos += i
				distorcion_4.append(distorcion_armonica[pos])
				pos = 0
				self.cont1 += 1
				lista_thd_alterado.append(thd_a[i])
				lista_hora1.append(self.hora[i])
				lista_fecha1.append(self.fecha[i])
				mensaje.append(" thd mayor a  %d"%(regla1))
				if regla5 == 7:
					identifica_btn_11 = 5
					lista_armonico_11.append(Armonico_11[i]) 
				else:
					identifica_btn_11 = 4
					lista_armonico_1.append(armonico_1[i]) 
					lista_armonico_2.append(armonico_2[i]) 
					lista_armonico_3.append(armonico_3[i]) 
					lista_armonico_4.append(armonico_4[i]) 
					lista_armonico_5.append(armonico_5[i]) 
					lista_armonico_6.append(armonico_6[i]) 
					lista_armonico_7.append(armonico_7[i]) 
					lista_armonico_8.append(armonico_8[i]) 
					lista_armonico_9.append(armonico_9[i]) 
					lista_armonico_10.append(armonico_10[i]) 

			if  distorcion_armonica[i]  >= 20 and distorcion_armonica[i] <50 and thd_a[i] > regla2:
				pos += i
				distorcion_4.append(distorcion_armonica[pos])
				pos = 0
				self.cont1 += 1
				lista_thd_alterado.append(thd_a[i])
				lista_hora1.append(self.hora[i])
				lista_fecha1.append(self.fecha[i])
				mensaje.append(" thd mayor a  %d"%(regla2))
				if regla5 == 7:
					identifica_btn_11 = 5
					lista_armonico_11.append(Armonico_11[i]) 

				else:
					identifica_btn_11 = 4
					lista_armonico_1.append(armonico_1[i]) 
					lista_armonico_2.append(armonico_2[i]) 
					lista_armonico_3.append(armonico_3[i]) 
					lista_armonico_4.append(armonico_4[i]) 
					lista_armonico_5.append(armonico_5[i]) 
					lista_armonico_6.append(armonico_6[i]) 
					lista_armonico_7.append(armonico_7[i]) 
					lista_armonico_8.append(armonico_8[i]) 
					lista_armonico_9.append(armonico_9[i]) 
					lista_armonico_10.append(armonico_10[i]) 


			# Distorcion Armonica < a 20 debe tener un thd a  < 4
			if  distorcion_armonica[i]  >= 50 and distorcion_armonica[i] <100 and thd_a[i] > regla3:
				pos += i
				distorcion_4.append(distorcion_armonica[pos])
				pos = 0
				self.cont1 += 1
				lista_thd_alterado.append(thd_a[i])
				lista_hora1.append(self.hora[i])
				lista_fecha1.append(self.fecha[i])
				mensaje.append(" thd mayor a  %d"%(regla3))
				if regla5 == 7:
					identifica_btn_11 = 5
					lista_armonico_11.append(Armonico_11[i]) 

				else:
					identifica_btn_11 = 4
					lista_armonico_1.append(armonico_1[i]) 
					lista_armonico_2.append(armonico_2[i]) 
					lista_armonico_3.append(armonico_3[i]) 
					lista_armonico_4.append(armonico_4[i]) 
					lista_armonico_5.append(armonico_5[i]) 
					lista_armonico_6.append(armonico_6[i]) 
					lista_armonico_7.append(armonico_7[i]) 
					lista_armonico_8.append(armonico_8[i]) 
					lista_armonico_9.append(armonico_9[i]) 
					lista_armonico_10.append(armonico_10[i]) 

			# Distorcion Armonica < a 20 debe tener un thd a  < 4
			if  distorcion_armonica[i]  >= 100 and distorcion_armonica[i] < 1000 and thd_a[i] > regla4:
				pos += i
				distorcion_4.append(distorcion_armonica[pos])
				pos = 0
				self.cont1 += 1
				lista_thd_alterado.append(thd_a[i])
				lista_hora1.append(self.hora[i])
				lista_fecha1.append(self.fecha[i])
				mensaje.append(" thd mayor a  %d"%(regla4))
				if regla5 == 7:
					identifica_btn_11 = 5
					lista_armonico_11.append(Armonico_11[i]) 

				else:
					identifica_btn_11 = 4
					lista_armonico_1.append(armonico_1[i]) 
					lista_armonico_2.append(armonico_2[i]) 
					lista_armonico_3.append(armonico_3[i]) 
					lista_armonico_4.append(armonico_4[i]) 
					lista_armonico_5.append(armonico_5[i]) 
					lista_armonico_6.append(armonico_6[i]) 
					lista_armonico_7.append(armonico_7[i]) 
					lista_armonico_8.append(armonico_8[i]) 
					lista_armonico_9.append(armonico_9[i]) 
					lista_armonico_10.append(armonico_10[i]) 

			if  distorcion_armonica[i] >= 1000 and thd_a[i] > regla5:
				pos += i
				distorcion_4.append(distorcion_armonica[pos])
				pos = 0
				self.cont1 += 1
				lista_thd_alterado.append(thd_a[i])
				lista_hora1.append(self.hora[i])
				lista_fecha1.append(self.fecha[i])
				mensaje.append(" thd mayor a  %d "%(regla5))
				if regla5 == 7:
					identifica_btn_11 = 5
					lista_armonico_11.append(Armonico_11[i]) 
				
				else:
					identifica_btn_11 = 4
					lista_armonico_1.append(armonico_1[i]) 
					lista_armonico_2.append(armonico_2[i]) 
					lista_armonico_3.append(armonico_3[i]) 
					lista_armonico_4.append(armonico_4[i]) 
					lista_armonico_5.append(armonico_5[i]) 
					lista_armonico_6.append(armonico_6[i]) 
					lista_armonico_7.append(armonico_7[i]) 
					lista_armonico_8.append(armonico_8[i]) 
					lista_armonico_9.append(armonico_9[i]) 
					lista_armonico_10.append(armonico_10[i]) 

		self.llenarTablaVoltage(lista_hora1,lista_fecha1,distorcion_4,lista_thd_alterado,mensaje,identifica_btn_11,lista_armonico_11,lista_armonico_1,lista_armonico_2,lista_armonico_3,lista_armonico_4,lista_armonico_5,lista_armonico_6,lista_armonico_7,lista_armonico_8,lista_armonico_9,lista_armonico_10)	
		identifica_btn_11 = 0
		
		if self.cont1 > 0:
			self.informacionDatos(self.cont1)

		else:
			self.InformacionDatos0()

	def llenarTablaVoltage(self,lista_hora,lista_fecha,distorcion_armonica,thd_alterado,mensaje,identifica_btn_11,lista_armonico_11,lista_armonico_1,lista_armonico_2,lista_armonico_3,lista_armonico_4,lista_armonico_5,lista_armonico_6,lista_armonico_7,lista_armonico_8,lista_armonico_9,lista_armonico_10):
		index = 0
		self.cont=0
		self.list_ctrl.DeleteAllItems()

		self.eliminarColumnas()

		if identifica_btn_11 == 5:
			self.eliminarColumnas()
			self.list_ctrl.InsertColumn(5, 'Armonico 11 ',width=150)

		if identifica_btn_11 == 4:
			self.eliminarColumnas()
			self.list_ctrl.InsertColumn(5, 'Armonico 1 ',width=150)
			self.list_ctrl.InsertColumn(6, 'Armonico 2 ',width=150)
			self.list_ctrl.InsertColumn(7, 'Armonico 3 ',width=150)
			self.list_ctrl.InsertColumn(8, 'Armonico 4 ',width=150)
			self.list_ctrl.InsertColumn(9, 'Armonico 5 ',width=150)
			self.list_ctrl.InsertColumn(10, 'Armonico 6 ',width=150)
			self.list_ctrl.InsertColumn(11, 'Armonico 7 ',width=150)
			self.list_ctrl.InsertColumn(12, 'Armonico 8 ',width=150)
			self.list_ctrl.InsertColumn(13, 'Armonico 9 ',width=150)
			self.list_ctrl.InsertColumn(14, 'Armonico 10 ',width=150)

		for data in range(len(thd_alterado)):

			self.list_ctrl.InsertItem(index, str(lista_fecha[data]))
			self.list_ctrl.SetItem(index, 1, str(lista_hora[data]))
			self.list_ctrl.SetItem(index, 2, str(thd_alterado[data]))
			self.list_ctrl.SetItem(index, 3, str(distorcion_armonica[data]))
			self.list_ctrl.SetItem(index, 4, str(mensaje[data]))	

			if identifica_btn_11 == 5:
				self.list_ctrl.SetItem(index, 5, str(lista_armonico_11[data]))
			if identifica_btn_11 == 4:
				self.list_ctrl.SetItem(index, 5, str(lista_armonico_1[data]))
				self.list_ctrl.SetItem(index, 6, str(lista_armonico_2[data]))
				self.list_ctrl.SetItem(index, 7, str(lista_armonico_3[data]))
				self.list_ctrl.SetItem(index, 8, str(lista_armonico_4[data]))
				self.list_ctrl.SetItem(index, 9, str(lista_armonico_5[data]))
				self.list_ctrl.SetItem(index, 10, str(lista_armonico_6[data]))
				self.list_ctrl.SetItem(index, 11, str(lista_armonico_7[data]))
				self.list_ctrl.SetItem(index, 12, str(lista_armonico_8[data]))
				self.list_ctrl.SetItem(index, 13, str(lista_armonico_9[data]))
				self.list_ctrl.SetItem(index, 14, str(lista_armonico_10[data]))

			if index % 2:
				self.list_ctrl.SetItemBackgroundColour(index, "#F2F2F2")
			else:
				self.list_ctrl.SetItemBackgroundColour(index, "#ECF2F2")
			index += 1

	def eliminarColumnas(self):
			self.list_ctrl.DeleteColumn(5)
			self.list_ctrl.DeleteColumn(6)
			self.list_ctrl.DeleteColumn(7)
			self.list_ctrl.DeleteColumn(8)
			self.list_ctrl.DeleteColumn(9)
			self.list_ctrl.DeleteColumn(10)
			self.list_ctrl.DeleteColumn(11)
			self.list_ctrl.DeleteColumn(12)
			self.list_ctrl.DeleteColumn(13)
			self.list_ctrl.DeleteColumn(14)

	def informacionDatos(self, cont ):
		box = wx.MessageDialog(None, ('Se encontro %d datos'% cont), 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def InformacionDatos0(self):
		box = wx.MessageDialog(None, 'No se encontro nigun dato', 'Informacion', wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def footer(self):
		barra_estado = self.CreateStatusBar(1) # crear pie de pagina
		barra_estado.SetBackgroundColour('#6E7B99')
		barra_estado.SetStatusWidths([-1])
	
		barra_estado_fields = ["Todos los derechos reservados."]
		for i in range(len(barra_estado_fields)):
			barra_estado.SetStatusText(barra_estado_fields[i], i)