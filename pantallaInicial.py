#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import easygui
import pandas

from threading import *
import time

from Definiciones import *
import EfenergyGUI as GUI

class pantallaPrincipal(GUI.pantallaPrincipal):

	def __init__(self, parent, title):

		GUI.pantallaPrincipal.__init__(self, parent)
		self.construirUI()

	def construirUI( self ):

		self.archivo_voltaje = None
		
		self.last_path = None
		self.url_voltaje = None
		self.url_potencia = None
		self.url_armonico = None
		self.ultima_url_voltaje = None
		self.ultima_url_potencia = None
		self.ultima_url_armonico = None
		self.ruta_archivo_texto = ruta1
		#self.archivo_txt = ArchivoInformacion(self.ruta_archivo_texto)

		self.SetIcon(wx.Icon(logotipo1))
		self.m_statusBar01.SetStatusText(barra_estado_fields[0])

		self.m_panel01.Show(False)

    # this is the event we defined in wxformbuilder, and now override from gui.py

	def Salir( self, event ):

		self.Destroy()

	def CargarPlanilla( self, event ):

		self.m_button01.Bind(wx.EVT_BUTTON, self.OnSeleccionArchivo)
		self.m_panel01.Show(True)
		self.GetSizer().Layout()
		pass

	def OnSeleccionArchivo( self, event ):

		self.rango_mayor = float(127 + (127 * (10 / 100)))
		self.rango_menor = float(127 - (127 * (10 / 100))) 

		if self.last_path != None:
			
			self.last_path = self.last_path[0:self.last_path.rfind('\\')]
			self.last_path = self.last_path + '\\' + extension_xls[0]
		
		else:
			
			self.last_path = extension_xls[0]
		
		self.url_archivo = easygui.fileopenbox(msg=texto_abrir_xls, title=titulo_abrir_xls, default=self.last_path, filetypes=extension_xls)

		if self.url_archivo == None:

			if self.last_path.rfind('\\') != -1:

				self.last_path = self.last_path[0:self.last_path.rfind('\\')]
				self.last_path = self.last_path + '\\' + extension_xls[0]			

			else:

				self.last_path = extension_xls[0]

			pass

		else:

			try:

				self.url_voltaje = self.url_archivo
				
				self.preCargaArchivo( self.m_gauge01, self.m_textCtrl01 )
				self.archivo_voltaje = self.CargaArchivo( self.url_voltaje )		
				self.Update()
				wx.Yield()
				self.ultima_url_voltaje = self.posCargaArchivo( self.url_voltaje, self.m_gauge01, self.m_textCtrl01 )
				self.Update()
				wx.Yield()

				print( self.archivo_voltaje.sheet_names )

			except:

				self.url_voltaje = self.ultima_url_voltaje

	def preCargaArchivo( self, gauge, textctrl ):

		print('PreCarga')
		textctrl.SetValue( '' )
		textctrl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		gauge.SetValue( 0 )
		gauge.Pulse()
		
	def CargaArchivo( self, file_name ):

		print('Inicio carga archivo Excel')
		df_xlsx = pandas.ExcelFile( file_name )
		print('Final carga archivo Excel')
		return df_xlsx

	def posCargaArchivo( self, file_name, gauge, textctrl ):

		print('postCarga')
		gauge.SetValue( 100 )
		self.tituloArchivoCargado( file_name, textctrl )
		return file_name[0:file_name.rfind( '\\' )]
	
	def tituloArchivoCargado( self, url_archivo, textctrl ):

		textctrl.SetEditable( True )
		ruta_archivo = url_archivo.replace( "\\", "&" )
		separar_ruta_archivo = ruta_archivo.split( '&' )
		longitud_ruta_archivo = len( separar_ruta_archivo )
		textctrl.SetValue( separar_ruta_archivo[longitud_ruta_archivo-1] )
		textctrl.SetEditable( False )