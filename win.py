from tkinter import *
import random
from tkinter import messagebox
from datetime import *
import pygame


def verify():
    pass


windows = Tk()
windows.title("Lotto Draw")
windows.geometry("320x380")
windows.config(background="yellow")

img = Canvas(windows, width=2000, height=650)
img.place(x=-10, y=-20)
_img1 = PhotoImage(file="money.png")
img.create_image(20, 20, anchor=NW, image=_img1)

status = StringVar()

lottries = Label(windows, text="TAKE IT ALL", font="bold")
lottries.place(x=100, y=5)

songstatus = Label(windows, textvariable=status, font="bold", bg="Orange")
songstatus.place(x=100, y=40)

play = Label(windows, text="LOTTO NUMBERS", font="bold")
play.place(x=10, y=70)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()

txt1 = Entry(windows, textvariable=num1, width=4)
txt1.place(x=60, y=120)
txt2 = Entry(windows, textvariable=num2, width=4)
txt2.place(x=100, y=120)
txt3 = Entry(windows, textvariable=num3, width=4)
txt3.place(x=140, y=120)
txt4 = Entry(windows, textvariable=num4, width=4)
txt4.place(x=180, y=120)
txt5 = Entry(windows, textvariable=num5, width=4)
txt5.place(x=220, y=120)
txt6 = Entry(windows, textvariable=num6, width=4)
txt6.place(x=260, y=120)

result_answer = Label(windows, font=14, width=50, height=8)
result_answer.place(x=30, y=200)

clock = Label(windows, font="bold")
clock.place(x=30, y=340)

dytime = datetime.now()
clock.config(text=dytime.strftime("%d/%m/%y  %H:%M:%S %p"))
def luck():
    x = num1.get()
    y = num2.get()
    z = num3.get()
    a = num4.get()
    b = num5.get()
    c = num6.get()

    my_list = [x, y, z, a, b, c]
    my_list.sort()

    todaylotto = sorted(random.sample(range(1, 49), 6))

    if any(my_list) < 0 or any(my_list) < 50:
        messagebox.showinfo("hurray", "Get ready")

        if len(todaylotto) == len(my_list):
            same = set(todaylotto).intersection(set(my_list))
            if len(same) == 6:
                result_answer.config(text="Jackpot Hurray \n" + "You just got your self Price : R10, 000 000.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 5:
                result_answer.config(text="Felicitations" + "You got 5 numbers correct" + "\n With this Outstanding Achievement" + "You won yourself R8, 584.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 4:
                result_answer.config(text="Felicitations" + "You got 4 numbers correct" + "\n With this Meritorious Achievement" + "You won yourself R2, 384.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 3:
                result_answer.config(text="Felicitations" + "You got 3 numbers correct" + "\n With this Substantial Achievement" + "You won yourself R100.50" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 2:
                result_answer.config(text="Felicitations" + "You got 2 numbers correct" + "\n With this Adequate Achievement" + "You won yourself R20.00" + "\n Today Lotto Numbers are" + str(todaylotto))
            elif len(same) == 1:
                messagebox.showinfo("RESULT", "We are sorry you only got one correct lotto numbers are: " + str(todaylotto))
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(todaylotto))
    else:
        messagebox.showinfo("NOOO", "Follow the rules")
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        num4.delete(0, END)
        num5.delete(0, END)
        num6.delete(0, END)


btn = Button(windows, text="CHECK YOUR RESULTS", bg="brown", command=luck)
btn.place(x=100, y=150)

filename = "Ndikhokhele (feat. Nathi, Rebecca Malope, Benjamin Dube, Mlindo The Vocalist, T'kinzy, Judith....mp3"

def music():

    status.set(filename)

    pygame.mixer.init()

    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

btn1 = Button(windows, text="PLAYMUSIC", bg="brown", command=music)
btn1.place(x=10, y=40)

windows.mainloop()
