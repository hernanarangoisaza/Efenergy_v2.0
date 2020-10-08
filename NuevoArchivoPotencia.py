#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xlwt
import pandas
import os
import os.path as path

class NuevoArchivoPotencia:
	def CrearArchivo(self, archivo_excel, nombre, identificador):
		wb = xlwt.Workbook() #Crear excel vacio

		for i in archivo_excel.sheet_names:
			agregar_hojas = wb.add_sheet(i)
			agregar_hojas.write(0,0,'Fecha')
			agregar_hojas.write(0,1,'Hora')
			if identificador == 4:
				agregar_hojas.write(0,2,'Factor de Potencia AN Med')
				agregar_hojas.write(0,3,'Factor de Potencia BN Med')
				agregar_hojas.write(0,4,'Factor de Potencia CN Med')

			elif identificador == 5:
				agregar_hojas.write(0,2,'Potencia Reactiva AN Med')
				agregar_hojas.write(0,3,'Potencia Reactiva BN Med')
				agregar_hojas.write(0,4,'Potencia Reactiva CN Med')
			
			df = pandas.read_excel(archivo_excel, i) # leer archivo el item cada hoja
			for columnas in df.columns.tolist(): # Obtener nombre de columnas del excel
				fecha = df['Fecha'].values
				hora = df['Hora'].values

				if identificador == 4 and columnas == ('Factor de Potencia AN Med'):
					potencia_fase_a = df['Factor de Potencia AN Med'].values
					potencia_fase_b = df['Factor de Potencia BN Med'].values
					potencia_fase_c = df['Factor de Potencia CN Med'].values

					for item in range(len(hora)):
						agregar_hojas.write(item+1, 0, str(fecha[item]))
						agregar_hojas.write(item+1, 1, str(hora[item]))
						agregar_hojas.write(item+1, 2, float(potencia_fase_a[item]))
						agregar_hojas.write(item+1, 3, float(potencia_fase_b[item]))
						agregar_hojas.write(item+1, 4, float(potencia_fase_c[item]))


				elif identificador == 5 and columnas == ('Potencia Reactiva AN Med'):
					potencia_fase_a = df['Potencia Reactiva AN Med'].values
					potencia_fase_b = df['Potencia Reactiva BN Med'].values
					potencia_fase_c = df['Potencia Reactiva CN Med'].values

					for item in range(len(hora)):
						agregar_hojas.write(item+1, 0, str(fecha[item]))
						agregar_hojas.write(item+1, 1, str(hora[item]))
						agregar_hojas.write(item+1, 2, float(potencia_fase_a[item]))
						agregar_hojas.write(item+1, 3, float(potencia_fase_b[item]))
						agregar_hojas.write(item+1, 4, float(potencia_fase_c[item]))


		ruta = ''

		wb.save(nombre)
		ruta = nombre
		return ruta
