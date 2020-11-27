from tkinter import *
from tkinter import messagebox
import pygame


# function
def logins():

    log = age_entry.get()
    log1 = int(log)
    if log1 < 18:
        messagebox.showerror("NOTE!!", "Not for person under the age of 18")

    else:
        messagebox.showinfo("HELLOW!!", "WELLCOME" + nm_entry.get() + snm_entry.get())
        lotto.destroy()
        import win
        win.verify()


lotto = Tk()
lotto.title("SIGN UP")
lotto.geometry("750x350")


status = StringVar()

# labels& entries

img = Canvas(lotto, width=800, height=650)
img.place(x=-20, y=-20)
_img1 = PhotoImage(file="HEADING.PNG")
img.create_image(20, 20, anchor=NW, image=_img1)

songstatus = Label(lotto, textvariable=status, font="bold", bg="Orange")
songstatus.place(x=100, y=50)

name = Label(lotto)
name.config(text="NAME", fg="black", font=("bold", 18))
name.place(x=100, y=100)

sname = Label(lotto)
sname.config(text="SURNAME", fg="black", font=("bold", 18))
sname.place(x=100, y=150)

age_l = Label(lotto)
age_l.config(text="AGE", fg="black", font=("bold", 18))
age_l.place(x=100, y=200)

nm_entry = Entry(lotto, width=12, fg="black", font=("bold", 18))
nm_entry.place(x=250, y=100)

snm_entry = Entry(lotto,  width=12,  fg="black", font=("bold", 18))
snm_entry.place(x=250, y=150)

age = IntVar

age_entry = Entry(lotto)
age_entry.config(textvariable=age, width=12)
age_entry.place(x=250, y=200)

# button
btn = Button(lotto, text="LOGIN", bg="red", command=logins)
btn.place(x=250, y=250)

filename = "Assertive Fam - Nkosi Sikelela Africa.mp3"
def music():

    status.set(filename)

    pygame.mixer.init()

    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

playbtn = Button(lotto, text="PLAYMUSIC", bg="red", command=music)
playbtn.place(x=10, y=50)

lotto.mainloop()
