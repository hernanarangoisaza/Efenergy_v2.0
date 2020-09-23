from ArchivoInformacion import ArchivoInformacion
import wx
import easygui as eg

class EditarInformacion(wx.Frame):
	def __init__(self, id, title, informacion, archivo_txt, ventana_inicio, identificador):
		wx.Frame.__init__(self, None, id, title, size = (878, 350),pos=(0,0), style = wx.DEFAULT_FRAME_STYLE
			& ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
		self.ventana_inicio = ventana_inicio
		self.SetIcon(wx.Icon("imagenes/logo.png"))
		self.panel = wx.Panel(self,-1)
		self.archivo_txt = archivo_txt
		self.informacion = informacion
		self.identificador = identificador
		self.SetBackgroundColour("#FFFFFF")
		self.elementos()

	def elementos(self):
		nombre_variable = ["Voltaje","Potencia","Armónicos"]
		panel = wx.Panel(self.panel, -1, size=(878,60), pos=wx.DefaultPosition)

		txt_informacion = wx.StaticText(panel, -1, "Editar información de %s"% nombre_variable[self.identificador - 1], pos=(10, 10))
		font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		txt_informacion.SetFont(font)
		txt_informacion.SetForegroundColour("#FFFFFF")
		panel.SetBackgroundColour("#6E7B99")

		txt_editar_norma = wx.StaticText(self.panel, -1, "Cambiar Archivo PDF:", pos=(650, 70))
		font = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		txt_editar_norma.SetFont(font)

		button_seleccionar = wx.Button(self.panel, -1, u"Seleccionar Norma", size=(130,30), pos=(680,100))
		button_seleccionar.Bind(wx.EVT_BUTTON, self.on_seleccion_norma)

		self.button_cargar = wx.Button(self.panel, -1, u"Cargar", size=(130,30), pos=(680,140))
		self.button_cargar.Show(False)
		self.button_cargar.Bind(wx.EVT_BUTTON, self.cargar_norma)

		linea_separador = wx.StaticLine(self.panel, id=wx.ID_ANY, pos=(640,65), size=(2,240),
           style=wx.LI_VERTICAL)
		linea_separador.SetBackgroundColour("#6E7B99")

		self.inp_informacion = wx.TextCtrl(self.panel, wx.ID_ANY, self.informacion, size=(600,200), pos=(30,70), style=wx.TE_MULTILINE)
		
		button_editar = wx.BitmapButton( self.panel, wx.ID_ANY, wx.Bitmap(u"imagenes/icono_aceptar.png"), pos=(600,275), size=wx.DefaultSize, style=wx.BU_AUTODRAW|wx.NO_BORDER )
		button_editar.SetBackgroundColour("#FFFFFF")
		button_editar.Bind(wx.EVT_BUTTON, self.on_editar_informacion)

		button_cancelar = wx.BitmapButton( self.panel, wx.ID_ANY, wx.Bitmap(u"imagenes/icono_cancelar.png"), pos=(30,275), size=wx.DefaultSize, style=wx.BU_AUTODRAW|wx.NO_BORDER )
		button_cancelar.SetBackgroundColour("#FFFFFF")
		button_cancelar.Bind(wx.EVT_BUTTON, self.on_cancelar)

	def on_editar_informacion(self, event):
		try:
			confirmacion = self.msgPregunta("Desea guardar la información?")
			if confirmacion == wx.ID_YES:
				informacion = self.archivo_txt.leer_archivo()
				if self.identificador == 1:
					total_informacion = "%s\n&%s\n&%s" % (self.inp_informacion.GetValue(),informacion[1],informacion[2])
					self.archivo_txt.escribir_archivo(total_informacion)
					self.ventana_inicio.txt_informacion_voltaje.SetLabel(self.archivo_txt.leer_archivo()[0])

				if self.identificador == 2:
					total_informacion = "%s\n&%s\n&%s" % (informacion[0],self.inp_informacion.GetValue(),informacion[2])
					self.archivo_txt.escribir_archivo(total_informacion)
					self.ventana_inicio.txt_informacion_potencia.SetLabel(self.archivo_txt.leer_archivo()[1])

				if self.identificador == 3:
					total_informacion = "%s\n&%s\n&%s" % (informacion[0],informacion[1],self.inp_informacion.GetValue())
					self.archivo_txt.escribir_archivo(total_informacion)
					self.ventana_inicio.txt_informacion_armonico.SetLabel(self.archivo_txt.leer_archivo()[2])

				self.msgInformacion("El texto de información se modificó correctamente")
				self.Destroy()

		except:
			self.msgError("Ha ocurrido un Error al modificar la información")


	def on_seleccion_norma(self, event):
		try:
			extension = ["*.pdf"]
			a = None # dfgf
			self.archivo = eg.fileopenbox(msg="Seleccionar PDF", title="Control", default=extension[0], filetypes=extension)
			#eg.msgbox("Error en seleccion de archivo.\nEl archivo debe de ser extension xlsx", "Error", ok_button="Continuar")
			
			if self.archivo != None:
				self.button_cargar.Show( True )

			else:
				self.button_cargar.Show( False )

		except:
			self.msgError("Error al intentar seleccionar el archivo PDF")

	def cargar_norma(self, event):
		try:
			import shutil
			if self.identificador == 1:
				shutil.copy(self.archivo, 'archivo/NormaVoltaje.pdf')

			if self.identificador == 2:
				shutil.copy(self.archivo, 'archivo/NormaPotencia.pdf')

			if self.identificador == 3:
				shutil.copy(self.archivo, 'archivo/NormaArmónico.pdf')

			self.msgInformacion("Se cargo el archivo PDF correctamente")
			self.button_cargar.Show( False )

		except:
			self.msgError("Error al cargar el archivo. \nPor favor verifique que el archivo seleccionado sea extensión .pdf ")

	def on_cancelar(self, event):
		confirmacion = self.msgPregunta("Realmente desea cancelar la operación?")
		if confirmacion == wx.ID_YES:
			self.Destroy()

	def msgInformacion(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'Información',style=wx.ICON_INFORMATION | wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def msgError(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'Error',style=wx.ICON_ERROR | wx.OK)
		answer = box.ShowModal()
		box.Destroy()

	def msgPregunta(self, mensaje):
		box = wx.MessageDialog(None, mensaje, 'Confirmación', style=wx.ICON_QUESTION|wx.YES_NO)
		answer = box.ShowModal()
		box.Destroy()
		return answer