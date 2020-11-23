#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from Efenergy2Globales import *

import math
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# ************************************************************************************************************************

class Efenergy2GraficoTipo1:

    def __init__(self):

        self.txtFaseA = []
        self.txtFaseB = []
        self.txtFaseC = []

    # ************************************************************************************************************************

    def generar(self, 
                idProceso, 
                lsHora, 
                lsMinuto, 
                lsAmPm, 
                datosFaseA, 
                datosFaseB, 
                datosFaseC, 
                txtEjeHorizontal, 
                txtEjeVertical):
        
        self.idProceso = idProceso
        
        faseA = []
        faseB = []
        faseC = []

        listaHora = []

        listaFaseA = []
        listaFaseB = []
        listaFaseC = [] 

        sumaFaseA = 0
        sumaFaseB = 0
        sumaFaseC = 0

        promedioFaseA = 0
        promedioFaseB = 0
        promedioFaseC = 0
        
        contador = -1
        pos = 0
        
        for i in range(len(datosFaseA)):

            # convertir numeros negativos a positivos

            faseA.append(math.fabs(datosFaseA[i]))
            faseB.append(math.fabs(datosFaseB[i]))
            faseC.append(math.fabs(datosFaseC[i]))

            contador += 1

            sumaFaseA += float(faseA[i])
            sumaFaseB += float(faseB[i])
            sumaFaseC += float(faseC[i])

            if contador == 60:

                pos += i

                listaHora.append(lsHora[pos]+":"+lsMinuto[i]+lsAmPm[pos])

                promedioFaseA = sumaFaseA / contador
                promedioFaseB = sumaFaseB / contador
                promedioFaseC = sumaFaseC / contador

                listaFaseA.append(promedioFaseA)
                listaFaseB.append(promedioFaseB)
                listaFaseC.append(promedioFaseC)

                contador = 0
                pos = 0    
            
                sumaFaseA = 0
                sumaFaseB = 0
                sumaFaseC = 0

                promedioFaseA = 0
                promedioFaseB = 0
                promedioFaseC = 0

        self.graficar(listaHora, listaFaseA, listaFaseB, listaFaseC, txtEjeHorizontal, txtEjeVertical)
    
    # ************************************************************************************************************************

    def graficar(self, listaHora, listaFaseA, listaFaseB, listaFaseC, txtEjeHorizontal, txtEjeVertical):

        fig, ax = plt.subplots()

        plt.grid(True)
        plt.grid(color = '0.5', linestyle = '--', linewidth = 1)

        self.lineaFaseA, = ax.plot(listaHora, listaFaseA, 'o-', visible=True, lw=2, color='red',  mfc='red')
        self.lineaFaseB, = ax.plot(listaHora, listaFaseB, 'o-', visible=True, lw=2, color='green', mfc='green' )
        self.lineaFaseC, = ax.plot(listaHora, listaFaseC, 'o-', visible=True, lw=2 , color='blue', mfc='blue')
        
        if self.idProceso == idVoltaje:

            for i in range(len(listaFaseA)):

                if listaFaseA[i] > 139.7:

                    plt.axhline(y = 139.7, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

                if listaFaseB[i] > 139.7:

                    plt.axhline(y = 139.7, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

                if listaFaseC[i] > 139.7:

                    plt.axhline(y = 139.7, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

                if listaFaseA[i] < 114.3:

                    plt.axhline(y = 114.3, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

                if listaFaseB[i] < 114.3:

                    plt.axhline(y = 114.3, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

                if listaFaseC[i] < 114.3:

                    plt.axhline(y = 114.3, xmin = 0, xmax = 1, color='#387B7F', linestyle='--', lw=2)

        plt.subplots_adjust(left=0.2, right=0.98, top=0.90, bottom=0.14)

        for i in range(len(listaFaseA)):

            self.txtFaseA.append(ax.text(listaHora[i], listaFaseA[i], ("%.3f"%listaFaseA[i]), visible=False, ha='center', va='bottom', color='black'))
            self.txtFaseB.append(ax.text(listaHora[i], listaFaseB[i], ("%.3f"%listaFaseB[i]), visible=False, ha='center', va='bottom', color='black'))
            self.txtFaseC.append(ax.text(listaHora[i], listaFaseC[i], ("%.3f"%listaFaseC[i]), visible=False, ha='center', va='bottom', color='black'))
        
        ax.set_title(txtEjeVertical)
        plt.xlabel(txtEjeHorizontal)
        plt.xticks(rotation=45)

        plt.gca().legend(('Fase A','Fase B', 'Fase C'), loc='center right') 

        #estilos = fancybox=True, shadow=True  posicion = bbox_to_anchor=(0.5,-0.05), ncol=3, fancybox=False, loc='upper center'
        
        rax = plt.axes([0.01, 0.6, 0.1, 0.30])

        check = CheckButtons(rax, ('Fase A', 'Datos A', 'Fase B', 'Datos B', 'Fase C', 'Datos C'), (True, False, True, False, True, False))

        check.on_clicked(self.selectorLineas)
        
        plt.show()

    # ************************************************************************************************************************

    def selectorLineas(self, label):

        if label == 'Fase A':

            self.lineaFaseA.set_visible(not self.lineaFaseA.get_visible())

        elif label == 'Fase B':

            self.lineaFaseB.set_visible(not self.lineaFaseB.get_visible())

        elif label == 'Fase C':

            self.lineaFaseC.set_visible(not self.lineaFaseC.get_visible())

        for i in range(len(self.txtFaseA)):

            if label == 'Datos A':

                self.txtFaseA[i].set_visible(not self.txtFaseA[i].get_visible())

            elif label == 'Datos B':

                self.txtFaseB[i].set_visible(not self.txtFaseB[i].get_visible())

            elif label == 'Datos C':

                self.txtFaseC[i].set_visible(not self.txtFaseC[i].get_visible())

        plt.draw()

    # ************************************************************************************************************************
