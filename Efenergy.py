#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import ctypes

from inicio import Aplicacion

from Definiciones import *

#-------------------------------------------------------------------------------------------------

class Menu:

	def main(self, argv=None):

		#-------------------------------------------------------------------------------------------------

		shell32 = ctypes.windll.shell32
		app = wx.App()

		if argv is None and shell32.IsUserAnAdmin():

			frame = Aplicacion(-1, nombreAplicacion)
			frame.Centre()
			frame.Show()
			app.MainLoop()

		else:

			box = wx.MessageDialog(None, mensajeAdministrador, titulo_error, style=wx.ICON_ERROR|wx.OK)
			answer = box.ShowModal()
			box.Destroy()

		#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':

	menu = Menu()
	menu.main()

#-------------------------------------------------------------------------------------------------
