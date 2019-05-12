import easygui
from tkinter import *
import PyInstaller
import os

ikone = False
ico = False

def ikonFunc():
    global ikone
    ikone = True
    window.destroy()


def imamIco():
    global ico
    ico = True
    window2.destroy()

#odabir = easygui.fileopenbox("Odaberi file: ","",r"C:\Users\Ivan\Documents\GitHub\MyPrograms\DefaultOpener")
dest = easygui.diropenbox("Odaberi destinaciju: ","",r"C:\Users\Ivan\Desktop")



window = Tk()
window.title("Ikone")
window.resizable(width=False, height=False)
window.geometry("800x600")
photo1 = PhotoImage(file="imaga.gif")
daButton = PhotoImage(file="da.gif")
neButton = PhotoImage(file="ne.gif")
#tekstSlika = PhotoImage(file="tekst.gif")
Label(window, image=photo1, bg="white") .place(x=-2, y=-2)
Label(window, text="Zelis li dodati svoju ikonicu?", fg="white", bg="black", font="none 19 bold") .place(relx=0.5, rely=0.27,anchor=CENTER)
Button(window, image=daButton, command=ikonFunc) .place(relx=0.333, rely=0.55, anchor=CENTER)
Button(window, image=neButton, command=window.destroy) .place(relx=0.666, rely=0.55, anchor=CENTER)
window.mainloop()

if ikone == True:
    odabirIcoa = easygui.fileopenbox("Odaberi Ico file: ", "", r"C:\Users\Ivan\Documents\GitHub\MyPrograms\DefaultOpener")

# WIP iako mi se neda vise

