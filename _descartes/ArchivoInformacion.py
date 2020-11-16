#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ArchivoInformacion():

	def __init__(self, archivo):

		self.archivo_texto = archivo

	def leer_archivo(self):

		archivo = open(self.archivo_texto, "r")
		lineas = archivo.read().split("&")
		archivo.close()
		return lineas

	def escribir_archivo(self, informacion):

		archivo = open(self.archivo_texto, "w")

		for info in informacion:

			archivo.write(info)

		archivo.close()
