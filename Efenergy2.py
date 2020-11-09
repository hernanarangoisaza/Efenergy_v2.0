#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import ctypes
from Definiciones import *
import pantallaInicial as pInicial

class Aplicacion(wx.App):

    def OnInit(self):

        # Mejorar la nitidez y resolución de la aplicación. Se ve pequeño en monitores de alta resolución como 4K.
        # ctypes.windll.shcore.SetProcessDpiAwareness(2)

        self.frame = pInicial.pantallaPrincipal(None, nombreAplicacion)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True

if __name__ == "__main__":

    app = Aplicacion(redirect=False) 

    #print(wx.GetDisplaySize())  # returns a tuple

    app.MainLoop()