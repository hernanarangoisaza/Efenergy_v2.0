#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import easygui as eg
import pandas as pd
from hilo_trabajo_barra_espera import WorkerThread
from AnalisisDatosVoltaje import AnalisisDatosVoltaje
from AnalisisDatosPotencia import AnalisisDatosPotencia
from AnalisisDatosPotenciaReactiva import AnalisisDatosPotenciaReactiva
from AnalisisDatosArmonicos import AnalisisDatosArmonicos
from AnalisisDatosArmonicosCorriente import AnalisisDatosArmonicosCorriente
from ArchivoInformacion import ArchivoInformacion
from EditarInformacion import EditarInformacion

class Aplicacion(wx.Frame):
	def __init__(self, id, title):
		self.frame = wx.Frame.__init__(self, None, id, title, size = (1000, 700),pos=(0,0), style = wx.DEFAULT_FRAME_STYLE)
		self.SetBackgroundColour("#6E7B99")

		self.url_voltaje = None
		self.url_potencia = None
		self.url_armonico = None
		self.ultima_url_voltaje = None
		self.ultima_url_potencia = None
		self.ultima_url_armonico = None

		self.ruta_archivo_texto = "archivo\informacion.txt"
		self.archivo_txt = ArchivoInformacion(self.ruta_archivo_texto)
		self.SetIcon(wx.Icon("Images/logo.png"))
		self.Elementos()
		self.footer()

	def Elementos(self):
		# --------------------------- / -----------------------------------
		header= wx.Panel(self,-1,size=(1000,100),pos=(0,0))
		header.SetBackgroundColour("#6E7B99")
		
		logotipo = 'images/logotipo.JPG'
		bmp1 = wx.Image(logotipo, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(header, -1, bmp1, (30,5))

		titulo = wx.StaticText(header, wx.ID_ANY, "Efenergy", style=wx.ALIGN_CENTER, pos=(150,25))
		font = wx.Font(40, wx.ROMAN, wx.ITALIC, wx.NORMAL)
		titulo.SetFont(font)

		# --------------------------- / -----------------------------------
		panel= wx.Panel(self,-1,size=(1000,700),pos=(8,110))

		notebook = wx.Notebook(panel, size=(970,500))
		notebook.SetBackgroundColour('#6E7B99')
		self.page_1 = wx.Panel(notebook)
		self.page_1.SetBackgroundColour('#F5F7F7')
		self.page_2 = wx.Panel(notebook)
		self.page_2.SetBackgroundColour('#F5F7F7')
		self.page_3 = wx.Panel(notebook)
		self.page_3.SetBackgroundColour('#F5F7F7')

		notebook.AddPage(self.page_1, "Voltaje")
		notebook.AddPage(self.page_2, "Potencia")
		notebook.AddPage(self.page_3, "Armónicos")
		
		# --------------------------- / -----------------------------------
		self.panel_informacion_voltage= wx.Panel(self.page_1,-1,size=(880,200),pos=(20,85))
		self.panel_informacion_voltage.SetBackgroundColour("#FFFFFF")

		self.panel_informacion_potencia= wx.Panel(self.page_2,-1,size=(880,200),pos=(20,85))
		self.panel_informacion_potencia.SetBackgroundColour("#FFFFFF")

		self.panel_informacion_armonico= wx.Panel(self.page_3,-1,size=(880,200),pos=(20,85))
		self.panel_informacion_armonico.SetBackgroundColour("#FFFFFF")

		# --------------------------- / -----------------------------------
		
		self.componentesComunes(self.page_1,self.panel_informacion_voltage,"VOLTAJE ",1,4)
		self.componentesComunes(self.page_2,self.panel_informacion_potencia,"POTENCIA ",2,5)
		self.componentesComunes(self.page_3,self.panel_informacion_armonico,"ARMÓNICOS ",3,6)

		btn_analizar_voltaje = wx.Button(self.page_1, 4, u"Analizar voltaje", size=(200,30), pos=(700,400))
		btn_analizar_voltaje.Bind(wx.EVT_BUTTON, self.OnViewTableVoltageMayor)

		btn_analizar_factor_potencia = wx.Button(self.page_2, 5, u"Analizar factor de potencia", size=(300,30), pos=(295,400))
		btn_analizar_factor_potencia.Bind(wx.EVT_BUTTON, self.OnViewTableVoltageMayor)

		btn_analizar_potencia_reactiva = wx.Button(self.page_2, 6, u"Analizar potencia reactiva", size=(300,30), pos=(600,400))
		btn_analizar_potencia_reactiva.Bind(wx.EVT_BUTTON, self.OnViewTableVoltageMayor)

		btn_analizar_armonicos_tension = wx.Button(self.page_3, 7, u"Analizar armónicos de tensión", size=(300,30), pos=(295,400))
		btn_analizar_armonicos_tension.Bind(wx.EVT_BUTTON, self.OnViewTableVoltageMayor)

		btn_analizar_armonicos_corriente = wx.Button(self.page_3, 8, u"Analizar armónicos de corrente", size=(300,30), pos=(600,400))
		btn_analizar_armonicos_corriente.Bind(wx.EVT_BUTTON, self.OnViewTableVoltageMayor)

		btn_pdf = wx.BitmapButton(self.panel_informacion_voltage, 9, wx.Bitmap( u"Images/pdf5.png",wx.BITMAP_TYPE_ANY),(800,10),wx.DefaultSize,wx.NO_BORDER)	
		btn_pdf.SetBitmapCurrent( wx.Bitmap( u"Images/pdf4.png",wx.BITMAP_TYPE_ANY))
		btn_pdf.SetBackgroundColour('#FFFFFF')
		btn_pdf.Bind(wx.EVT_BUTTON, self.abrirPDF)

		btn_pdf = wx.BitmapButton(self.panel_informacion_potencia, 10, wx.Bitmap( u"Images/pdf5.png",wx.BITMAP_TYPE_ANY),(800,10),wx.DefaultSize,wx.NO_BORDER)	
		btn_pdf.SetBitmapCurrent( wx.Bitmap( u"Images/pdf4.png",wx.BITMAP_TYPE_ANY))
		btn_pdf.SetBackgroundColour('#FFFFFF')
		btn_pdf.Bind(wx.EVT_BUTTON, self.abrirPDF)

		btn_pdf = wx.BitmapButton(self.panel_informacion_armonico, 11, wx.Bitmap( u"Images/pdf5.png",wx.BITMAP_TYPE_ANY),(800,10),wx.DefaultSize,wx.NO_BORDER)	
		btn_pdf.SetBitmapCurrent( wx.Bitmap( u"Images/pdf4.png",wx.BITMAP_TYPE_ANY))
		btn_pdf.SetBackgroundColour('#FFFFFF')
		btn_pdf.Bind(wx.EVT_BUTTON, self.abrirPDF)
	
		# --------------------------- / -----------------------------------
		menubar = wx.MenuBar(0)
		menu = wx.Menu()
		menuItem3 = wx.MenuItem(menu, wx.ID_ANY, u"Salir\tCTRL+Q",u"Salir de Efenergy",  wx.ITEM_NORMAL )
		menuItem3.SetBitmap(wx.Bitmap(u"Images/cerrar.png", wx.BITMAP_TYPE_ANY ))
		self.Bind(wx.EVT_MENU, self.salir, menuItem3)
		menu.Append(menuItem3)
		menu.AppendSeparator()

		menu2 = wx.Menu()
		menu2Item = wx.MenuItem(menu, wx.ID_ANY, u"About...\tF1", u"Acerca de Efenergy", wx.ITEM_NORMAL )
		menu2Item.SetBitmap(wx.Bitmap(u"Images/acerca_de.png", wx.BITMAP_TYPE_ANY ))
		self.Bind(wx.EVT_MENU, self.informacion, menu2Item)
		menu2.Append(menu2Item)

		menubar.Append(menu, u"Archivo" )
		menubar.Append(menu2, u"Ayuda" ) 

		self.SetMenuBar(menubar)
		# ---------------------------/--------------------------------------------

	def componentesComunes(self,ubicacion,panel,nombre,identificador_btn1,identificador_btn2):
		if identificador_btn1 == 1:
			self.txt_informacion_voltaje = wx.StaticText(panel, -1, self.cargar_informacion()[0], pos=(40, 30), size=(700,150),style=wx.ST_NO_AUTORESIZE)
			font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
			self.txt_informacion_voltaje.SetFont(font)

		if identificador_btn1 == 2:
			self.txt_informacion_potencia = wx.StaticText(panel, -1, self.cargar_informacion()[1], pos=(40, 30), size=(700,150),style=wx.ST_NO_AUTORESIZE)
			font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
			self.txt_informacion_potencia.SetFont(font)
		if identificador_btn1 == 3:
			self.txt_informacion_armonico = wx.StaticText(panel, -1, self.cargar_informacion()[2], pos=(40, 30), size=(700,150),style=wx.ST_NO_AUTORESIZE)
			font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
			self.txt_informacion_armonico.SetFont(font)

		button_editar_informacion = wx.BitmapButton(panel, identificador_btn1, wx.Bitmap(u"Images/icono_editar.png"), pos=(835,10), size=wx.DefaultSize, style=wx.BU_AUTODRAW|wx.NO_BORDER )
		button_editar_informacion.SetBackgroundColour("#FFFFFF")
		button_editar_informacion.Bind(wx.EVT_BUTTON, self.on_editar_informacion)

		decoracion_derecha1_panel_informacion= wx.Panel(panel,-1,size=(200,5),pos=(0,0))
		decoracion_derecha1_panel_informacion.SetBackgroundColour("#6CFFCD")

		decoracion_derecha2_panel_informacion= wx.Panel(panel,-1,size=(5,100),pos=(0,0))
		decoracion_derecha2_panel_informacion.SetBackgroundColour("#6CFFCD")
		
		decoracion_izquierda1_panel_informacion= wx.Panel(panel,-1,size=(200,5),pos=(680,195))
		decoracion_izquierda1_panel_informacion.SetBackgroundColour("#6CFFCD")

		decoracion_izquierda2_panel_informacion= wx.Panel(panel,-1,size=(5,100),pos=(875,100))
		decoracion_izquierda2_panel_informacion.SetBackgroundColour("#6CFFCD")

		icon_seleccionar_archivo = 'images/archivo.png'
		bmp1 = wx.Image(icon_seleccionar_archivo, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		self.bitmap1 = wx.StaticBitmap(ubicacion, -1, bmp1, (225, 11))

		btn_seleccionar_archivo = wx.Button(ubicacion, identificador_btn1, u"Seleccionar Archivo", size=(200,30), pos=(20,10))
		btn_seleccionar_archivo.Bind(wx.EVT_BUTTON, self.OnSeleccionArchivo)

		txt_voltaje = wx.StaticText(ubicacion, wx.ID_ANY, nombre, pos=(30,55))
		font = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		txt_voltaje.SetFont(font)
		
	def informacion(self,event):
		from VentanaInformacion import VentanaInformacion
		informacion_semillero = VentanaInformacion()
		informacion_semillero.informacion()

	def salir(self,event):
		self.Destroy()

	def on_editar_informacion(self, event):
		try:
			identificador = event.GetId()
			self.validacion_clave(identificador)
		except ValueError:
			print("Error Validando Clave")
	
	def validacion_clave(self, identificador):
		clave = "1234"
		dlg = wx.PasswordEntryDialog(self.frame, 'Ingrese Clave de Validación','Validar Clave',style=wx.TextEntryDialogStyle)
		if dlg.ShowModal() == wx.ID_OK:
			clave_digitada = dlg.GetValue()
			if clave_digitada == clave:
				app = wx.App()
				if identificador == 1:
					frame = EditarInformacion(-1, 'Editar Información de Voltaje', self.cargar_informacion()[0], self.archivo_txt, self, identificador)
				if identificador == 2:
					frame = EditarInformacion(-1, 'Editar Información de Potencia', self.cargar_informacion()[1], self.archivo_txt, self, identificador)
				if identificador == 3:
					frame = EditarInformacion(-1, 'Editar Información de Armónicos', self.cargar_informacion()[2], self.archivo_txt, self, identificador)
				
				frame.Centre()
				frame.Show()
				app.MainLoop()

			else:
				self.msgError("Clave Incorrecta")
				self.validacion_clave(identificador)

	def cargar_informacion(self):
		informacion = self.archivo_txt.leer_archivo()
	
		return informacion

	def abrirPDF(self,event):
		import webbrowser as wb
		identificador = event.GetId()

		if identificador == 9:
			wb.open_new(u'archivo\\NormaVoltaje.pdf')

		elif identificador == 10:
			wb.open_new(u'archivo\\NormaPotencia.pdf')

		elif identificador == 11:
			wb.open_new(u'archivo\\NormaArmónico.pdf')


	def OnSeleccionArchivo(self, event):
		self.rango_mayor = float(127 + (127 * (10 / 100)))
		self.rango_menor = float(127 - (127 * (10 / 100))) 
		
		extension = ["*.xlsx","*.xls"]
		
		self.url_archivo = eg.fileopenbox(msg="Abrir archivo de Excel", title="Control", default=extension[0], filetypes=extension)
		if self.url_archivo == None:
			pass
		else:
			self.OnRunButton()

		identificador = event.GetId()
		try:
			if identificador == 1:
				self.url_voltaje = self.url_archivo
				self.archivo_voltaje= pd.ExcelFile(self.url_voltaje)
				self.tituloArchivo(self.url_voltaje,self.page_1)
		
				self.ultima_url_voltaje = self.url_voltaje

			if identificador == 2:
				self.url_potencia = self.url_archivo
				self.archivo_potencia = pd.ExcelFile(self.url_potencia)
				self.tituloArchivo(self.url_potencia,self.page_2)

				self.ultima_url_potencia = self.url_potencia

			if identificador == 3:
				self.url_armonico = self.url_archivo
				self.archivo_armonico = pd.ExcelFile(self.url_armonico)
				self.tituloArchivo(self.url_armonico,self.page_3)

				self.ultima_url_armonico = self.url_armonico
		except:
			self.url_voltaje = self.ultima_url_voltaje
			self.url_potencia = self.ultima_url_potencia
			self.url_armonico = self.ultima_url_armonico
			print("No se selecciono el archivo")

	def tituloArchivo(self,url_archivo,ubicacion):
		ruta_archivo = url_archivo.replace("\\", "&")
		separar_ruta_archivo = ruta_archivo.split('&')
		longitud_ruta_archivo = len(separar_ruta_archivo)

		nombre_archivo = wx.StaticText(ubicacion, wx.ID_ANY, separar_ruta_archivo[longitud_ruta_archivo-1], pos=(260,17))
		font1 = wx.Font(11, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		nombre_archivo.SetFont(font1)

	def OnViewTableVoltageMayor(self, event):
		identificador = event.GetId()
		
		app = wx.App()

		if identificador == 4:
			if self.url_voltaje != None:
				frame = AnalisisDatosVoltaje(-1, 'Analizar Voltaje', self.archivo_voltaje )
				frame.Centre()
				frame.Show()
			else:
				self.msgError("ERROR Seleccionar archivo")

		if identificador == 5:
			if self.url_potencia != None:
				frame = AnalisisDatosPotencia(-1, 'Analizar Factor de Potencia', self.archivo_potencia )
				frame.Centre()
				frame.Show()
			else:
				self.msgError("ERROR Seleccionar archivo")

		if identificador == 6:
			if self.url_potencia != None:
				frame = AnalisisDatosPotenciaReactiva(-1, 'Analizar Potencia reactiva', self.archivo_potencia )
				frame.Centre()
				frame.Show()
			else:
				self.msgError("ERROR Seleccionar archivo")

		if identificador == 7:
			if self.url_armonico != None:
				frame = AnalisisDatosArmonicos(-1, 'Analisis armónicos de tensión',self.archivo_armonico)
				frame.Centre()
				frame.Show()
			else:
				self.msgError("ERROR Seleccionar archivo")

		if identificador == 8:
			if self.url_armonico != None:
				frame = AnalisisDatosArmonicosCorriente(-1, 'Analizar armónicos de corriente', self.archivo_armonico )	
				frame.Centre()
				frame.Show()
			else:
				self.msgError("ERROR Seleccionar archivo")

		app.MainLoop()
	
	def OnRunButton(self):
		self.progressDialog = wx.ProgressDialog("Cargando Archivo...",
							"Cargando Archivo...",
							maximum=WorkerThread.MAX_COUNT, parent=self,
							style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
		
		self.worker(self.threadCallback)
		self.progressDialog.ShowModal()
		self.progressDialog.Layout()

	def worker(self, callback):
		thread = WorkerThread(callback)
		thread.start()

	def threadCallback(self, info):

		if info == -1:
			self.progressDialog.Destroy()
		else:
			self.progressDialog.Update(info)
			
	def msgError(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'ERROR',style=wx.ICON_ERROR | wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def footer(self):
		barra_estado = self.CreateStatusBar(1) # crear pie de pagina
		barra_estado.SetStatusWidths([-1])
	
		barra_estado_fields = ["Todos los derechos reservados."]
		for i in range(len(barra_estado_fields)):
			barra_estado.SetStatusText(barra_estado_fields[i], i)
