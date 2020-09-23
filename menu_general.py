import wx
import easygui as eg
from VentanaInformacion import VentanaInformacion

class Menu2:
	def menugeneral(self,opt_general,archivo_excel):
		self.archivo_excel = archivo_excel 
		self.opt_general = opt_general
		self.menubar = wx.MenuBar(0)
		self.menu = wx.Menu()

		self.menu.AppendSeparator()

		menuItem3 = wx.MenuItem(self.menu, wx.ID_ANY, u"Salir\tCTRL+Q",u"Salir de Efenergy", wx.ITEM_NORMAL )
		menuItem3.SetBitmap(wx.Bitmap(u"imagenes/atras.png", wx.BITMAP_TYPE_ANY ))
		opt_general.Bind(wx.EVT_MENU, self.salir, menuItem3)
		self.menu.Append(menuItem3)

		menu2 = wx.Menu()
		menu2Item = wx.MenuItem(self.menu, wx.ID_ANY, u"About...\tF1", u"Acerca de Efenergy", wx.ITEM_NORMAL )
		menu2Item.SetBitmap(wx.Bitmap(u"imagenes/acerca_de.png", wx.BITMAP_TYPE_ANY ))
		opt_general.Bind(wx.EVT_MENU, self.informacion, menu2Item)
		menu2.Append(menu2Item)

		self.menubar.Append(self.menu, u"Archivo" )
		self.menubar.Append(menu2, u"Ayuda" ) 
		
		opt_general.SetMenuBar(self.menubar)

	def opt_ir_atras(self,opt_general):	
		menuItem2 = wx.MenuItem(self.menu, wx.ID_ANY, u"Cerrar ventana", wx.EmptyString, wx.ITEM_NORMAL )
		menuItem2.SetBitmap(wx.Bitmap(u"imagenes/atras.png", wx.BITMAP_TYPE_ANY ))

		self.Bind(wx.EVT_MENU, self.irAtras, menuItem2)
		self.menu.Append(menuItem2)
		opt_general.SetMenuBar(self.menubar)

	def informacion(self,event):
		informacion_semillero = VentanaInformacion()
		informacion_semillero.informacion()

	def irAtras(self,event):
		self.Destroy()

	def salir(self,event):
		self.opt_general.Destroy()
