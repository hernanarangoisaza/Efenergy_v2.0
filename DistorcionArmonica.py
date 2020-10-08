#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx
import numpy
import wx.grid
import pandas

from AnalisisDistorcionArmonica import AnalisisDistorcionArmonica

class DistorcionArmonica(wx.Frame):
	def __init__(self, id, title,archivo):
		self.id = id 
		self.archivo_excel = archivo

		self.frame = wx.Frame.__init__(self, None, id, title, size = (200,50), style = wx.DEFAULT_FRAME_STYLE 
			& ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)) # bloquear boton de maximizar

		self.panel = wx.Panel(self, -1)
		self.Elementos()

	# Elementos quecomponen el frame principal
	def Elementos(self):
		# Create text input
		dlg = wx.TextEntryDialog(self.frame, 'máxima corriente de cortocircuito en el PCC','PCC')
		dlg.SetValue("50000")
		
		try:
			if dlg.ShowModal() == wx.ID_OK:
				pcc = int(dlg.GetValue())
				print(pcc)
				self.OnViewDistorcionArmonica(pcc)
			self.Destroy()
		except ValueError:
			self.Destroy()

	def OnViewDistorcionArmonica(self,pcc):
		app = wx.App()
		frame = AnalisisDistorcionArmonica(self.id, 'Tabla de Datos', self.archivo_excel,pcc)
		frame.Centre()
		frame.Show()
		app.MainLoop()
		
