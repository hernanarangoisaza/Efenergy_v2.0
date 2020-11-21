import math
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

class GraficaPotencia:

	def __init__(self):

		self.txt_fase_a = []
		self.txt_fase_b = []
		self.txt_fase_c = []

	def generar(self,parametro_en_analisis,ls_hora,ls_minuto,ls_tiempo,datos_potencia_reactiva_fase_a,datos_potencia_reactiva_fase_b,datos_potencia_reactiva_fase_c,txt_vs_horizontal,txt_vs_vertical):
		
		self.parametro_en_analisis = parametro_en_analisis
		
		potencia_reactiva_fase_b = []
		potencia_reactiva_fase_a = []
		potencia_reactiva_fase_c = []

		lista_hora = []
		lista_potencia_reactiva_fase_a = []
		lista_potencia_reactiva_fase_b = []
		lista_potencia_reactiva_fase_c = [] 

		suma_potencia_reactiva_fase_a = 0
		suma_potencia_reactiva_fase_b = 0
		suma_potencia_reactiva_fase_c = 0
		promedio_potencia_reactiva_fase_a = 0
		promedio_potencia_reactiva_fase_b = 0
		promedio_potencia_reactiva_fase_c = 0
		
		contador = -1
		pos = 0
		
		for i in range(len(datos_potencia_reactiva_fase_a)):
			# convertir numeros negativos a positivos
			potencia_reactiva_fase_a.append(math.fabs(datos_potencia_reactiva_fase_a[i]))
			potencia_reactiva_fase_b.append(math.fabs(datos_potencia_reactiva_fase_b[i]))
			potencia_reactiva_fase_c.append(math.fabs(datos_potencia_reactiva_fase_c[i]))
			contador += 1
			suma_potencia_reactiva_fase_a += float(potencia_reactiva_fase_a[i])
			suma_potencia_reactiva_fase_b += float(potencia_reactiva_fase_b[i])
			suma_potencia_reactiva_fase_c += float(potencia_reactiva_fase_c[i])

			if contador == 60:
				pos += i
				lista_hora.append(ls_hora[pos]+":"+ls_minuto[i]+ls_tiempo[pos])
				promedio_potencia_reactiva_fase_a = suma_potencia_reactiva_fase_a / contador
				promedio_potencia_reactiva_fase_b = suma_potencia_reactiva_fase_b / contador
				promedio_potencia_reactiva_fase_c = suma_potencia_reactiva_fase_c / contador
				lista_potencia_reactiva_fase_a.append(promedio_potencia_reactiva_fase_a)
				lista_potencia_reactiva_fase_b.append(promedio_potencia_reactiva_fase_b)
				lista_potencia_reactiva_fase_c.append(promedio_potencia_reactiva_fase_c)
				contador = 0
				pos = 0	
			
				suma_potencia_reactiva_fase_a = 0
				suma_potencia_reactiva_fase_b = 0
				suma_potencia_reactiva_fase_c = 0
				promedio_potencia_reactiva_fase_a = 0
				promedio_potencia_reactiva_fase_b = 0
				promedio_potencia_reactiva_fase_c = 0

		self.graficas(lista_hora, lista_potencia_reactiva_fase_a, lista_potencia_reactiva_fase_b, lista_potencia_reactiva_fase_c,txt_vs_horizontal,txt_vs_vertical)
	
	def graficas(self, lista_hora, lista_potencia_reactiva_fase_a, lista_potencia_reactiva_fase_b, lista_potencia_reactiva_fase_c,txt_vs_horizontal,txt_vs_vertical):
		fig, ax = plt.subplots()

		plt.grid(True)
		plt.grid(color = '0.5', linestyle = '--', linewidth = 1)

		self.l_potencia_reactiva_fase_a, = ax.plot(lista_hora, lista_potencia_reactiva_fase_a, 'o-', visible=True, lw=2, color='red',  mfc='red')
		self.l_potencia_reactiva_fase_b, = ax.plot(lista_hora, lista_potencia_reactiva_fase_b, 'o-', visible=True, lw=2, color='green', mfc='green' )
		self.l_potencia_reactiva_fase_c, = ax.plot(lista_hora, lista_potencia_reactiva_fase_c, 'o-', visible=True, lw=2 , color='blue', mfc='blue')
		
		if self.parametro_en_analisis == "voltaje":
			for i in range(len(lista_potencia_reactiva_fase_a)):
				if lista_potencia_reactiva_fase_a[i] > 139.7:
					plt.axhline(y = 139.7, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

				if lista_potencia_reactiva_fase_b[i] > 139.7:
					plt.axhline(y = 139.7, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

				if lista_potencia_reactiva_fase_c[i] > 139.7:
					plt.axhline(y = 139.7, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

				if lista_potencia_reactiva_fase_a[i] < 114.3:
					plt.axhline(y = 114.3, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

				if lista_potencia_reactiva_fase_b[i] < 114.3:
					plt.axhline(y = 114.3, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

				if lista_potencia_reactiva_fase_c[i] < 114.3:
					plt.axhline(y = 114.3, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

		plt.subplots_adjust(left=0.2, right=0.98, top=0.90, bottom=0.14)

		for i in range(len(lista_potencia_reactiva_fase_a)):
			self.txt_fase_a.append(ax.text(lista_hora[i], lista_potencia_reactiva_fase_a[i], ("%.3f"%lista_potencia_reactiva_fase_a[i]), visible=False, ha='center', va='bottom', color='black'))
			self.txt_fase_b.append(ax.text(lista_hora[i], lista_potencia_reactiva_fase_b[i], ("%.3f"%lista_potencia_reactiva_fase_b[i]), visible=False, ha='center', va='bottom', color='black'))
			self.txt_fase_c.append(ax.text(lista_hora[i], lista_potencia_reactiva_fase_c[i], ("%.3f"%lista_potencia_reactiva_fase_c[i]), visible=False, ha='center', va='bottom', color='black'))
		
		ax.set_title(txt_vs_vertical)
		plt.xlabel(txt_vs_horizontal)
		plt.xticks(rotation=45)

		plt.gca().legend(('fase A','fase B', 'fase C'), loc='center right') #estilos = fancybox=True, shadow=True  posicion = bbox_to_anchor=(0.5,-0.05), ncol=3, fancybox=False, loc='upper center'
		rax = plt.axes([0.01, 0.6, 0.1, 0.30])
		check = CheckButtons(rax, ('fase A', 'Datos A', 'fase B', 'Datos B', 'fase C', 'Datos C'), (True, False, True, False, True, False))

		check.on_clicked(self.func)
		
		plt.show()

	def func(self, label):
		if label == 'fase A':
			self.l_potencia_reactiva_fase_a.set_visible(not self.l_potencia_reactiva_fase_a.get_visible())
		elif label == 'fase B':
			self.l_potencia_reactiva_fase_b.set_visible(not self.l_potencia_reactiva_fase_b.get_visible())
		elif label == 'fase C':
			self.l_potencia_reactiva_fase_c.set_visible(not self.l_potencia_reactiva_fase_c.get_visible())

		for i in range(len(self.txt_fase_a)):
			if label == 'Datos A':
				self.txt_fase_a[i].set_visible(not self.txt_fase_a[i].get_visible())

			elif label == 'Datos B':
				self.txt_fase_b[i].set_visible(not self.txt_fase_b[i].get_visible())

			elif label == 'Datos C':
				self.txt_fase_c[i].set_visible(not self.txt_fase_c[i].get_visible())
		plt.draw()

