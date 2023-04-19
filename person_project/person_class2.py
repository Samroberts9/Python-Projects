"""
    Name: person_class2.py
    Author: Samantha Roberts
"""
from tkinter import *

class Person:

    def __init__(self):
        self._name = ""
        self._age =""
        self._major = ""

        # Create app
        self.root = Tk()
        # Create title for app
        self.root.title("Person")
        # Call create_widgets method
        self.create_widgets()
        
        # mainloop to keep app on screen
        mainloop()

    def create_widgets(self):

        # Main frame to hold other widgets
        self.information_frame = LabelFrame(
            self.root,
            text="Person Information",
            relief=RAISED
        )
        self.lbl_name = Label(
            self.information_frame,
            text="Name:",
            width=5
        )
        self.entry_name = Entry(
            self.information_frame,
            width=20
        )
        self.lbl_age = Label(
            self.information_frame,
            text="Age",
            width=5
        )
        self.entry_age = Entry(
            self.information_frame,
            width=20
        )
        self.lbl_major = Label(
            self.information_frame,
            text="Major",
            width=5
        )
        self.entry_major = Entry(
            self.information_frame,
            width=20
        )
        self.lbl_greet = Label(
            self.information_frame,
            wraplength=200
        )
        self.btn_run = Button(
            self.information_frame,
            text="Run Greeting",
            width=10,
            command=self.greet
        )


        self.lbl_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.lbl_age.grid(row=1, column=0)
        self.entry_age.grid(row=1, column=1)
        self.lbl_major.grid(row=2, column=0)
        self.entry_major.grid(row=2, column=1)

        self.btn_run.grid(row= 3, column= 0)
        self.lbl_greet.grid(row=4, column=0)


        # Set padding for all wedgets in the frames
        self.information_frame.grid_configure(padx=25, pady=25)

        for widget in self.information_frame.winfo_children():
            widget.grid_configure(padx=15, pady=15)

    """def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_major(self):
        return self._major"""
    
    
    def greet(self, *args):
       #print(f"Hello! My name is {self._name} and I am {self._age} years old\
            #  \nMy major is {self._major}.")

        self._name = self.entry_name.get()
        self._age = self.entry_age.get()
        self._major = self.entry_major.get()

        self.lbl_greet.configure(text=f"Hello! My name is {self._name}.\
                                 \nI am {self._age} and my major is {self._major}.")