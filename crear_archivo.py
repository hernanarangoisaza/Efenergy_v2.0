#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlwt
import pandas as pd
import os

class NuevoArchivo:
	def CrearArchivo(self, archivo_excel):
		wb = xlwt.Workbook()
		encontrado = False
		for i in archivo_excel.sheet_names:
			ws = wb.add_sheet(i)
			ws.write(0,0,'Fecha')
			ws.write(0,1,'Hora')
			ws.write(0,2,'THD V AN Med')
			ws.write(0,3,'THD V BN Med')
			ws.write(0,4,'THD V CN Med')
			ws.write(0,5,'Armónicos Tensión0 AN Med')
			ws.write(0,6,'Armónicos Tensión0 BN Med')
			ws.write(0,7,'Armónicos Tensión0 CN Med')
			ws.write(0,8,'Armónicos Tensión1 AN Med')
			ws.write(0,9,'Armónicos Tensión1 BN Med')
			ws.write(0,10,'Armónicos Tensión1 CN Med')
			ws.write(0,11,'Armónicos Tensión2 AN Med')
			ws.write(0,12,'Armónicos Tensión2 BN Med')
			ws.write(0,13,'Armónicos Tensión2 CN Med')
			ws.write(0,14,'Armónicos Tensión3 AN Med')
			ws.write(0,15,'Armónicos Tensión3 BN Med')
			ws.write(0,16,'Armónicos Tensión3 CN Med')
			ws.write(0,17,'Armónicos Tensión4 AN Med')
			ws.write(0,18,'Armónicos Tensión4 BN Med')
			ws.write(0,19,'Armónicos Tensión4 CN Med')
			ws.write(0,20,'Armónicos Tensión5 AN Med')
			ws.write(0,21,'Armónicos Tensión5 BN Med')
			ws.write(0,22,'Armónicos Tensión5 CN Med')
			ws.write(0,23,'Armónicos Tensión6 AN Med')
			ws.write(0,24,'Armónicos Tensión6 BN Med')
			ws.write(0,25,'Armónicos Tensión6 CN Med')
			ws.write(0,26,'Armónicos Tensión7 AN Med')
			ws.write(0,27,'Armónicos Tensión7 BN Med')
			ws.write(0,28,'Armónicos Tensión7 CN Med')
			ws.write(0,29,'Armónicos Tensión8 AN Med')
			ws.write(0,30,'Armónicos Tensión8 BN Med')
			ws.write(0,31,'Armónicos Tensión8 CN Med')
			ws.write(0,32,'Armónicos Tensión9 AN Med')
			ws.write(0,33,'Armónicos Tensión9 BN Med')
			ws.write(0,34,'Armónicos Tensión9 CN Med')
			ws.write(0,35,'Armónicos Tensión10 AN Med')
			ws.write(0,36,'Armónicos Tensión10 BN Med')
			ws.write(0,37,'Armónicos Tensión10 CN Med')
			ws.write(0,38,'Armónicos Tensión11 AN Med')
			ws.write(0,39,'Armónicos Tensión11 BN Med')
			ws.write(0,40,'Armónicos Tensión11 CN Med')
			df = pd.read_excel(archivo_excel, i)
			for z in df.columns.tolist():
				if z == 'THD V AN Med':
					encontrado = True
					fecha = df['Fecha'].values
					hora = df['Hora'].values
					thdvA = df['THD V AN Med'].values
					thdvB = df['THD V BN Med'].values
					thdvC = df['THD V CN Med'].values
					armonico0 = df['Armónicos Tensión0 AN Med'].values
					armonico1 = df['Armónicos Tensión1 AN Med'].values
					armonico2 = df['Armónicos Tensión2 AN Med'].values
					armonico3 = df['Armónicos Tensión3 AN Med'].values
					armonico4 = df['Armónicos Tensión4 AN Med'].values
					armonico5 = df['Armónicos Tensión5 AN Med'].values
					armonico6 = df['Armónicos Tensión6 AN Med'].values
					armonico7 = df['Armónicos Tensión7 AN Med'].values
					armonico8 = df['Armónicos Tensión8 AN Med'].values
					armonico9 = df['Armónicos Tensión9 AN Med'].values
					armonico10 = df['Armónicos Tensión10 AN Med'].values
					armonico11 = df['Armónicos Tensión11 AN Med'].values

					armonicoB0 = df['Armónicos Tensión0 BN Med'].values
					armonicoB1 = df['Armónicos Tensión1 BN Med'].values
					armonicoB2 = df['Armónicos Tensión2 BN Med'].values
					armonicoB3 = df['Armónicos Tensión3 BN Med'].values
					armonicoB4 = df['Armónicos Tensión4 BN Med'].values
					armonicoB5 = df['Armónicos Tensión5 BN Med'].values
					armonicoB6 = df['Armónicos Tensión6 BN Med'].values
					armonicoB7 = df['Armónicos Tensión7 BN Med'].values
					armonicoB8 = df['Armónicos Tensión8 BN Med'].values
					armonicoB9 = df['Armónicos Tensión9 BN Med'].values
					armonicoB10 = df['Armónicos Tensión10 BN Med'].values
					armonicoB11 = df['Armónicos Tensión11 BN Med'].values

					armonicoC0 = df['Armónicos Tensión0 CN Med'].values
					armonicoC1 = df['Armónicos Tensión1 CN Med'].values
					armonicoC2 = df['Armónicos Tensión2 CN Med'].values
					armonicoC3 = df['Armónicos Tensión3 CN Med'].values
					armonicoC4 = df['Armónicos Tensión4 CN Med'].values
					armonicoC5 = df['Armónicos Tensión5 CN Med'].values
					armonicoC6 = df['Armónicos Tensión6 CN Med'].values
					armonicoC7 = df['Armónicos Tensión7 CN Med'].values
					armonicoC8 = df['Armónicos Tensión8 CN Med'].values
					armonicoC9 = df['Armónicos Tensión9 CN Med'].values
					armonicoC10 = df['Armónicos Tensión10 CN Med'].values
					armonicoC11 = df['Armónicos Tensión11 CN Med'].values

					for y in range(len(hora)):
						ws.write(y+1, 0, str(fecha[y]))
						ws.write(y+1, 1, str(hora[y]))
						ws.write(y+1, 2, float(thdvA[y]))
						ws.write(y+1, 3, float(thdvB[y]))
						ws.write(y+1, 4, float(thdvC[y]))
						ws.write(y+1, 5, float(armonico0[y]))
						ws.write(y+1, 6, float(armonicoB0[y]))
						ws.write(y+1, 7, float(armonicoC0[y]))
						ws.write(y+1, 8, float(armonico1[y]))
						ws.write(y+1, 9, float(armonicoB0[y]))
						ws.write(y+1, 10, float(armonicoC0[y]))
						ws.write(y+1, 11, float(armonico2[y]))
						ws.write(y+1, 12, float(armonicoB2[y]))
						ws.write(y+1, 13, float(armonicoC2[y]))
						ws.write(y+1, 14, float(armonico3[y]))
						ws.write(y+1, 15, float(armonicoB3[y]))
						ws.write(y+1, 16, float(armonicoC3[y]))
						ws.write(y+1, 17, float(armonico4[y]))
						ws.write(y+1, 18, float(armonicoB4[y]))
						ws.write(y+1, 19, float(armonicoC4[y]))
						ws.write(y+1, 20, float(armonico5[y]))
						ws.write(y+1, 21, float(armonicoB5[y]))
						ws.write(y+1, 22, float(armonicoC5[y]))
						ws.write(y+1, 23, float(armonico6[y]))
						ws.write(y+1, 24, float(armonicoB6[y]))
						ws.write(y+1, 25, float(armonicoC6[y]))
						ws.write(y+1, 26, float(armonico7[y]))
						ws.write(y+1, 27, float(armonicoB7[y]))
						ws.write(y+1, 28, float(armonicoC7[y]))
						ws.write(y+1, 29, float(armonico8[y]))
						ws.write(y+1, 30, float(armonicoB8[y]))
						ws.write(y+1, 31, float(armonicoC8[y]))
						ws.write(y+1, 32, float(armonico9[y]))
						ws.write(y+1, 33, float(armonicoB9[y]))
						ws.write(y+1, 34, float(armonicoC9[y]))
						ws.write(y+1, 35, float(armonico10[y]))
						ws.write(y+1, 36, float(armonicoB10[y]))
						ws.write(y+1, 37, float(armonicoC10[y]))
						ws.write(y+1, 38, float(armonico11[y]))
						ws.write(y+1, 39, float(armonicoB11[y]))
						ws.write(y+1, 40, float(armonicoC11[y]))

		wb.save('armonicos.xls')
		ruta = 'armonicos.xls'
		if encontrado == True:
			return ruta
		return archivo_excel

	def Cerrar(self):
		self.borrar = os.remove('armonicos.xls')
		return self.borrar



