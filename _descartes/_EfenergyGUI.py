# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class pantallaPrincipal
###########################################################################

class pantallaPrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Efenergy 2.0", pos = wx.DefaultPosition, size = wx.Size( 1100,640 ), style = wx.DEFAULT_FRAME_STYLE )

		self.SetSizeHints( wx.Size( 1100,640 ), wx.Size( 1100,640 ) )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer01 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel01 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,50 ), wx.TAB_TRAVERSAL )
		self.m_panel01.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		self.m_panel01.SetMinSize( wx.Size( -1,50 ) )
		self.m_panel01.SetMaxSize( wx.Size( -1,50 ) )

		bSizer02 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button01 = wx.Button( self.m_panel01, wx.ID_ANY, u"Seleccionar plantilla", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer02.Add( self.m_button01, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_gauge01 = wx.Gauge( self.m_panel01, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge01.SetValue( 0 )
		bSizer02.Add( self.m_gauge01, 0, wx.ALL|wx.EXPAND, 12 )

		self.m_textCtrl01 = wx.TextCtrl( self.m_panel01, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer02.Add( self.m_textCtrl01, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel01.SetSizer( bSizer02 )
		self.m_panel01.Layout()
		bSizer01.Add( self.m_panel01, 1, wx.EXPAND, 0 )

		self.m_panel02 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel02.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer01.Add( self.m_panel02, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer01 )
		self.Layout()
		self.m_menubar01 = wx.MenuBar( 0 )
		self.m_menubar01.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_menu01 = wx.Menu()
		self.m_menuItem01 = wx.MenuItem( self.m_menu01, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu01.Append( self.m_menuItem01 )

		self.m_menubar01.Append( self.m_menu01, u"Aplicación" )

		self.m_menu02 = wx.Menu()
		self.m_menuItem02 = wx.MenuItem( self.m_menu02, wx.ID_ANY, u"Cargar plantilla", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu02.Append( self.m_menuItem02 )

		self.m_menu02.AppendSeparator()

		self.m_menuItem03 = wx.MenuItem( self.m_menu02, wx.ID_ANY, u"Analizar voltaje", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu02.Append( self.m_menuItem03 )

		self.m_menu02.AppendSeparator()

		self.m_menuItem04 = wx.MenuItem( self.m_menu02, wx.ID_ANY, u"Norma de referencia", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu02.Append( self.m_menuItem04 )

		self.m_menubar01.Append( self.m_menu02, u"Voltaje" )

		self.m_menu03 = wx.Menu()
		self.m_menuItem05 = wx.MenuItem( self.m_menu03, wx.ID_ANY, u"Cargar plantilla", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu03.Append( self.m_menuItem05 )

		self.m_menu03.AppendSeparator()

		self.m_menuItem06 = wx.MenuItem( self.m_menu03, wx.ID_ANY, u"Analizar Factor de Potencia", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu03.Append( self.m_menuItem06 )

		self.m_menuItem07 = wx.MenuItem( self.m_menu03, wx.ID_ANY, u"Analizar Potencia Reactiva", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu03.Append( self.m_menuItem07 )

		self.m_menu03.AppendSeparator()

		self.m_menuItem08 = wx.MenuItem( self.m_menu03, wx.ID_ANY, u"Norma de referencia", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu03.Append( self.m_menuItem08 )

		self.m_menubar01.Append( self.m_menu03, u"Potencia" )

		self.m_menu04 = wx.Menu()
		self.m_menuItem09 = wx.MenuItem( self.m_menu04, wx.ID_ANY, u"Cargar plantilla", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu04.Append( self.m_menuItem09 )

		self.m_menu04.AppendSeparator()

		self.m_menuItem10 = wx.MenuItem( self.m_menu04, wx.ID_ANY, u"Analizar Armónicos de Tensión", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu04.Append( self.m_menuItem10 )

		self.m_menuItem11 = wx.MenuItem( self.m_menu04, wx.ID_ANY, u"Analizar Armónicos de Corriente", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu04.Append( self.m_menuItem11 )

		self.m_menu04.AppendSeparator()

		self.m_menuItem12 = wx.MenuItem( self.m_menu04, wx.ID_ANY, u"Norma de referencia", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu04.Append( self.m_menuItem12 )

		self.m_menubar01.Append( self.m_menu04, u"Armónicos" )

		self.m_menu05 = wx.Menu()
		self.m_menuItem13 = wx.MenuItem( self.m_menu05, wx.ID_ANY, u"Acerca de Efenergy", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu05.Append( self.m_menuItem13 )

		self.m_menu05.AppendSeparator()

		self.m_submenu01 = wx.Menu()
		self.m_menuItem14 = wx.MenuItem( self.m_submenu01, wx.ID_ANY, u"Voltaje", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_submenu01.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.m_submenu01, wx.ID_ANY, u"Potencia", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_submenu01.Append( self.m_menuItem15 )

		self.m_menuItem16 = wx.MenuItem( self.m_submenu01, wx.ID_ANY, u"Armónicos", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_submenu01.Append( self.m_menuItem16 )

		self.m_menu05.AppendSubMenu( self.m_submenu01, u"Gestión de las normas de referencia" )

		self.m_menubar01.Append( self.m_menu05, u"Opciones" )

		self.SetMenuBar( self.m_menubar01 )

		self.m_statusBar01 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button01.Bind( wx.EVT_BUTTON, self.OnSeleccionArchivo )
		self.Bind( wx.EVT_MENU, self.Salir, id = self.m_menuItem01.GetId() )
		self.Bind( wx.EVT_MENU, self.CargarPlanilla, id = self.m_menuItem02.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnSeleccionArchivo( self, event ):
		pass

	def Salir( self, event ):
		pass

	def CargarPlanilla( self, event ):
		pass


