from tkinter import *
import random

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title('Dice Simulator')

        self.root.geometry('580x400')
        self.root.config(bg='#069c71', pady=1, padx=10)
        self.root.resizable(False,False) #change this to ratio (?)

        self.root.mainloop()