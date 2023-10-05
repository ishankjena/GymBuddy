import PushUpCounter
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from PIL import Image, ImageTk

window = ttk.Window()
window.title('Gym Buddy')
window.geometry('700x900')
window.resizable(False, False)

titleLabel = ttk.Label(master=window, text='  GYM \nBUDDY', font='Garamond 40 bold')
titleLabel.place(relx=0.5, rely=0.2, anchor="c")

frame1 = ttk.Labelframe(master=window, text='Biceps Curls')
curls_ = Image.open('images/curl.png').resize((200,200))
curls = ImageTk.PhotoImage(curls_)
btn1 = ttk.Button(master=frame1, image=curls, command=None, bootstyle="light-outline")
btn1.pack()
frame1.place(relx=0.27, rely=0.52, anchor="c")

frame2 = ttk.Labelframe(master=window, text='Squats')
squats_ = Image.open('images/squat.png').resize((200,200))
squats = ImageTk.PhotoImage(squats_)
btn2 = ttk.Button(master=frame2, image=squats, command=None, bootstyle="light-outline")
btn2.pack()
frame2.place(relx=0.73, rely=0.52, anchor="c")

frame3 = ttk.Labelframe(master=window, text='Elbow Plank')
planks_ = Image.open('images/plank.png').resize((200,200))
planks = ImageTk.PhotoImage(planks_)
btn3 = ttk.Button(master=frame3, image=planks, command=None, bootstyle="light-outline")
btn3.pack()
frame3.place(relx=0.27, rely=0.82, anchor="c")

frame4 = ttk.Labelframe(master=window, text='Standard Push-Ups')
push_ups_ = Image.open('images/push-up.png').resize((200,200))
push_ups = ImageTk.PhotoImage(push_ups_)
btn4 = ttk.Button(master=frame4, image=push_ups, command=lambda:PushUpCounter.run(), bootstyle="light-outline")
btn4.pack()
frame4.place(relx=0.73, rely=0.82, anchor="c")

window.mainloop()