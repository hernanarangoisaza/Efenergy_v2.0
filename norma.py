#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx

class Norma(wx.Frame):
	def __init__(self, id, title):
		self.frame = wx.Frame.__init__(self, None, id, title, size = (972, 288), style = wx.DEFAULT_FRAME_STYLE )
		
		panel= wx.Panel(self,-1,size=(1500, 100),pos=(0,0))
		img_cuadro_norma = 'images/cuadro_distorsion_armonica.JPG'
		bmp1 = wx.Image(img_cuadro_norma, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
		cuadro_norma = wx.StaticBitmap(panel, -1, bmp1, (0, 0))