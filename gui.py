from tkinter import *
import constantes

class Window():
    def __init__(self,title = 'Sort'):
        self.window = Tk()
        self.window.title(title)
        self.canvas = Canvas(width = constantes.width,
        height = constantes.height,
        bg = 'white')
        self.canvas.grid()
