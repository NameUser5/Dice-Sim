from tkinter import *
import random

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title('Dice Simulator')

        self.root.geometry('580x400')
        self.root.config(bg='#069c71', pady=1, padx=10)
        self.root.resizable(False,False) #change this to ratio (?)

        ## Die display:
        self.current_die = PhotoImage(file=r'images\blank.png').subsample(9,9)
        self.die_display = Label(image=self.current_die, bg='#069c71')
        self.die_display.grid(row=2, column=2)

        self.blank = PhotoImage(file=r'images\blank.png').subsample(9,9)
        self.one = PhotoImage(file=r'images\1.png').subsample(9,9)
        self.two = PhotoImage(file=r'images\2.png').subsample(9,9)
        self.three = PhotoImage(file=r'images\3.png').subsample(9,9)
        self.four = PhotoImage(file=r'images\4.png').subsample(9,9)
        self.five = PhotoImage(file=r'images\5.png').subsample(9,9)
        self.six = PhotoImage(file=r'images\6.png').subsample(9,9)

        ## Inert sprites (add hover text-- eg: This isn't poker!):
        self.chips = PhotoImage(file='images\chips.png').subsample(3,3)
        self.chips_label = Label(image=self.chips, bg='#069c71')
        self.chips_label.grid(row=4, column=1)

        self.cigar = PhotoImage(file='images\cigar.png').subsample(3, 3)
        self.cigar_label = Label(image=self.cigar, bg='#069c71')
        self.cigar_label.grid(row=4, column=2)

        self.cards = PhotoImage(file='images\cards.png').subsample(3, 3)
        self.cards_label = Label(image=self.cards, bg='#069c71')
        self.cards_label.grid(row=4, column=3)

        ## Roll button:
        self.roll_button = Button(text="Roll", command=lambda: self.roll_dice('y'))
        self.roll_button.grid(row=3, column=2)

        ## Leave button:
        self.leave_button = Button(text="Leave", bg='gray', command=self.root.destroy)
        self.leave_button.grid(row=5, column=2)

        # faces = [1, 2, 3, 4, 5, 6]

        self.root.mainloop()

    ## Roll functions:
    def roll_dice(self, user_click):
        global faces
        faces = [1, 2, 3, 4, 5, 6]

        if user_click == 'y':
            rand_idx = random.randrange(len(faces))
            result = faces[rand_idx]
        print(result)
        self.update_dice(user_click, result)  #### THIS is what was missing! Remember the order of fxs
                                                                            # does not matter in a class :)

    def update_dice(self, user_click, result = 10):
        if user_click == 'y':
            if result == 1:
                self.die_display.config(image=self.one)
            elif result == 2:
                self.die_display.config(image=self.two)
            elif result == 3:
                self.die_display.config(image=self.three)
            elif result == 4:
                self.die_display.config(image=self.four)
            elif result == 5:
                self.die_display.config(image=self.five)
            else:
                self.die_display.config(image=self.six)
        else:
            self.die_display.config(image=self.blank)

        self.root.update()







        # if user_click == 1:
        # # faces = range(0,5)
        # # print(faces)
        # # for _ in faces:
        #     result = random.choice(faces)
        #     return result
        #     print(result)

