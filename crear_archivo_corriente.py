#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xlwt
import pandas
import os

class ArchivoCorriente:
	def CrearArchivo(self, archivo_excel, nombre):
		wb = xlwt.Workbook()
		encontrado = False
		for i in archivo_excel.sheet_names:
			ws = wb.add_sheet(i)
			ws.write(0,0,'Fecha')
			ws.write(0,1,'Hora')
			ws.write(0,2,'Corriente Fundamental A Med')
			ws.write(0,3,'Corriente Fundamental B Med')
			ws.write(0,4,'Corriente Fundamental C Med')
			ws.write(0,5,'THD A A Med')
			ws.write(0,6,'THD A B Med')
			ws.write(0,7,'THD A C Med')
			ws.write(0,8,'Armónicos Corriente0 A Med')
			ws.write(0,9,'Armónicos Corriente0 B Med')
			ws.write(0,10,'Armónicos Corriente0 C Med')
			ws.write(0,11,'Armónicos Corriente1 A Med')
			ws.write(0,12,'Armónicos Corriente1 B Med')
			ws.write(0,13,'Armónicos Corriente1 C Med')
			ws.write(0,14,'Armónicos Corriente2 A Med')
			ws.write(0,15,'Armónicos Corriente2 B Med')
			ws.write(0,16,'Armónicos Corriente2 C Med')
			ws.write(0,17,'Armónicos Corriente3 A Med')
			ws.write(0,18,'Armónicos Corriente3 B Med')
			ws.write(0,19,'Armónicos Corriente3 C Med')
			ws.write(0,20,'Armónicos Corriente4 A Med')
			ws.write(0,21,'Armónicos Corriente4 B Med')
			ws.write(0,22,'Armónicos Corriente4 C Med')
			ws.write(0,23,'Armónicos Corriente5 A Med')
			ws.write(0,24,'Armónicos Corriente5 B Med')
			ws.write(0,25,'Armónicos Corriente5 C Med')
			ws.write(0,26,'Armónicos Corriente6 A Med')
			ws.write(0,27,'Armónicos Corriente6 B Med')
			ws.write(0,28,'Armónicos Corriente6 C Med')
			ws.write(0,29,'Armónicos Corriente7 A Med')
			ws.write(0,30,'Armónicos Corriente7 B Med')
			ws.write(0,31,'Armónicos Corriente7 C Med')
			ws.write(0,32,'Armónicos Corriente8 A Med')
			ws.write(0,33,'Armónicos Corriente8 B Med')
			ws.write(0,34,'Armónicos Corriente8 C Med')
			ws.write(0,35,'Armónicos Corriente9 A Med')
			ws.write(0,36,'Armónicos Corriente9 B Med')
			ws.write(0,37,'Armónicos Corriente9 C Med')
			ws.write(0,38,'Armónicos Corriente10 A Med')
			ws.write(0,39,'Armónicos Corriente10 B Med')
			ws.write(0,40,'Armónicos Corriente10 C Med')
			ws.write(0,41,'Armónicos Corriente11 A Med')
			ws.write(0,42,'Armónicos Corriente11 B Med')
			ws.write(0,43,'Armónicos Corriente11 C Med')

			df = pandas.read_excel(archivo_excel, i)
			for y in df.columns.tolist():
				if y == 'THD A A Med':
					encontrado = True
					fecha = df['Fecha'].values
					hora = df['Hora'].values
					corrienteA = df['Corriente Fundamental A Med']
					corrienteB = df['Corriente Fundamental B Med']
					corrienteC = df['Corriente Fundamental C Med']
					thdcA = df['THD A A Med'].values
					thdcB = df['THD A B Med'].values
					thdcC = df['THD A C Med'].values
					armonico0 = df['Armónicos Corriente0 A Med'].values
					armonico1 = df['Armónicos Corriente1 A Med'].values
					armonico2 = df['Armónicos Corriente2 A Med'].values
					armonico3 = df['Armónicos Corriente3 A Med'].values
					armonico4 = df['Armónicos Corriente4 A Med'].values
					armonico5 = df['Armónicos Corriente5 A Med'].values
					armonico6 = df['Armónicos Corriente6 A Med'].values
					armonico7 = df['Armónicos Corriente7 A Med'].values
					armonico8 = df['Armónicos Corriente8 A Med'].values
					armonico9 = df['Armónicos Corriente9 A Med'].values
					armonico10 = df['Armónicos Corriente10 A Med'].values
					armonico11 = df['Armónicos Corriente11 A Med'].values

					armonicoB0 = df['Armónicos Corriente0 B Med'].values
					armonicoB1 = df['Armónicos Corriente1 B Med'].values
					armonicoB2 = df['Armónicos Corriente2 B Med'].values
					armonicoB3 = df['Armónicos Corriente3 B Med'].values
					armonicoB4 = df['Armónicos Corriente4 B Med'].values
					armonicoB5 = df['Armónicos Corriente5 B Med'].values
					armonicoB6 = df['Armónicos Corriente6 B Med'].values
					armonicoB7 = df['Armónicos Corriente7 B Med'].values
					armonicoB8 = df['Armónicos Corriente8 B Med'].values
					armonicoB9 = df['Armónicos Corriente9 B Med'].values
					armonicoB10 = df['Armónicos Corriente10 B Med'].values
					armonicoB11 = df['Armónicos Corriente11 B Med'].values

					armonicoC0 = df['Armónicos Corriente0 C Med'].values
					armonicoC1 = df['Armónicos Corriente1 C Med'].values
					armonicoC2 = df['Armónicos Corriente2 C Med'].values
					armonicoC3 = df['Armónicos Corriente3 C Med'].values
					armonicoC4 = df['Armónicos Corriente4 C Med'].values
					armonicoC5 = df['Armónicos Corriente5 C Med'].values
					armonicoC6 = df['Armónicos Corriente6 C Med'].values
					armonicoC7 = df['Armónicos Corriente7 C Med'].values
					armonicoC8 = df['Armónicos Corriente8 C Med'].values
					armonicoC9 = df['Armónicos Corriente9 C Med'].values
					armonicoC10 = df['Armónicos Corriente10 C Med'].values
					armonicoC11 = df['Armónicos Corriente11 C Med'].values

					for z in range(len(hora)):
						ws.write(z+1, 0, str(fecha[z]))
						ws.write(z+1, 1, str(hora[z]))
						ws.write(z+1, 2, float(corrienteA[z]))
						ws.write(z+1, 3, float(corrienteB[z]))
						ws.write(z+1, 4, float(corrienteC[z]))
						ws.write(z+1, 5, float(thdcA[z]))
						ws.write(z+1, 6, float(thdcB[z]))
						ws.write(z+1, 7, float(thdcC[z]))
						ws.write(z+1, 8, float(armonico0[z]))
						ws.write(z+1, 9, float(armonicoB0[z]))
						ws.write(z+1, 10, float(armonicoC0[z]))
						ws.write(z+1, 11, float(armonico1[z]))
						ws.write(z+1, 12, float(armonicoB0[z]))
						ws.write(z+1, 13, float(armonicoC0[z]))
						ws.write(z+1, 14, float(armonico2[z]))
						ws.write(z+1, 15, float(armonicoB2[z]))
						ws.write(z+1, 16, float(armonicoC2[z]))
						ws.write(z+1, 17, float(armonico3[z]))
						ws.write(z+1, 18, float(armonicoB3[z]))
						ws.write(z+1, 19, float(armonicoC3[z]))
						ws.write(z+1, 20, float(armonico4[z]))
						ws.write(z+1, 21, float(armonicoB4[z]))
						ws.write(z+1, 22, float(armonicoC4[z]))
						ws.write(z+1, 23, float(armonico5[z]))
						ws.write(z+1, 24, float(armonicoB5[z]))
						ws.write(z+1, 25, float(armonicoC5[z]))
						ws.write(z+1, 26, float(armonico6[z]))
						ws.write(z+1, 27, float(armonicoB6[z]))
						ws.write(z+1, 28, float(armonicoC6[z]))
						ws.write(z+1, 29, float(armonico7[z]))
						ws.write(z+1, 30, float(armonicoB7[z]))
						ws.write(z+1, 31, float(armonicoC7[z]))
						ws.write(z+1, 32, float(armonico8[z]))
						ws.write(z+1, 33, float(armonicoB8[z]))
						ws.write(z+1, 34, float(armonicoC8[z]))
						ws.write(z+1, 35, float(armonico9[z]))
						ws.write(z+1, 36, float(armonicoB9[z]))
						ws.write(z+1, 37, float(armonicoC9[z]))
						ws.write(z+1, 38, float(armonico10[z]))
						ws.write(z+1, 39, float(armonicoB10[z]))
						ws.write(z+1, 40, float(armonicoC10[z]))
						ws.write(z+1, 41, float(armonico11[z]))
						ws.write(z+1, 42, float(armonicoB11[z]))
						ws.write(z+1, 43, float(armonicoC11[z]))

		ruta = ''

		if nombre == 'default':

			wb.save('armonicos THD A.xls')
			ruta = 'armonicos THD A.xls'

		else:
			wb.save(nombre)
			ruta = nombre
		#ruta = 'armonicos THD A.xls'
		#if encontrado == True:
		return ruta

	def Cerrar(self):
		borrar = os.remove('armonicos THD A.xls')
		return borrar




