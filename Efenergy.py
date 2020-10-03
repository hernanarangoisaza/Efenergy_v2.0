#!/usr/bin/env python3

import wx
import ctypes
from inicio import Aplicacion

class Menu:

	def main(self, argv=None):

		shell32 = ctypes.windll.shell32
		app = wx.App()

		if argv is None and shell32.IsUserAnAdmin():

			frame = Aplicacion(-1, 'Efenergy')
			frame.Centre()
			frame.Show()
			app.MainLoop()

		else:

			box = wx.MessageDialog(None, "Ejecute la Aplicación como Administrador", 'Error', style=wx.ICON_ERROR|wx.OK)
			answer = box.ShowModal()
			box.Destroy()

if __name__ == '__main__':

	menu = Menu()
	menu.main()