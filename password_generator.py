"""
    Name: password_generator.py
    Author: Samantha Roberts
    Created: 6/24/23
    Purpose: Get information for a user to randomly generate a password
"""

from tkinter import *
import random
from tkinter import ttk
from tkinter.messagebox import showinfo

class Generator:

    def __init__(self):

        self._uppercase = False

        self._length = 0

        self._lowercase = False

        self._numbers = 0

        self._special_chars = ""

        # Create app
        self.root = Tk()
        # Create app title
        self.root.title("Password Generator")
        # Call create frames
        self.create_frames()
        # Call create widgerts
        self.create_widgets()

        # mainloop to keep app on screen
        mainloop()

    def create_frames(self):

        # Create frame to hold password information widgets
        self.information_frame = LabelFrame(
            self.root,
            text="Password Information",
            relief=RAISED
        )
        # Create frame to hold new generated password
        self.password_frame = LabelFrame(
            self.root,
            text="Generated Password",
            relief=RAISED
        )
        # Pack frames
        self.information_frame.pack(fill=X)
        self.password_frame.pack(fill=Y)

        self.information_frame.pack_propagate(False)
        self.password_frame.pack_propagate(False)

        
    def create_widgets(self):

        self.lbl_length = Label(
            self.information_frame,
            text="Password length:"
        )

        self.entry_length = Entry(
            self.information_frame,
            width=15,
            relief=RAISED
        )
        
        self.chk_uppercase = Checkbutton(
            self.information_frame,
            text="UpperCase",
            variable=self._uppercase,
            onvalue= True,
            offvalue= False
        )

        self.chk_lowercase= Checkbutton(
            self.information_frame,
            text="Lowercase"
        )

        self.chk_special = Checkbutton(
            self.information_frame,
            text="Special Characters"
        )

        self.chk_numbers = Checkbutton(
            self.information_frame,
            text="Numbers"
        )
        
        self.btn_password = Button(
            self.password_frame,
            text="Generate",
            command=self.generate_password
        )
        self.lbl_password = Label(
            self.password_frame,
            width=40,
            relief=RAISED
        )

        # Grid the widgets
        self.lbl_length.grid(row=0, column=0, sticky='w')
        self.entry_length.grid(row=0, column=1, sticky='w')
        self.chk_uppercase.grid(row=1, column=0, sticky='w')
        self.chk_lowercase.grid(row=2, column=0, sticky='w')
        self.chk_special.grid(row=1,column=1, sticky='w')
        self.chk_numbers.grid(row=2, column=1, sticky='w')

        self.btn_password.grid(row=0, column=0)
        self.lbl_password.grid(row=0, column=1)

        # Pack widgets into frames
        for widget in self.information_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        for widget in self.password_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    def generate_password(self):



        if self._uppercase == True:
            Tk.messagebox.showinfo(message="upper")




password = Generator()
