#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import wx.adv

from Definiciones import *

class VentanaInformacion():

    def informacion(self):

		#-------------------------------------------------------------------------------------------------

        info = wx.adv.AboutDialogInfo()

        info.SetName(nombreApp)
        info.SetVersion(versionApp)
        info.SetDescription(descripcion)
        info.SetCopyright(copy_right)
        info.AddDeveloper(desarrolladores)
        info.SetDocWriters(integrantes_semillero)

        wx.adv.AboutBox(info)

		#-------------------------------------------------------------------------------------------------
