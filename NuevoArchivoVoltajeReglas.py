#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlwt
import pandas as pd
import os
import easygui as eg 
import os.path as path

class NuevoArchivoVoltajeReglas:
	def CrearArchivo(self,archivo_excel,estado_voltaje):
		extension = "*.xls"
		nombre = eg.filesavebox(msg="Guardar archivo",
							title="Control: filesavebox",
							default=extension,
							filetypes=extension)

		self.rango_mayor = float(127 + (127 * (10 / 100)))
		self.rango_menor = float(127 - (127 * (10 / 100)))

		if nombre is not None:
			nuevo_archivo_excel = xlwt.Workbook() #Crear excel vacio
			for i in archivo_excel.sheet_names:
				agregar_hojas = nuevo_archivo_excel.add_sheet(i)
				agregar_hojas.write(0,0,'Fecha')
				agregar_hojas.write(0,1,'Hora')
				agregar_hojas.write(0,2,'Vrms ph-n AN Med')

				agregar_hojas.write(0,4,'Fecha')
				agregar_hojas.write(0,5,'Hora')
				agregar_hojas.write(0,6,'Vrms ph-n BN Med')

				agregar_hojas.write(0,8,'Fecha')
				agregar_hojas.write(0,9,'Hora')
				agregar_hojas.write(0,10,'Vrms ph-n CN Med')

				df = pd.read_excel(archivo_excel, i)
				for columna in df.columns.tolist():
					if columna == ('Vrms ph-n CN Med'):
						self.fecha = []
						fecha_larga = df['Fecha']
						for i in fecha_larga:
							self.fecha.append(str(i).rstrip(':0'))

						self.hora = df['Hora'].values
						voltaje_fase_a = df['Vrms ph-n AN Med'].values
						voltaje_fase_b = df['Vrms ph-n BN Med'].values
						voltaje_fase_c = df['Vrms ph-n CN Med'].values
						
						if estado_voltaje == "RANGO":
							lista_fecha_fase_a, lista_hora_fase_a, lista_voltaje_fase_a = self.pruebaRango(voltaje_fase_a)
							lista_fecha_fase_b, lista_hora_fase_b, lista_voltaje_fase_b = self.pruebaRango(voltaje_fase_b)
							lista_fecha_fase_c, lista_hora_fase_c, lista_voltaje_fase_c = self.pruebaRango(voltaje_fase_c)	
							
							for item in range(len(lista_hora_fase_a)):
								agregar_hojas.write(item+1, 0, str(lista_fecha_fase_a[item]))
								agregar_hojas.write(item+1, 1, str(lista_hora_fase_a[item]))
								agregar_hojas.write(item+1, 2, float(lista_voltaje_fase_a[item]))
							
							for item in range(len(lista_hora_fase_b)):
								agregar_hojas.write(item+1, 4, str(lista_fecha_fase_b[item]))
								agregar_hojas.write(item+1, 5, str(lista_hora_fase_b[item]))
								agregar_hojas.write(item+1, 6, float(lista_voltaje_fase_b[item]))
							
							for item in range(len(lista_hora_fase_c)):
								agregar_hojas.write(item+1, 8, str(lista_fecha_fase_c[item]))
								agregar_hojas.write(item+1, 9, str(lista_hora_fase_c[item]))
								agregar_hojas.write(item+1, 10, float(lista_voltaje_fase_c[item]))

						elif estado_voltaje == "MAYOR":
							lista_fecha_fase_a, lista_hora_fase_a, lista_voltaje_fase_a = self.pruebaMayor(voltaje_fase_a)
							lista_fecha_fase_b, lista_hora_fase_b, lista_voltaje_fase_b = self.pruebaMayor(voltaje_fase_b)
							lista_fecha_fase_c, lista_hora_fase_c, lista_voltaje_fase_c = self.pruebaMayor(voltaje_fase_c)	
							
							for item in range(len(lista_hora_fase_a)):
								agregar_hojas.write(item+1, 0, str(lista_fecha_fase_a[item]))
								agregar_hojas.write(item+1, 1, str(lista_hora_fase_a[item]))
								agregar_hojas.write(item+1, 2, float(lista_voltaje_fase_a[item]))
							
							for item in range(len(lista_hora_fase_b)):
								agregar_hojas.write(item+1, 4, str(lista_fecha_fase_b[item]))
								agregar_hojas.write(item+1, 5, str(lista_hora_fase_b[item]))
								agregar_hojas.write(item+1, 6, float(lista_voltaje_fase_b[item]))
							
							for item in range(len(lista_hora_fase_c)):
								agregar_hojas.write(item+1, 8, str(lista_fecha_fase_c[item]))
								agregar_hojas.write(item+1, 9, str(lista_hora_fase_c[item]))
								agregar_hojas.write(item+1, 10, float(lista_voltaje_fase_c[item]))

						elif estado_voltaje == "MENOR":
							lista_fecha_fase_a, lista_hora_fase_a, lista_voltaje_fase_a = self.pruebaMenor(voltaje_fase_a)
							lista_fecha_fase_b, lista_hora_fase_b, lista_voltaje_fase_b = self.pruebaMenor(voltaje_fase_b)
							lista_fecha_fase_c, lista_hora_fase_c, lista_voltaje_fase_c = self.pruebaMenor(voltaje_fase_c)	
							
							for item in range(len(lista_fecha_fase_a)):
								agregar_hojas.write(item+1, 0, str(lista_fecha_fase_a[item]))
								agregar_hojas.write(item+1, 1, str(lista_hora_fase_a[item]))
								agregar_hojas.write(item+1, 2, float(lista_voltaje_fase_a[item]))
							
							for item in range(len(lista_hora_fase_b)):
								agregar_hojas.write(item+1, 4, str(lista_fecha_fase_b[item]))
								agregar_hojas.write(item+1, 5, str(lista_hora_fase_b[item]))
								agregar_hojas.write(item+1, 6, float(lista_voltaje_fase_b[item]))
							
							for item in range(len(lista_hora_fase_c)):
								agregar_hojas.write(item+1, 8, str(lista_fecha_fase_c[item]))
								agregar_hojas.write(item+1, 9, str(lista_hora_fase_c[item]))
								agregar_hojas.write(item+1, 10, float(lista_voltaje_fase_c[item]))
			ruta = ''

			nuevo_archivo_excel.save(nombre)
			ruta = nombre
			return ruta


	def pruebaRango(self, voltage_fase):
		lista_fecha = []
		lista_hora = []
		lista_rango = []
		posicion_item = 0
		for i in range(len(voltage_fase)):
			if voltage_fase[i] < self.rango_mayor and voltage_fase[i] > self.rango_menor:
				posicion_item += i
				lista_rango.append(voltage_fase[posicion_item])
				lista_fecha.append(self.fecha[posicion_item])
				lista_hora.append(self.hora[posicion_item])
				posicion_item = 0
		return lista_fecha, lista_hora,lista_rango 
	
	def pruebaMenor(self,voltage_fase):
		lista_fecha = []
		lista_hora = []
		lista_menores = []
		posicion_item = 0

		for i in range(len(voltage_fase)):
			if voltage_fase[i] < self.rango_menor:
				posicion_item += i
				lista_menores.append(voltage_fase[posicion_item])
				lista_fecha.append(self.fecha[posicion_item])
				lista_hora.append(self.hora[posicion_item])
				posicion_item = 0
		return lista_fecha, lista_hora,lista_menores 
			
	def pruebaMayor(self,voltage_fase):
		lista_fecha = []
		lista_hora = []
		lista_mayores = []
		posicion_item = 0
		for i in range(len(voltage_fase)):
			if voltage_fase[i] > self.rango_mayor:
				posicion_item += i
				lista_mayores.append(voltage_fase[posicion_item])
				lista_fecha.append(self.fecha[posicion_item])
				lista_hora.append(self.hora[posicion_item])
				posicion_item = 0
		return lista_fecha, lista_hora,lista_mayores 
		