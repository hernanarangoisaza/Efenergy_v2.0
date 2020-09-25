#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import easygui as eg

from ArchivoInformacion import ArchivoInformacion
from Definiciones import *

class EditarInformacion(wx.Frame):

	def __init__(self, id, title, informacion, archivo_txt, ventana_inicio, identificador):

		# ---------------------------/--------------------------------------------

		wx.Frame.__init__(self, None, id, title, size=size9, pos=(0,0), style=style4)
		
		self.ventana_inicio = ventana_inicio
		self.SetIcon(wx.Icon(logotipo1))
		self.panel = wx.Panel(self, -1)
		self.archivo_txt = archivo_txt
		self.informacion = informacion
		self.identificador = identificador
		self.SetBackgroundColour(blanco)
		self.elementos()

		# ---------------------------/--------------------------------------------

	def elementos(self):

		# ---------------------------/--------------------------------------------

		# HEADER VENTANA EDICIÓN DE INFORMACIÓN DE LA NORMA
		
		panel = wx.Panel(self.panel, -1, size=size10, pos=wx.DefaultPosition)

		txt_informacion = wx.StaticText(panel, -1, texto_edicion%nombre_variable[self.identificador-1], pos=(10, 10))
		font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
		txt_informacion.SetFont(font)
		txt_informacion.SetForegroundColour(negro)
		panel.SetBackgroundColour(gris2)

		# ZONA CAMBIAR PDF DE LA NORMA
		
		txt_editar_norma = wx.StaticText(self.panel, -1, texto_cambiar_pdf, pos=(650,70))
		font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
		txt_editar_norma.SetFont(font)

		button_seleccionar = wx.Button(self.panel, -1, texto_seleccionar_norma, size=size11, pos=(680,100))
		button_seleccionar.Bind(wx.EVT_BUTTON, self.on_seleccion_norma)

		self.button_cargar = wx.Button(self.panel, -1, texto_cargar, size=size11, pos=(680,140))
		self.button_cargar.Show(False)
		self.button_cargar.Bind(wx.EVT_BUTTON, self.cargar_norma)

		linea_separador = wx.StaticLine(self.panel, id=wx.ID_ANY, pos=(640,65), size=(2,240), style=wx.LI_VERTICAL)
		linea_separador.SetBackgroundColour(gris1)

		font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
		self.inp_informacion = wx.TextCtrl(self.panel, wx.ID_ANY, self.informacion, size=size12, pos=(30,70), style=wx.TE_MULTILINE)
		self.inp_informacion.SetFont(font)
		
		button_editar = wx.BitmapButton(self.panel, wx.ID_ANY, wx.Bitmap(icono_aceptar), pos=(600,275), size=wx.DefaultSize, style=wx.BU_AUTODRAW|wx.NO_BORDER)
		button_editar.SetBackgroundColour(blanco)
		button_editar.Bind(wx.EVT_BUTTON, self.on_editar_informacion)

		button_cancelar = wx.BitmapButton(self.panel, wx.ID_ANY, wx.Bitmap(icono_cancelar), pos=(550,275), size=wx.DefaultSize, style=wx.BU_AUTODRAW|wx.NO_BORDER)
		button_cancelar.SetBackgroundColour(blanco)
		button_cancelar.Bind(wx.EVT_BUTTON, self.on_cancelar)

		# ---------------------------/--------------------------------------------

	def on_editar_informacion(self, event):

		# ---------------------------/--------------------------------------------

		# EDITAR INFORMACIÓN SOBRE LA NORMA
		
		try:

			confirmacion = self.msgPregunta(texto_guardar)

			if confirmacion == wx.ID_YES:

				informacion = self.archivo_txt.leer_archivo()

				if self.identificador == 1:

					total_informacion = "%s\n&%s\n&%s" % (self.inp_informacion.GetValue(), informacion[1], informacion[2])
					self.archivo_txt.escribir_archivo(total_informacion)
					self.ventana_inicio.txt_informacion_voltaje.SetLabel(self.archivo_txt.leer_archivo()[0])

				if self.identificador == 2:

					total_informacion = "%s\n&%s\n&%s" % (informacion[0], self.inp_informacion.GetValue(), informacion[2])
					self.archivo_txt.escribir_archivo(total_informacion)
					self.ventana_inicio.txt_informacion_potencia.SetLabel(self.archivo_txt.leer_archivo()[1])

				if self.identificador == 3:

					total_informacion = "%s\n&%s\n&%s" % (informacion[0], informacion[1], self.inp_informacion.GetValue())
					self.archivo_txt.escribir_archivo(total_informacion)
					self.ventana_inicio.txt_informacion_armonico.SetLabel(self.archivo_txt.leer_archivo()[2])

				self.msgInformacion(texto_modificado_ok)
				self.Destroy()

		except:

			self.msgError(texto_modificado_error)

		# ---------------------------/--------------------------------------------

	def on_seleccion_norma(self, event):

		# ---------------------------/--------------------------------------------

		# SELECCIONAR EL PDF ASOCIADO A LA NORMA

		try:

			extension = ["*.pdf"]
			a = None 
			self.archivo = eg.fileopenbox(msg=texto_seleccionar_pdf, title=titulo_norma, default=extension[0], filetypes=extension)
			
			if self.archivo != None:

				self.button_cargar.Show(True)

			else:

				self.button_cargar.Show(False)

		except:

			self.msgError(texto_seleccionar_pdf_error)

		# ---------------------------/--------------------------------------------

	def cargar_norma(self, event):

		# ---------------------------/--------------------------------------------

		# CARGAR EL PDF ASOCIADO A LA NORMA

		try:

			import shutil

			if self.identificador == 1:

				shutil.copy(self.archivo, ruta_pdf_voltaje)

			if self.identificador == 2:

				shutil.copy(self.archivo, ruta_pdf_potencia)

			if self.identificador == 3:

				shutil.copy(self.archivo, ruta_pdf_armonicos)

			self.msgInformacion(texto_cargar_pdf_ok)
			self.button_cargar.Show(False)

		except:

			self.msgError(texto_cargar_pdf_error)

		# ---------------------------/--------------------------------------------

	def on_cancelar(self, event):

		# ---------------------------/--------------------------------------------

		# DESCARTAR CAMBIOS EN EL TEXTO ASOCIADO A LA NORMA

		confirmacion = self.msgPregunta(texto_cancelar_operacion)

		if confirmacion == wx.ID_YES:

			self.Destroy()

		# ---------------------------/--------------------------------------------

	def msgInformacion(self, mensaje):

		# ---------------------------/--------------------------------------------

		# MENSAJE DE DIÁLOGO PARA INFORMACIÓN

		box = wx.MessageDialog(None, mensaje, titulo_informacion, style=wx.ICON_INFORMATION|wx.OK)
		answer = box.ShowModal()
		box.Destroy()

		# ---------------------------/--------------------------------------------

	def msgError(self, mensaje):

		# ---------------------------/--------------------------------------------

		# MENSAJE DE DIÁLOGO PARA ERROR

		box = wx.MessageDialog(None, mensaje, titulo_error, style=wx.ICON_ERROR|wx.OK)
		answer = box.ShowModal()
		box.Destroy()

		# ---------------------------/--------------------------------------------

	def msgPregunta(self, mensaje):

		# ---------------------------/--------------------------------------------
		
		# MENSAJE DE DIÁLOGO PARA CONFIRMACIÓN

		box = wx.MessageDialog(None, mensaje, titulo_confirmacion, style=wx.ICON_QUESTION|wx.YES_NO)
		answer = box.ShowModal()
		box.Destroy()

		return answer

		# ---------------------------/--------------------------------------------
