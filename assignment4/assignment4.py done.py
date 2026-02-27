import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class FoodViewer:

    def __init__(self):
        self.root = Tk()
        self.root.title("Food Viewer")
        self.root.geometry("400x300")

        # Frame for image
        self.img_frame = Frame(self.root)
        self.img_frame.pack()

        # Frame for radio buttons
        self.rbdBtn_frame = Frame(self.root)
        self.rbdBtn_frame.pack()

        # Load images
        self.img1 = Image.open("chicken.jpg")
        self.img1 = self.img1.resize((400, 300))
        self.imgOne = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("pie.jpg")
        self.img2 = self.img2.resize((400, 300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("pizza.jpg")
        self.img3 = self.img3.resize((350, 300))
        self.imgThree = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open("steak.jpg")
        self.img4 = self.img4.resize((300, 300))
        self.imgFour = ImageTk.PhotoImage(self.img4)

        # Label initial image is Chicken
        self.lbl = Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()

        # IntVar
        self.var = IntVar()
        self.var.set(1)

        # Radiobuttons
        self.radio_a = Radiobutton(self.rbdBtn_frame, text="Chicken",
                                   variable=self.var, value=1,
                                   command=self.on_radio_select)
        self.radio_a.pack(side="left", padx=10)

        self.radio_b = Radiobutton(self.rbdBtn_frame, text="Pie",
                                   variable=self.var, value=2,
                                   command=self.on_radio_select)
        self.radio_b.pack(side="left", padx=10)

        self.radio_c = Radiobutton(self.rbdBtn_frame, text="Pizza",
                                   variable=self.var, value=3,
                                   command=self.on_radio_select)
        self.radio_c.pack(side="left", padx=10)

        self.radio_d = Radiobutton(self.rbdBtn_frame, text="Steak",
                                   variable=self.var, value=4,
                                   command=self.on_radio_select)
        self.radio_d.pack(side="left", padx=10)
        

        self.root.mainloop()

    def on_radio_select(self):
        choice = self.var.get()

        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)
    
    


    

# Run the program
app = FoodViewer()




