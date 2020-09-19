import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.widgets import Slider
import numpy as np
from matplotlib.widgets import CheckButtons

style.use("ggplot")
class GraficaBarras:
    def __init__(self, id, lista_hora, lista_thda, lista_armonico0, lista_armonico1, lista_armonico2, lista_armonico3, lista_armonico4, lista_armonico5, lista_armonico6, lista_armonico7, lista_armonico8, lista_armonico9, lista_armonico10, lista_armonico11 ):  
        self.id = id
        self.lista_hora = lista_hora
        self.lista_thda = lista_thda
        self.lista_armonico0 = lista_armonico0
        self.lista_armonico1 = lista_armonico1
        self.lista_armonico2 = lista_armonico2
        self.lista_armonico3 = lista_armonico3
        self.lista_armonico4 = lista_armonico4
        self.lista_armonico5 = lista_armonico5
        self.lista_armonico6 = lista_armonico6
        self.lista_armonico7 = lista_armonico7
        self.lista_armonico8 = lista_armonico8
        self.lista_armonico9 = lista_armonico9
        self.lista_armonico10 = lista_armonico10
        self.lista_armonico11 = lista_armonico11

        self.txt_thd = []
        self.txt_corriente_fundamental = []
        self.txt_armonico1 = []
        self.txt_armonico2 = []
        self.txt_armonico3 = []
        self.txt_armonico4 = []
        self.txt_armonico5 = []
        self.txt_armonico6 = []
        self.txt_armonico7 = []
        self.txt_armonico8 = []
        self.txt_armonico9 = []
        self.txt_armonico10 = []
        self.txt_armonico11 = []

        self.letra_armonico = ['A', 'V']

        self.fig,self.ax=plt.subplots()
        
        self.N=2
        self.slider(self.N)
        

    def slider(self,N):
        barpos = plt.axes([0.18, 0.01, 0.70, 0.03], facecolor="gray")
        slider = Slider(barpos, '', 0, len(self.lista_hora)-N, valinit=0)
        slider.on_changed(self.bar)

        
        rax = plt.axes([0.01, 0.30, 0.12, 0.65])
        check = CheckButtons(rax, ('C. Fund.', 'Arm. 1', 'Arm. 2', 'Arm. 3', 'Arm. 4',
        'Arm. 5', 'Arm. 6', 'Arm. 7', 'Arm. 8', 'Arm. 9', 'Arm. 10', 'Arm. 11'), (True, True, 
        True, True, True, True, True, True, True, True, True, True))
        check.get_status()

        check.on_clicked(self.func)
        self.bar(0)
        plt.show()


    def bar(self,pos):

        pos = int(pos)
        self.ax.clear()
        if pos+self.N > len(self.lista_hora): 
            n=len(self.lista_hora)-pos
        else:
            n=self.N
        X=self.lista_hora[pos:pos+n]
        Y=self.lista_thda[pos:pos+n]
        self.Y0=self.lista_armonico0[pos:pos+n]
        Y1=self.lista_armonico1[pos:pos+n]
        Y2=self.lista_armonico2[pos:pos+n]
        Y3=self.lista_armonico3[pos:pos+n]
        Y4=self.lista_armonico4[pos:pos+n]
        Y5=self.lista_armonico5[pos:pos+n]
        Y6=self.lista_armonico6[pos:pos+n]
        Y7=self.lista_armonico7[pos:pos+n]
        Y8=self.lista_armonico8[pos:pos+n]
        Y9=self.lista_armonico9[pos:pos+n]
        Y10=self.lista_armonico10[pos:pos+n]
        Y11=self.lista_armonico11[pos:pos+n]


        ind = np.arange(len(X))
        self.b_corriente_fundamental = self.ax.bar(X,self.Y0,width=0.06,visible=True,align='edge', data=None, label='C. Fund.',color='#94FF3F',ecolor='black')
        self.b_armonico1 = self.ax.bar(ind+0.06,Y1,width=0.06,visible=True,align='edge',label='Arm. 1',color='#FF4618',ecolor='black')
        self.b_armonico2 = self.ax.bar(ind+0.12,Y2,width=0.06,visible=True,align='edge',label='Arm. 2',color='#1DC0CC',ecolor='black')
        self.b_armonico3 = self.ax.bar(ind+0.18,Y3,width=0.06,visible=True,align='edge',label='Arm. 3',color='#77CC32',ecolor='black')
        self.b_armonico4 = self.ax.bar(ind+0.24,Y4,width=0.06,visible=True,align='edge',label='Arm. 4',color='#CC3813',ecolor='black')
        self.b_armonico5 = self.ax.bar(ind+0.3,Y5,width=0.06,visible=True,align='edge',label='Arm. 5',color='#24F0FF',ecolor='black')
        self.b_armonico6 = self.ax.bar(ind+0.36,Y6,width=0.06,visible=True,align='edge',label='Arm. 6',color='#BFFF8E',ecolor='black')
        self.b_armonico7 = self.ax.bar(ind+0.42,Y7,width=0.06,visible=True,align='edge',label='Arm. 7',color='#FF8465',ecolor='black')
        self.b_armonico8 = self.ax.bar(ind+0.48,Y8,width=0.06,visible=True,align='edge',label='Arm. 8',color='#387B7F',ecolor='black')
        self.b_armonico9 = self.ax.bar(ind+0.54,Y9,width=0.06,visible=True,align='edge',label='Arm. 9',color='#4A7F1F',ecolor='black')
        self.b_armonico10 = self.ax.bar(ind+0.60,Y10,width=0.06,visible=True,align='edge',label='Arm. 10',color='#FF7A7A',ecolor='black')
        self.b_armonico11 = self.ax.bar(ind+0.66,Y11,width=0.06,visible=True,align='edge',label='Arm. 11',color='#3FFF1F',ecolor='black')

        plt.subplots_adjust(left=0.15, right=0.98, top=0.95, bottom=0.25)

        thd = []
        for i,txt in enumerate(Y):
            thd.append(txt)
            
        for i,txt in enumerate(self.Y0):
            self.txt_corriente_fundamental.append(self.ax.annotate(txt, (X[i],self.Y0[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y1):
            self.txt_armonico1.append(self.ax.annotate(txt, (ind[i]+0.06,Y1[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y2):
            self.txt_armonico2.append(self.ax.annotate(txt, (ind[i]+0.12,Y2[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y3):
            self.txt_armonico3.append(self.ax.annotate(txt, (ind[i]+0.18,Y3[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y4):
            self.txt_armonico4.append(self.ax.annotate(txt, (ind[i]+0.24,Y4[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y5):
            self.txt_armonico5.append(self.ax.annotate(txt, (ind[i]+0.3,Y5[i]),visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y6):
            self.txt_armonico6.append(self.ax.annotate(txt, (ind[i]+0.36,Y6[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y7):
            self.txt_armonico7.append(self.ax.annotate(txt, (ind[i]+0.42,Y7[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y8):
            self.txt_armonico8.append(self.ax.annotate(txt, (ind[i]+0.48,Y8[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y9):
            self.txt_armonico9.append(self.ax.annotate(txt, (ind[i]+0.54,Y9[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y10):
            self.txt_armonico10.append(self.ax.annotate(txt, (ind[i]+0.60,Y10[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
        for i,txt in enumerate(Y11):
            self.txt_armonico11.append(self.ax.annotate(txt, (ind[i]+0.66,Y11[i]), visible=True, ha='center', va='bottom', fontsize=8, rotation=45, color='black'))
       # miercoles 10 Am 
        armonico = ["Corriente","Tensión"]
        self.ax.set_title('Armónicos de %s'%armonico[self.id - 1] )
   
        plt.text(x = 2, y = 1, s = 'THD%s: %s'%(self.letra_armonico[self.id - 1],thd[0]),
         fontsize = 8,
            bbox={'facecolor':'white', 'alpha':0.99, 'pad':5})
        plt.text(x = 6.7, y = 1, s = 'THD%s: %s'%(self.letra_armonico[self.id - 1],thd[1]), fontsize = 8,
            bbox={'facecolor':'white', 'alpha':0.99, 'pad':5})
        self.ax.xaxis.set_ticks(X)
        self.ax.yaxis.set_ticks([])
        #box = dict(facecolor='green', pad=5, alpha=0.2)
        #self.ax.set_xlabel('Tiempo(Minuto)', bbox=box)
        self.ax.legend(loc='upper center', bbox_to_anchor=(0.45, -0.07),
          fancybox=True, shadow=True, ncol=5)

        
    def func(self, label):
        for i in range(self.N):
            if label == 'C. Fund.':
                self.b_corriente_fundamental[i].set_visible(not self.b_corriente_fundamental[i].get_visible())
                    

            elif label == 'Arm. 1':
                self.b_armonico1[i].set_visible(not self.b_armonico1[i].get_visible())
                self.txt_armonico1[i].set_visible(not self.txt_armonico1[i].get_visible())

            elif label == 'Arm. 2':
                self.b_armonico2[i].set_visible(not self.b_armonico2[i].get_visible())
                self.txt_armonico2[i].set_visible(not self.txt_armonico2[i].get_visible())

            elif label == 'Arm. 3':
                self.b_armonico3[i].set_visible(not self.b_armonico3[i].get_visible())
                self.txt_armonico3[i].set_visible(not self.txt_armonico3[i].get_visible())

            elif label == 'Arm. 4':
                self.b_armonico4[i].set_visible(not self.b_armonico4[i].get_visible())
                self.txt_armonico4[i].set_visible(not self.txt_armonico4[i].get_visible())

            elif label == 'Arm. 5':
                self.b_armonico5[i].set_visible(not self.b_armonico5[i].get_visible())
                self.txt_armonico5[i].set_visible(not self.txt_armonico5[i].get_visible())

            elif label == 'Arm. 6':
                self.b_armonico6[i].set_visible(not self.b_armonico6[i].get_visible())
                self.txt_armonico6[i].set_visible(not self.txt_armonico6[i].get_visible())

            elif label == 'Arm. 7':
                self.b_armonico7[i].set_visible(not self.b_armonico7[i].get_visible())
                self.txt_armonico7[i].set_visible(not self.txt_armonico7[i].get_visible())

            elif label == 'Arm. 8':
                self.b_armonico8[i].set_visible(not self.b_armonico8[i].get_visible())
                self.txt_armonico8[i].set_visible(not self.txt_armonico8[i].get_visible())

            elif label == 'Arm. 9':
                self.b_armonico9[i].set_visible(not self.b_armonico9[i].get_visible())
                self.txt_armonico9[i].set_visible(not self.txt_armonico9[i].get_visible())

            elif label == 'Arm. 10':
                self.b_armonico10[i].set_visible(not self.b_armonico10[i].get_visible())
                self.txt_armonico10[i].set_visible(not self.txt_armonico10[i].get_visible())

            elif label == 'Arm. 11':
                self.b_armonico11[i].set_visible(not self.b_armonico11[i].get_visible())
                self.txt_armonico11[i].set_visible(not self.txt_armonico11[i].get_visible())



            if label == 'C. Fund.':
                for y in range(len(self.Y0)):
                    self.txt_corriente_fundamental[i].set_visible(not self.txt_corriente_fundamental[y].get_visible())    

        plt.draw()
    '''def txtBarra(self, X, Y):
                    while True:
                        for i,txt in enumerate(Y):
                            txt = self.ax.annotate(txt, (X[i],Y[i]))
                            return txt'''