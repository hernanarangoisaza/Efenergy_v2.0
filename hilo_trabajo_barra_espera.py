import wx
import threading

''' ejecuta en segundo plano hasta que numero_iteraciones sea igual a MAX_COUNT  '''
class WorkerThread(threading.Thread):
    MAX_COUNT = 100
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback = callback

    def run(self):
        lista= []
        for numero_iteraciones in range(WorkerThread.MAX_COUNT):            
            print(numero_iteraciones)
            wx.MilliSleep(100)
            wx.CallAfter(self.callback, numero_iteraciones)

        # envia la señal -1 para cuando el bucle termine
        wx.CallAfter(self.callback, -1)

    