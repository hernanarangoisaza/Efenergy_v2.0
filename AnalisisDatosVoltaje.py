#!/usr/bin/python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import pandas

from Efenergy2Globales import *
import Efenergy2UI

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import datetime
import numpy      

#from GraficaPotencia import GraficaPotencia
#from NuevoArchivoVoltajeReglas import NuevoArchivoVoltajeReglas

# ************************************************************************************************************************

class AnalisisDatosVoltaje():

	def __init__(self, datosVoltaje, rangoMenor, rangoMayor, dia, fase, voltaje, window, tablaVoltaje):

		self.datosVoltaje = datosVoltaje
		self.rangoMenor = rangoMenor
		self.rangoMayor = rangoMayor
		self.dia = dia
		self.fase = fase
		self.voltaje = voltaje

		self.txt_fase_a = []
		self.txt_fase_b = []
		self.txt_fase_c = []

		self.cargarDatos(tablaVoltaje)

	# ************************************************************************************************************************

	def cargarDatos(self, tablaVoltaje):

		dfVoltaje = pandas.read_excel(self.datosVoltaje, self.dia)

		self.fechas = []

		for i in dfVoltaje['Fecha']:
			self.fechas.append(str(i).rstrip(':0'))		# Verificar para que es el ':0'

		self.horas = dfVoltaje.Hora.str.slice(0,13)
		
		voltajes = dfVoltaje[('Vrms ph-n %sN Med')% self.fase].values

		estadoVoltaje = self.voltaje

		if estadoVoltaje == 'RANGO':

			self.datosRango(voltajes, tablaVoltaje)	

		elif estadoVoltaje == 'MAYOR':

			self.datosMayores(voltajes, tablaVoltaje)

		elif estadoVoltaje == 'MENOR':

			self.datosMenores(voltajes, tablaVoltaje)

	# ************************************************************************************************************************

	def datosRango(self, voltajes, tablaVoltaje):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] < self.rangoMayor and voltajes[i] > self.rangoMenor:

				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])
				listaVoltajes.append(voltajes[i])

		self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes, tablaVoltaje)

	# ************************************************************************************************************************

	def datosMenores(self, voltajes, tablaVoltaje):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] < self.rangoMenor:

				listaVoltajes.append(voltajes[i])
				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])

		self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes, tablaVoltaje)
			
	# ************************************************************************************************************************

	def datosMayores(self, voltajes, tablaVoltaje):

		listaFechas = []
		listaHoras = []
		listaVoltajes = []

		for i in range(len(voltajes)):

			if voltajes[i] > self.rangoMayor:

				listaVoltajes.append(voltajes[i])
				listaFechas.append(self.fechas[i])
				listaHoras.append(self.horas[i])

		dataTable = self.llenarTablaVoltaje(listaFechas, listaHoras, listaVoltajes, tablaVoltaje)
		
	# ************************************************************************************************************************

	def llenarTablaVoltaje(self, listaFechas, listaHoras, listaVoltajes, tablaVoltaje):

		numRows = len(listaVoltajes)
		numCols = 3
		
		data = [[j for j in range(numCols)] for i in range(numRows)]

		for fila in range(0, numRows):
			data[fila] = [str(listaFechas[fila]), str(listaHoras[fila]), str(listaVoltajes[fila])]

		tablaVoltaje.update(values=data)

	# ************************************************************************************************************************

	def graficaVoltajeVsTiempo(self, event, dia):

		dfVoltaje = pandas.read_excel(self.datosVoltaje, self.dia)

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

	# ************************************************************************************************************************



