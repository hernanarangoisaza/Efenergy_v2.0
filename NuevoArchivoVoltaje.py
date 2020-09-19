#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlwt
import pandas as pd
import os
import os.path as path

class NuevoArchivoVoltaje:
	def CrearArchivo(self, archivo_excel, nombre):
		wb = xlwt.Workbook() #Crear excel vacio

		for i in archivo_excel.sheet_names:
			agregar_hojas = wb.add_sheet(i)
			agregar_hojas.write(0,0,'Fecha')
			agregar_hojas.write(0,1,'Hora')
			agregar_hojas.write(0,2,'Vrms ph-n AN Med')
			agregar_hojas.write(0,3,'Vrms ph-n BN Med')
			agregar_hojas.write(0,4,'Vrms ph-n CN Med')
			
			df = pd.read_excel(archivo_excel, i) # leer archivo el itemcada hoja
			for columnas in df.columns.tolist(): # Obtener nombre de columnas del excel
				if columnas == ('Vrms ph-n AN Med'):
					fecha = df['Fecha'].values
					hora = df['Hora'].values
					voltaje_fase_a = df['Vrms ph-n AN Med'].values
					voltaje_fase_b = df['Vrms ph-n BN Med'].values
					voltaje_fase_c = df['Vrms ph-n CN Med'].values

					for item in range(len(hora)):
						agregar_hojas.write(item+1, 0, str(fecha[item]))
						agregar_hojas.write(item+1, 1, str(hora[item]))
						agregar_hojas.write(item+1, 2, float(voltaje_fase_a[item]))
						agregar_hojas.write(item+1, 3, float(voltaje_fase_b[item]))
						agregar_hojas.write(item+1, 4, float(voltaje_fase_c[item]))

		ruta = ''

		wb.save(nombre)
		ruta = nombre
		return ruta
