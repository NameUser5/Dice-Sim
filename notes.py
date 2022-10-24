#https://replit.com/@EvelynBrooks1/Week12?v=1

from tkinter import *
import ttk
from cat import Cat

text_list = ['Name:', 'Breed: ', 'Age: ', 'Gender: ', 'Color: ']
counter = 0

# Create GUI window
root = Tk()
root.title("Cats Management")

# Add Tabs
tabControl = ttk.Notebook(root, width=570, height=350)
submit_tab = Frame(tabControl)
search_tab = Frame(tabControl)
tabControl.add(submit_tab, text='Submit')
tabControl.add(search_tab, text='Search')
tabControl.grid(row=0, column=0)

# Background Images
background_submit = PhotoImage(file="bgcats.png")
background_label_submit = Label(submit_tab, image=background_submit)
background_label_submit.place(x=0, y=0, relwidth=1, relheight=1)

background_search = PhotoImage(file="searchcat.png")
background_label_search = Label(search_tab, image=background_search, bg="white")
background_label_search.place(x=0, y=0, relwidth=1, relheight=1)


class Gui:
    def __init__(self, window):

        # creating labels Submit tab
        self.updater_text = Label(submit_tab, text=text_list[counter], bg='white', font=('comic sans', 17))
        self.updater_text.grid(row=1, column=0, padx=10, pady=70)

        self.validate_submit = Label(submit_tab, text='', bg='beige')
        self.validate_submit.grid(row=1, column=3)

        # creating labels Search tab
        self.name_search = Label(search_tab, text="Name:", bg='white', font=('comic sans', 17))
        self.name_search.grid(row=1, column=0, padx=10, pady=70)

        self.validate_search = Label(search_tab, text='', bg='black')
        self.validate_search.grid(row=1, column=3)

        # Creating entries
        self.updater_entry = Entry(submit_tab, width=20)
        self.updater_entry.grid(row=1, column=1)

        self.search_entry = Entry(search_tab, width=20)
        self.search_entry.grid(row=1, column=1)

        # Creating Buttons
        self.next_btn = Button(submit_tab, text='Submit', command=self.updater)
        self.next_btn.grid(row=1, column=2)

        self.search_btn = Button(search_tab, text='Search', command=self.cat_searched)
        self.search_btn.grid(row=1, column=2)

    def updater(self):
        next_field = TRUE
        global counter

        # Validate Breed, Gender, & Color are letters only
        if ((counter == 1) or (counter == 3) or (counter == 4)):
            if self.updater_entry.get().isalpha():
                self.set_Cat_attribute()
                counter
                self.validate_submit.config(text='', fg='red')
            else:
                self.validate_submit.config(text='Invalid', fg='red')
                next_field = FALSE

        # Validate Age is Numbers only
        if counter == 2:
            if self.updater_entry.get().isnumeric():
                self.set_Cat_attribute()
                counter
                self.validate_submit.config(text='', fg='red')
            else:
                self.validate_submit.config(text='Invalid', fg='red')
                next_field = FALSE

        # Import Name without Validation
        if counter == 0:
            self.set_Cat_attribute()
            counter

        # Clear Entry field after each submit
        self.updater_entry.delete(0, END)

        # Reset to Name entry after last submit, Write data to file
        if counter == 4:
            counter = 0
            self.create_cat()
            self.updater_text.config(text=text_list[counter])
        # Add to counter if input data is valid
        else:
            if next_field:
                counter += 1
                self.updater_text.config(text=text_list[counter])

    def cat_searched(self):
        self.target_search = self.search_entry.get()

        with open("cats.txt", "r") as file:
            data = file.readlines()

        for cat_info in data:
            self.current_name = cat_info.split(',')[0]
            self.current_breed = cat_info.split(',')[1]
            self.current_age = cat_info.split(',')[2]
            self.current_gender = cat_info.split(',')[3]
            self.current_color = cat_info.split(',')[4]

        if self.current_name == self.target_search:
            self.breed_label = Label(search_tab, text=self.current_breed, bg='white', font=('', 17, 'bold'))
            self.breed_label.grid(row=2, column=0)

            self.age_label = Label(search_tab, text=self.current_age, bg='white', font=('', 17, 'bold'))
            self.age_label.grid(row=3, column=0)

            self.gender_label = Label(search_tab, text=self.current_gender, bg='white', font=('', 17, 'bold'))
            self.gender_label.grid(row=4, column=0)

            self.color_label = Label(search_tab, text=self.current_color, bg='white', font=('', 17, 'bold'))
            self.color_label.grid(row=5, column=0)

    # Function to set entries as Cat Attributes
    def set_Cat_attribute(self):
        global counter

        if counter == 0:
            Cat.name = self.updater_entry.get()

        if counter == 1:
            Cat.breed = self.updater_entry.get()

        if counter == 2:
            Cat.age = self.updater_entry.get()

        if counter == 3:
            Cat.gender = self.updater_entry.get()

        if counter == 4:
            Cat.color = self.updater_entry.get()