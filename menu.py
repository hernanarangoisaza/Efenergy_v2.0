import wx
import easygui as eg 
from DistorcionArmonica import DistorcionArmonica
from NuevoArchivoArmonico import NuevoArchivoArmonico
from NuevoArchivoVoltaje import NuevoArchivoVoltaje
from NuevoArchivoPotencia import NuevoArchivoPotencia
from VentanaInformacion import VentanaInformacion

class Menu:
	def __init__(self, id,archivo_excel):
		self.id = id
		self.archivo_excel = archivo_excel

	def menugeneral(self,opt_general):
		self.opt_general = opt_general
		self.menubar = wx.MenuBar(0)
		self.menu = wx.Menu()
		menuItem = wx.MenuItem(self.menu, wx.ID_ANY, u"Guardar Archivo\tCTRL+S", u"Guardar archivo en formato XLS", wx.ITEM_NORMAL )
		menuItem.SetBitmap(wx.Bitmap(u"imagenes/guardar_como.png", wx.BITMAP_TYPE_ANY ))
		self.menu.Append(menuItem)

		opt_general.Bind(wx.EVT_MENU, self.guardarArchivo, id = menuItem.GetId() )		
		self.menu.AppendSeparator()

		menuItem3 = wx.MenuItem(self.menu, wx.ID_ANY, u"Salir\tCTRL+Q",u"Salir de Efenergy",  wx.ITEM_NORMAL )
		menuItem3.SetBitmap(wx.Bitmap(u"imagenes/atras.png", wx.BITMAP_TYPE_ANY ))
		opt_general.Bind(wx.EVT_MENU, self.salir, menuItem3)
		self.menu.Append(menuItem3)
		self.menu.AppendSeparator()

		menu2 = wx.Menu()
		menu2Item = wx.MenuItem(self.menu, wx.ID_ANY, u"About...\tF1", u"Acerca de Efenergy", wx.ITEM_NORMAL )
		menu2Item.SetBitmap(wx.Bitmap(u"imagenes/acerca_de.png", wx.BITMAP_TYPE_ANY ))
		opt_general.Bind(wx.EVT_MENU, self.informacion, menu2Item)
		menu2.Append(menu2Item)

		self.menubar.Append(self.menu, u"Archivo" )
		self.menubar.Append(menu2, u"Ayuda" ) 
		
		opt_general.SetMenuBar(self.menubar)

	def informacion(self,event):
		informacion_semillero = VentanaInformacion()
		informacion_semillero.informacion()

	def opt_armonicos(self,opt_general):
		menu3 = wx.Menu()
		menuItem3 = wx.MenuItem(self.menu, wx.ID_ANY, u"Distorción Armonica"+ u"\t" + u"", u"",wx.ITEM_NORMAL )
		menuItem3.SetBitmap(wx.Bitmap(u"imagenes/distorcion.png", wx.BITMAP_TYPE_ANY ))
		opt_general.Bind(wx.EVT_MENU, self.onDistorcionArmonica, menuItem3)
		menu3.Append(menuItem3)
		self.menubar.Append(menu3, u"Armonicos")
		opt_general.SetMenuBar(self.menubar)

	def opt_grafica_voltaje(self):
		return self.menu
			
	def guardarArchivo(self, event):
		extension = "*.xls"
		archivo = eg.filesavebox(msg="Guardar archivo",
							title="Control: filesavebox",
							default=extension,
							filetypes=extension)

		
		if archivo is not None:
			if self.id == 1:
				crear_archivo = NuevoArchivoArmonico()
				archivo_armonicos = crear_archivo.CrearArchivo(self.archivo_excel, archivo, "A", "", "Corriente")

			elif self.id == 2:
				crear_archivo = NuevoArchivoArmonico()
				archivo_armonicos = crear_archivo.CrearArchivo(self.archivo_excel,archivo, "V", "N", "Tensión")
			
			elif self.id == 3:
				crear_archivo = NuevoArchivoVoltaje()
				archivo_voltaje = crear_archivo.CrearArchivo(self.archivo_excel, archivo)

			elif self.id == 4:
				crear_archivo = NuevoArchivoPotencia()
				archivo_voltaje = crear_archivo.CrearArchivo(self.archivo_excel, archivo, 4)

			elif self.id == 5:
				crear_archivo = NuevoArchivoPotencia()
				archivo_voltaje = crear_archivo.CrearArchivo(self.archivo_excel, archivo, 5)

			self.msgInformacion("Archivo Guardado")

		

	def onDistorcionArmonica(self, event):
		app = wx.App()
		frame = DistorcionArmonica(self.id, 'Distorción Armonica',self.archivo_excel)
		frame.Centre()
		frame.Show()
		self.Destroy()
		app.MainLoop()

	def irAtras(self,event):
		self.Destroy()

	def salir(self,event):
		self.opt_general.Destroy()

	def msgInformacion(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'Informacion', wx.ICON_INFORMATION|wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def msgError(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'Error', wx.ICON_ERROR|wx.OK)
		answer = box.ShowModal()
		box.Destroy()

