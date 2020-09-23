# -*- coding: utf-8 -*-

import wx
import wx.adv

class VentanaInformacion():

    def informacion(self):

        descripcion = """\nEfernergy es un sistema de análisis de variables eléctricas para el sistema 
operativo Windows. Dicho análisis incluye una serie de opciones con la 
que el usuario puede interactuar, entre estas opciones se encuentra:
Graficar datos, Guardar datos en Excel, Listar Datos
"""

        integrantes_semillero = ['Semillero Eficiencia Energetica:','\n\nAndres Tafur Piedrahita','\nViviana Ramirez Ramirez']


        info = wx.adv.AboutDialogInfo()

        info.SetIcon(wx.Icon('imagenes/logo_sena.png', wx.BITMAP_TYPE_PNG))
        info.SetName('EFENERGY')
        info.SetVersion('1.0')
        info.SetDescription(descripcion)
        info.SetCopyright('(C) 2019 Centro de Diseño e Innovación Tecnológica Industrial')
        #info.SetWebSite('http://www.zetcode.com')
        #info.SetLicence(licence)
        info.AddDeveloper('Wendy Vanessa Mejia Agudelo\nDiego Alexander Sepulveda Garcia')
        info.SetArtists(integrantes_semillero)

        #info.AddArtist('The Tango crew')
        #info.AddTranslator('Jan Bodnar')

        wx.adv.AboutBox(info)

