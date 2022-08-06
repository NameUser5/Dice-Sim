from tkinter import *
import random

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title('Dice Simulator')

        self.root.geometry('580x400')
        self.root.config(bg='#069c71', pady=1, padx=10)
        self.root.resizable(False,False) #change this to ratio (?)

        self.current_die = PhotoImage(file=r'images\1.png').subsample(9,9)
        self.die_display = Label(image=self.current_die, bg='#069c71')
        self.die_display.grid(row=2, column=2)

        self.chips = PhotoImage(file='images\chips.png').subsample(3,3)
        self.chips_label = Label(image=self.chips, bg='#069c71')
        self.chips_label.grid(row=4, column=1)

        self.cigar = PhotoImage(file='images\cigar.png').subsample(3, 3)
        self.cigar_label = Label(image=self.cigar, bg='#069c71')
        self.cigar_label.grid(row=4, column=2)

        self.cards = PhotoImage(file='images\cards.png').subsample(3, 3)
        self.cards_label = Label(image=self.cards, bg='#069c71')
        self.cards_label.grid(row=4, column=3)

        self.roll_button = Button(text="Roll", command=lambda: self.roll_dice)
        self.roll_button.grid(row=3, column=2)

        self.root.mainloop()