from tkinter import *
from tkinter import ttk
import random
from gui_two_dice import GUI2

count = 0   #remember for a variable to be global, it needs to exist OUTSIDE of the class/function/file!

'''Attempted placing the style outside, still does not work'''
# style = ttk.Style()
# style.configure("Casino", foreground='#069c71', background='#069c71')

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title('Dice Simulator')
        self.root.resizable(False, False)
        self.root.config(bg='#069c71', pady=1, padx=3)
        # self.root.geometry('580x400')

        # self.style = ttk.Style()
        # self.style.configure("Casino", foreground='#069c71', background='#069c71')

        self.tabs = ttk.Notebook(self.root, width=580, height=400)
        self.tabs.grid(row=0, column=1, columnspan=1)
        self.tab1 = ttk.Frame(self.tabs) #(self.tabs, style="Casino")
        self.tab2 = ttk.Frame(self.tabs)
        self.tab3 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text="1 Die")
        self.tabs.add(self.tab2, text="2 Dice", image='images\2.png')
        self.tabs.add(self.tab3, text="3 Dice", state="disabled")

        '''This works as well, but I haven't found how to stretch it adequately. Alternatively, I can replace the image'''
        # background_image = PhotoImage(file='images/blank.png')
        # background_tab1 = Label(self.tab1, image=background_image)
        # # background_tab1.place(x=0, y=0, relwidth=0.8, relheight=1)

        '''Background'''
        self.background_tab1 = Canvas(self.tab1, bg='#069c71')
        self.background_tab1.place(x=0, y=0,  width=580, height=400)


        ## Banner:
        self.banner = Label(self.tab1, text="Dice Simulator: \n Let it roll!", font=('Monotype Corsiva', 24, 'bold'), pady=3,
                            padx=2, fg='#eac527', bg='#069c71', borderwidth=3, relief='ridge') #eac527
        self.banner.grid(row=1, column=3)

        ## Secret Banner:
        self.secret_banner = Label(self.tab1, text="", font=('Segoe UI', 11, 'bold'), pady=3, padx=2,
                                   fg='#ffde59', bg='#069c71')
        self.secret_banner.grid(row=4, column=1)

        ## Die display:
        self.current_die = PhotoImage(file=r'images\blank.png').subsample(9, 9)
        self.die_display = Label(self.tab1, image=self.current_die, bg='#069c71')
        self.die_display.grid(row=2, column=2)

        self.blank = PhotoImage(file=r'images\blank.png').subsample(9, 9)
        self.one = PhotoImage(file=r'images\1.png').subsample(9, 9)
        self.two = PhotoImage(file=r'images\2.png').subsample(9, 9)
        self.three = PhotoImage(file=r'images\3.png').subsample(9, 9)
        self.four = PhotoImage(file=r'images\4.png').subsample(9, 9)
        self.five = PhotoImage(file=r'images\5.png').subsample(9, 9)
        self.six = PhotoImage(file=r'images\6.png').subsample(9, 9)

        ## Inert sprites (add hover text-- eg: This isn't poker!):
        self.chips = PhotoImage(file=r'images\chips.png').subsample(3, 3)
        self.chips_label = Label(self.tab1, image=self.chips, bg='#069c71')
        self.chips_label.grid(row=1, column=1)

        self.cigar = PhotoImage(file=r'images\cigar.png').subsample(3, 3)
        self.cigar_label = Label(self.tab1, image=self.cigar, bg='#069c71')
        self.cigar_label.grid(row=4, column=2)

        self.cards = PhotoImage(file=r'images\cards.png').subsample(3, 3)
        self.cards_label = Label(self.tab1, image=self.cards, bg='#069c71')
        self.cards_label.grid(row=4, column=3)

        ## Roll button:
        self.roll_button = Button(self.tab1, text="Roll!", command=lambda: self.roll_dice('y'))
        self.roll_button.grid(row=3, column=2)

        ## Leave button:
        self.leave_button = Button(self.tab1, text="Leave", bg='gray', command=self.root.destroy)
        self.leave_button.grid(row=2, column=3)

        self.root.mainloop()


    ## Roll functions:
    def roll_dice(self, user_click):
        faces = [1, 2, 3, 4, 5, 6]

        if user_click == 'y':
            rand_idx = random.randrange(len(faces))
            result = faces[rand_idx]
        print(result)
        self.update_dice(user_click, result)  #### THIS is what was missing! Remember the order of fxs
                                                                            # does not matter in a class :)

        self.update_count(user_click)
        print(f"{count}\n")

        self.root.update()

    def update_dice(self, user_click, result= 10):
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


    def update_count(self, user_click):
        global count
        if user_click == 'y':
            count +=1

        if count == 10:
            self.secret_banner.config(text="Don't you think \n you're \n overdoing this?")
        elif count == 20:
            self.secret_banner.config(text="You're definitely \n overdoing this.")
        elif count == 35:
            self.secret_banner.config(text="You're not stopping, \n are you?")
        elif count == 50:
            self.secret_banner.config(text="Is this a \n different person??")
        elif count == 55:
            self.secret_banner.config(text="Do you really have \n a need for this?")
        elif count == 70:
            self.secret_banner.config(text="STOP!")
        elif count == 80:
            self.secret_banner.config(text="We have no prizes...")
        elif count == 100:
            self.secret_banner.config(text="Whatever. Addict. :) \n Here's your \n dopamine hit.")
        else:
            self.secret_banner.config(text="")


###########################----------------- TWO DICE -----------------###########################

# class GUI2():
#     def __init__(self):
#         self.root = Tk()
#         self.root.title('Dice Simulator')
#         self.root.resizable(False, False)
#         self.root.config(bg='#069c71', pady=1, padx=3)
#
#         self.tabs = ttk.Notebook(self.root, width=580, height=400)
#         self.tabs.grid(row=0, column=1, columnspan=1)
#         self.tab1 = ttk.Frame(self.tabs)  # (self.tabs, style="Casino")
#         self.tab2 = ttk.Frame(self.tabs)
#         self.tab3 = ttk.Frame(self.tabs)
#         self.tabs.add(self.tab1, text="1 Die")
#         self.tabs.add(self.tab2, text="2 Dice", image='images\2.png')
#         self.tabs.add(self.tab3, text="3 Dice", state="disabled")
#
#         '''Background'''
#         self.background_tab2 = Canvas(self.tab2, bg='#069c71')
#         self.background_tab2.place(x=0, y=0, width=580, height=400)
#
#         # self.root.geometry('580x400')
#         # self.root.config(bg='#069c71', pady=1, padx=10)
#         # self.root.resizable(False, False)
#
#         ## Banner:
#         self.banner = Label(self.tab2, text="Dice Simulator: \n Let it roll!", font=('Monotype Corsiva', 24, 'bold'), pady=3,
#                             padx=2, fg='#eac527', bg='#069c71', borderwidth=3, relief='ridge') #eac527
#         self.banner.grid(row=1, column=3)
#
#         ## Secret Banner:
#         self.secret_banner = Label(self.tab2, text="", font=('Segoe UI', 11, 'bold'), pady=3, padx=2,
#                                    fg='#ffde59', bg='#069c71')
#         self.secret_banner.grid(row=4, column=1)
#
#         ## Die display:
#         self.current_die = PhotoImage(file=r'images\blank.png').subsample(9, 9)
#         self.current_die2 = PhotoImage(file=r'images\blank.png').subsample(9, 9)
#         self.die_display = Label(self.tab2, image=self.current_die, bg='#069c71')
#         self.die_display2 = Label(self.tab2, image=self.current_die2, bg='#069c71')
#         self.die_display.grid(row=2, column=1)
#         self.die_display2.grid(row=2, column=2)
#
#         self.blank = PhotoImage(file=r'images\blank.png').subsample(9, 9)
#         self.one = PhotoImage(file=r'images\1.png').subsample(9, 9)
#         self.two = PhotoImage(file=r'images\2.png').subsample(9, 9)
#         self.three = PhotoImage(file=r'images\3.png').subsample(9, 9)
#         self.four = PhotoImage(file=r'images\4.png').subsample(9, 9)
#         self.five = PhotoImage(file=r'images\5.png').subsample(9, 9)
#         self.six = PhotoImage(file=r'images\6.png').subsample(9, 9)
#
#         ## Inert sprites (add hover text-- eg: This isn't poker!):
#         self.chips = PhotoImage(file=r'images\chips.png').subsample(3, 3)
#         self.chips_label = Label(self.tab2, image=self.chips, bg='#069c71')
#         self.chips_label.grid(row=1, column=1)
#
#         self.cigar = PhotoImage(file=r'images\cigar.png').subsample(3, 3)
#         self.cigar_label = Label(self.tab2, image=self.cigar, bg='#069c71')
#         self.cigar_label.grid(row=4, column=2)
#
#         self.cards = PhotoImage(file=r'images\cards.png').subsample(3, 3)
#         self.cards_label = Label(self.tab2, image=self.cards, bg='#069c71')
#         self.cards_label.grid(row=4, column=3)
#
#         ## Roll button:
#         self.roll_button = Button(self.tab2, text="Roll!", command=lambda: self.roll_dice('y'))
#         self.roll_button.grid(row=3, column=2)
#
#         ## Leave button:
#         self.leave_button = Button(self.tab2, text="Leave", bg='gray', command=self.root.destroy)
#         self.leave_button.grid(row=2, column=3)
#
#         self.root.mainloop()
#
#
#     ## Roll functions:
#     def roll_dice(self, user_click):
#         faces = [1, 2, 3, 4, 5, 6]
#
#         if user_click == 'y':
#             rand_idx1 = random.randrange(len(faces))
#             result1 = faces[rand_idx1]
#
#             rand_idx2 = random.randrange(len(faces))
#             result2 = faces[rand_idx2]
#         print(result1, result2)
#
#         self.update_dice(user_click, result1)  #### THIS is what was missing! Remember the order of fxs does not matter in a class :)
#         self.update_dice2(user_click, result2)
#
#         self.update_count(user_click)
#         print(f"{count}\n")
#
#         self.root.update()
#
#     # def roll_dice2(self, user_click):
#     #     faces = [1, 2, 3, 4, 5, 6]
#     #
#     #     if user_click == 'y':
#     #         rand_idx = random.randrange(len(faces))
#     #         result = faces[rand_idx]
#     #     print(result)
#     #     self.update_dice2(user_click, result)  #### THIS is what was missing! Remember the order of fxs
#     #                                                                         # does not matter in a class :)
#     #     self.update_count(user_click)
#     #     print(f"{count}\n")
#     #
#     #     self.root.update()
#
#     def update_dice(self, user_click, result= 10):
#         if user_click == 'y':
#             if result == 1:
#                 self.die_display.config(image=self.one)
#                 self.die_display2.config(image=self.one)
#             elif result == 2:
#                 self.die_display.config(image=self.two)
#                 self.die_display2.config(image=self.two)
#             elif result == 3:
#                 self.die_display.config(image=self.three)
#                 self.die_display2.config(image=self.three)
#             elif result == 4:
#                 self.die_display.config(image=self.four)
#                 self.die_display2.config(image=self.four)
#             elif result == 5:
#                 self.die_display.config(image=self.five)
#                 self.die_display2.config(image=self.five)
#             else:
#                 self.die_display.config(image=self.six)
#                 self.die_display2.config(image=self.six)
#         else:
#             self.die_display.config(image=self.blank)
#             self.die_display2.config(image=self.blank)
#
#     def update_dice2(self, user_click, result= 10):
#         if user_click == 'y':
#             if result == 1:
#                 self.die_display2.config(image=self.one)
#             elif result == 2:
#                 self.die_display2.config(image=self.two)
#             elif result == 3:
#                 self.die_display2.config(image=self.three)
#             elif result == 4:
#                 self.die_display2.config(image=self.four)
#             elif result == 5:
#                 self.die_display2.config(image=self.five)
#             else:
#                 self.die_display2.config(image=self.six)
#         else:
#             self.die_display2.config(image=self.blank)
#
#
#     def update_count(self, user_click):
#         global count
#         if user_click == 'y':
#             count +=1
#
#         if count == 10:
#             self.secret_banner.config(text="Don't you think \n you're \n overdoing this?")
#         elif count == 20:
#             self.secret_banner.config(text="You're definitely \n overdoing this.")
#         elif count == 35:
#             self.secret_banner.config(text="You're not stopping, \n are you?")
#         elif count == 50:
#             self.secret_banner.config(text="Is this a \n different person??")
#         elif count == 55:
#             self.secret_banner.config(text="Do you really have \n a need for this?")
#         elif count == 70:
#             self.secret_banner.config(text="STOP!")
#         elif count == 80:
#             self.secret_banner.config(text="We have no prizes...")
#         elif count == 100:
#             self.secret_banner.config(text="Whatever. Addict. :) \n Here's your \n dopamine hit.")
#         else:
#             self.secret_banner.config(text="")