
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import tkinter


root = tk.Tk()

# setting the windows size
root.geometry("700x500")
# root.resizeable(False, False)
# declaring string variable
# for storing name and password
name_var = tk.StringVar()


def submit():

    name = name_var.get()
    text = []
    text.append(name)
    df = profile.predict(vectorizer, LRmodel, text)
    data = df['Sentiment']
    tkinter.messagebox.showinfo('Prediction', data.item())

    name_var.set("")


root.configure(bg='#BB8FCE')

canvas = Canvas(root, width=400, height=330)
canvas.place(x=150, y=60)

title = Label(root, text="Personality Prediction", font="Bold 26")
title.place(x=180, y=150)

text = Label(root, text="Enter Your Text", font="Bold 16")
text.place(x=200, y=220)

name_entry = tk.Entry(root, textvariable=name_var,
                      font=('calibre', 10, 'normal'))
name_entry.place(x=250, y=250)

sub_btn = tk.Button(root, text='Submit', command=submit)


root.mainloop()

# class login(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("700x500")
#         self.resizable(False, False)

#     def Label(self):
#         # self.backGroundImage = PhotoImage(file="background2.png")
#         # self.backGroundImage = Label(self, image=self.backGroundImage)
#         # self.backGroundImage.place(x=0, y=0)
#         self.configure(bg='#BB8FCE')

#         self.canvas = Canvas(self, width=400, height=330)
#         self.canvas.place(x=150, y=60)

#         self.title = Label(self, text="Personality Prediction", font="Bold 26")
#         self.title.place(x=180, y=150)

#         self.text = Label(self, text="Enter Your Text", font="Bold 16")
#         self.text.place(x=200, y=220)

#     def Entry(self):
#         self.Text1 = Text(self, borderwidth=1,
#                           highlightthickness=0, width=25, height=2)

#         self.Text1.place(x=250, y=250)

#     def Button(self):
#         self.submitButtonImage = PhotoImage(file="img0.png")
#         self.submitbutton = Button(
#             self, image=self.submitButtonImage, command=self.Submit, border=0)
#         self.submitbutton.place(x=250, y=300)

#     def Submit(self):
#         text = []
#         user_input = Entry(text).get()
#         text.append(user_input)
#         df = profile.predict(vectorizer, LRmodel, text)
#         data = df['Sentiment']
#         tkinter.messagebox.showinfo('Prediction', data.item())


# if __name__ == "__main__":
#     Screen = login()
#     Screen.Label()
#     Screen.Entry()
#     Screen.Button()
#     Screen.mainloop()
