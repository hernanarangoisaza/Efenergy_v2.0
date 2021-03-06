# ************************************************************************************************************************

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import pandas

from Efenergy2Globales import *
import Efenergy2UI
from Efenergy2GraficoTipo1 import Efenergy2GraficoTipo1

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import datetime
import numpy      


# ************************************************************************************************************************

class Efenergy2AnalisisVoltaje():

	def __init__(self, datosVoltaje, rangoMenor, rangoMayor, dia, fase, voltaje, window):

		self.datosVoltaje = datosVoltaje
		self.rangoMenor = rangoMenor
		self.rangoMayor = rangoMayor
		self.dia = dia
		self.fase = fase
		self.voltaje = voltaje

		self.cargarDatos(window)

	# ************************************************************************************************************************

	def cargarDatos(self, window):

		dfVoltaje = pandas.read_excel(self.datosVoltaje, self.dia)

		self.fechas = []

		for i in dfVoltaje['Fecha']:
			self.fechas.append(str(i).rstrip(':0'))		# Verificar para que es el ':0'

		self.horas = dfVoltaje.Hora.str.slice(0,13)
		
		voltajes = dfVoltaje[('Vrms ph-n %sN Med')% self.fase].values

		estadoVoltaje = self.voltaje

		if estadoVoltaje == 'RANGO':

			self.datosRango(voltajes, window)	

		elif estadoVoltaje == 'MAYOR':

			self.datosMayores(voltajes, window)

		elif estadoVoltaje == 'MENOR':

			self.datosMenores(voltajes, window)

	# ************************************************************************************************************************

	def datosRango(self, voltajes, window):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] < self.rangoMayor and voltajes[i] > self.rangoMenor:

				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])
				listaVoltajes.append(voltajes[i])

		self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes, window)

	# ************************************************************************************************************************

	def datosMenores(self, voltajes, window):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] < self.rangoMenor:

				listaVoltajes.append(voltajes[i])
				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])

		self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes, window)
			
	# ************************************************************************************************************************

	def datosMayores(self, voltajes, window):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] > self.rangoMayor:

				listaVoltajes.append(voltajes[i])
				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])

		dataTable = self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes, window)
		
	# ************************************************************************************************************************

	def llenarTablaVoltaje(self, listaFechas, listaHoras, listaVoltajes, window):

		numRows = len(listaVoltajes)
		numCols = 4
		
		data = [[j for j in range(numCols)] for i in range(numRows)]

		for fila in range(0, numRows):
			data[fila] = [str(fila+1), str(listaFechas[fila]), str(listaHoras[fila]), str(listaVoltajes[fila])]

		window['-tablaVoltaje-'].update(values=data)
		window['-cantidadRegistros-'].update(numRows)

		self.graficaVoltajeVsTiempo(self.dia)

	# ************************************************************************************************************************

	def graficaVoltajeVsTiempo(self, dia):

		dfVoltaje = pandas.read_excel(self.datosVoltaje, self.dia)

		datosVoltajeFaseA = dfVoltaje['Vrms ph-n AN Med'].values
		datosVoltajeFaseB = dfVoltaje['Vrms ph-n BN Med'].values
		datosVoltajeFaseC = dfVoltaje['Vrms ph-n CN Med'].values 

		lsHora = dfVoltaje.Hora.str.slice(0,2)
		lsMinuto = dfVoltaje.Hora.str.slice(3,5)
		lsAmPm = dfVoltaje.Hora.str.slice(9,13)

		grafica = Efenergy2GraficoTipo1()

		grafica.generar(idVoltaje, 
						lsHora, 
						lsMinuto, 
						lsAmPm, 
						datosVoltajeFaseA, 
						datosVoltajeFaseB, 
						datosVoltajeFaseC, 
						self.rangoMenor,
						self.rangoMayor,
						'Tiempo(Hora)', 
						'Voltaje')

	# ************************************************************************************************************************



