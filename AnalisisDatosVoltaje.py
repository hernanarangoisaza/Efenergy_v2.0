#!/usr/bin/python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg


import wx
import wx.grid
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy      
from menu import Menu 
import wx.lib.agw.aquabutton as AB    
from GraficaPotencia import GraficaPotencia
from matplotlib.widgets import CheckButtons
from NuevoArchivoVoltajeReglas import NuevoArchivoVoltajeReglas

class AnalisisDatosVoltaje(wx.Frame):

	def __init__(self, datosVoltaje, rangoMenor, rangoMayor, dia, fase, voltaje, layoutTabTablaContenido):

		self.datosVoltaje = datosVoltaje
		self.rangoMenor = rangoMenor
		self.rangoMayor = rangoMayor
		self.dia = dia
		self.fase = fase
		self.voltaje = voltaje
		self.layoutTabTablaContenido = layoutTabTablaContenido

		self.txt_fase_a = []
		self.txt_fase_b = []
		self.txt_fase_c = []

		self.cargarDatos()

#----------------------------------------------------------------------------------------------------

	def cargarDatos(self):

		dfVoltaje = pd.read_excel(self.datosVoltaje, self.dia)

		self.fechas = []

		for i in dfVoltaje['Fecha']:
			self.fechas.append(str(i).rstrip(':0'))		# Verificar para que es el ':0'

		self.horas = dfVoltaje.Hora.str.slice(0,13)
		
		voltajes = dfVoltaje[('Vrms ph-n %sN Med')% self.fase].values

		estadoVoltaje = self.voltaje

		if estadoVoltaje == 'RANGO':

			self.datosRango(voltajes)	

		elif estadoVoltaje == 'MAYOR':

			self.datosMayores(voltajes)

		elif estadoVoltaje == 'MENOR':

			self.datosMenores(voltajes)

	def datosRango(self, voltajes):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] < self.rangoMayor and voltajes[i] > self.rangoMenor:

				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])
				listaVoltajes.append(voltajes[i])

		self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes)

	def datosMenores(self, voltajes):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] < self.rangoMenor:

				listaVoltajes.append(voltajes[i])
				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])

		self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes)
			
	def datosMayores(self,voltajes):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] > self.rangoMayor:

				listaVoltajes.append(voltajes[i])
				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])

		dataTable = self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes)
		
	def llenarTablaVoltaje(self, listaFechas, listaHoras, listaVoltajes):

		#self.tablaVoltaje.DeleteAllItems()

		encabezadoVoltaje = ['Fecha', 'Hora', 'Voltaje']

		prueba = sg.Text('Acá va la tabla', key="-prueba-")

		self.layoutTabTablaContenido.append([prueba])


#		tablaVoltaje = sg.Table(key='-tablaVoltaje-',
#								values=[['', '', ''],],
#								headings=encabezadoVoltaje, 
#								max_col_width=25,
#								# background_color='light blue',
#								auto_size_columns=True,
#								display_row_numbers=True,
#								justification='right',
#								num_rows=20,
#								alternating_row_color='lightyellow',
#								row_height=35),


#		for fila in range(len(listaVoltajes)):

#			data.append(str(fila+1), str(listaFechas[fila]), str(listaHoras[fila]), str(listaVoltajes[fila]))

#		window['-tablaVoltaje-'].update(values=data)

	def graficaVoltajeVsTiempo(self, event, dia):

		dfVoltaje = pd.read_excel(self.datosVoltaje, self.dia)

		datosVoltajeFaseA = dfVoltaje['Vrms ph-n AN Med'].values
		datosVoltajeFaseB = dfVoltaje['Vrms ph-n BN Med'].values
		datosVoltajeFaseC = dfVoltaje['Vrms ph-n CN Med'].values 

		lsHora = df.Hora.str.slice(0,2)
		lsMinuto = df.Hora.str.slice(3,5)
		lsAmPm = df.Hora.str.slice(9,13)

		grafica = GraficaPotencia()

		grafico.generar('voltaje',
						lsHora,
 						lsMinuto,
 						lsAmPm,
 						datosVoltajeFaseA,
 						datosVoltajeFaseB,
						datosVoltajeFaseC,
						'Tiempo(Hora)',
						'Voltaje')

