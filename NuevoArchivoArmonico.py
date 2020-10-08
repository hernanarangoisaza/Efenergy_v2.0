#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xlwt
import pandas
import os
import os.path as path

class NuevoArchivoArmonico:
	def CrearArchivo(self, archivo_excel, nombre, letra_armonico, neutro, armonico):
		wb = xlwt.Workbook()
		for i in archivo_excel.sheet_names:
			ws = wb.add_sheet(i)
			ws.write(0,0,'Fecha')
			ws.write(0,1,'Hora')
			ws.write(0,2,'Corriente Fundamental A Med')
			ws.write(0,3,'Corriente Fundamental B Med')
			ws.write(0,4,'Corriente Fundamental C Med')
			ws.write(0,5,('THD %s A%s Med'% (letra_armonico,neutro)))
			ws.write(0,6,('THD %s B%s Med'% (letra_armonico,neutro)))
			ws.write(0,7,('THD %s C%s Med'% (letra_armonico,neutro)))
			ws.write(0,8,'Armónicos %s0 A%s Med'% (armonico, neutro))
			ws.write(0,9,'Armónicos %s0 B%s Med'% (armonico, neutro))
			ws.write(0,10,'Armónicos %s0 C%s Med'% (armonico, neutro))
			ws.write(0,11,'Armónicos %s1 A%s Med'% (armonico, neutro))
			ws.write(0,12,'Armónicos %s1 B%s Med'% (armonico, neutro))
			ws.write(0,13,'Armónicos %s1 C%s Med'% (armonico, neutro))
			ws.write(0,14,'Armónicos %s2 A%s Med'% (armonico, neutro))
			ws.write(0,15,'Armónicos %s2 B%s Med'% (armonico, neutro))
			ws.write(0,16,'Armónicos %s2 C%s Med'% (armonico, neutro))
			ws.write(0,17,'Armónicos %s3 A%s Med'% (armonico, neutro))
			ws.write(0,18,'Armónicos %s3 B%s Med'% (armonico, neutro))
			ws.write(0,19,'Armónicos %s3 C%s Med'% (armonico, neutro))
			ws.write(0,20,'Armónicos %s4 A%s Med'% (armonico, neutro))
			ws.write(0,21,'Armónicos %s4 B%s Med'% (armonico, neutro))
			ws.write(0,22,'Armónicos %s4 C%s Med'% (armonico, neutro))
			ws.write(0,23,'Armónicos %s5 A%s Med'% (armonico, neutro))
			ws.write(0,24,'Armónicos %s5 B%s Med'% (armonico, neutro))
			ws.write(0,25,'Armónicos %s5 C%s Med'% (armonico, neutro))
			ws.write(0,26,'Armónicos %s6 A%s Med'% (armonico, neutro))
			ws.write(0,27,'Armónicos %s6 B%s Med'% (armonico, neutro))
			ws.write(0,28,'Armónicos %s6 C%s Med'% (armonico, neutro))
			ws.write(0,29,'Armónicos %s7 A%s Med'% (armonico, neutro))
			ws.write(0,30,'Armónicos %s7 B%s Med'% (armonico, neutro))
			ws.write(0,31,'Armónicos %s7 C%s Med'% (armonico, neutro))
			ws.write(0,32,'Armónicos %s8 A%s Med'% (armonico, neutro))
			ws.write(0,33,'Armónicos %s8 B%s Med'% (armonico, neutro))
			ws.write(0,34,'Armónicos %s8 C%s Med'% (armonico, neutro))
			ws.write(0,35,'Armónicos %s9 A%s Med'% (armonico, neutro))
			ws.write(0,36,'Armónicos %s9 B%s Med'% (armonico, neutro))
			ws.write(0,37,'Armónicos %s9 C%s Med'% (armonico, neutro))
			ws.write(0,38,'Armónicos %s10 A%s Med'% (armonico, neutro))
			ws.write(0,39,'Armónicos %s10 B%s Med'% (armonico, neutro))
			ws.write(0,40,'Armónicos %s10 C%s Med'% (armonico, neutro))
			ws.write(0,41,'Armónicos %s11 A%s Med'% (armonico, neutro))
			ws.write(0,42,'Armónicos %s11 B%s Med'% (armonico, neutro))
			ws.write(0,43,'Armónicos %s11 C%s Med'% (armonico, neutro))

			df = pandas.read_excel(archivo_excel, i)
			for y in df.columns.tolist():
				if y == ('THD %s A%s Med'% (letra_armonico, neutro)):
					fecha = df['Fecha'].values
					hora = df['Hora'].values
					corrienteA = df['Corriente Fundamental A Med']
					corrienteB = df['Corriente Fundamental B Med']
					corrienteC = df['Corriente Fundamental C Med']
					thdcA = df['THD %s A%s Med'% (letra_armonico,neutro)].values
					thdcB = df['THD %s B%s Med'% (letra_armonico,neutro)].values
					thdcC = df['THD %s C%s Med'% (letra_armonico,neutro)].values
					armonico0 = df['Armónicos %s0 A%s Med'% (armonico, neutro)].values
					armonico1 = df['Armónicos %s1 A%s Med'% (armonico, neutro)].values
					armonico2 = df['Armónicos %s2 A%s Med'% (armonico, neutro)].values
					armonico3 = df['Armónicos %s3 A%s Med'% (armonico, neutro)].values
					armonico4 = df['Armónicos %s4 A%s Med'% (armonico, neutro)].values
					armonico5 = df['Armónicos %s5 A%s Med'% (armonico, neutro)].values
					armonico6 = df['Armónicos %s6 A%s Med'% (armonico, neutro)].values
					armonico7 = df['Armónicos %s7 A%s Med'% (armonico, neutro)].values
					armonico8 = df['Armónicos %s8 A%s Med'% (armonico, neutro)].values
					armonico9 = df['Armónicos %s9 A%s Med'% (armonico, neutro)].values
					armonico10 = df['Armónicos %s10 A%s Med'% (armonico, neutro)].values
					armonico11 = df['Armónicos %s11 A%s Med'% (armonico, neutro)].values

					armonicoB0 = df['Armónicos %s0 B%s Med'% (armonico, neutro)].values
					armonicoB1 = df['Armónicos %s1 B%s Med'% (armonico, neutro)].values
					armonicoB2 = df['Armónicos %s2 B%s Med'% (armonico, neutro)].values
					armonicoB3 = df['Armónicos %s3 B%s Med'% (armonico, neutro)].values
					armonicoB4 = df['Armónicos %s4 B%s Med'% (armonico, neutro)].values
					armonicoB5 = df['Armónicos %s5 B%s Med'% (armonico, neutro)].values
					armonicoB6 = df['Armónicos %s6 B%s Med'% (armonico, neutro)].values
					armonicoB7 = df['Armónicos %s7 B%s Med'% (armonico, neutro)].values
					armonicoB8 = df['Armónicos %s8 B%s Med'% (armonico, neutro)].values
					armonicoB9 = df['Armónicos %s9 B%s Med'% (armonico, neutro)].values
					armonicoB10 = df['Armónicos %s10 B%s Med'% (armonico, neutro)].values
					armonicoB11 = df['Armónicos %s11 B%s Med'% (armonico, neutro)].values

					armonicoC0 = df['Armónicos %s0 C%s Med'% (armonico, neutro)].values
					armonicoC1 = df['Armónicos %s1 C%s Med'% (armonico, neutro)].values
					armonicoC2 = df['Armónicos %s2 C%s Med'% (armonico, neutro)].values
					armonicoC3 = df['Armónicos %s3 C%s Med'% (armonico, neutro)].values
					armonicoC4 = df['Armónicos %s4 C%s Med'% (armonico, neutro)].values
					armonicoC5 = df['Armónicos %s5 C%s Med'% (armonico, neutro)].values
					armonicoC6 = df['Armónicos %s6 C%s Med'% (armonico, neutro)].values
					armonicoC7 = df['Armónicos %s7 C%s Med'% (armonico, neutro)].values
					armonicoC8 = df['Armónicos %s8 C%s Med'% (armonico, neutro)].values
					armonicoC9 = df['Armónicos %s9 C%s Med'% (armonico, neutro)].values
					armonicoC10 = df['Armónicos %s10 C%s Med'% (armonico, neutro)].values
					armonicoC11 = df['Armónicos %s11 C%s Med'% (armonico, neutro)].values

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
						ws.write(z+1, 12, float(armonicoB1[z]))
						ws.write(z+1, 13, float(armonicoC1[z]))
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

			wb.save('armonicos THD %s.xls'%letra_armonico)
			ruta = 'armonicos THD %s.xls'%letra_armonico

		else:
			wb.save(nombre)
			ruta = nombre
		return ruta

	def eliminar(self):
		if path.exists('armonicos THD A.xls'):
			borrar = os.remove('armonicos THD A.xls')

		if path.exists('armonicos THD V.xls'):
			borrar = os.remove('armonicos THD V.xls')