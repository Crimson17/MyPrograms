import easygui
from tkinter import *

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
#dest = easygui.diropenbox("Odaberi destinaciju: ","",r"C:\Users\Ivan\Desktop")



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
    window2 = Tk()
    window2.title("IcoFile-ovi")
    window2.resizable(width=False, height=False)
    window2.geometry("800x600")
    photo1 = PhotoImage(file="imaga.gif")
    daButton = PhotoImage(file="da.gif")
    neButton = PhotoImage(file="ne.gif")
    Label(window2, image=photo1, bg="white") .place(x=-2, y=-2)
    Label(window2, text="Imas li vec IcoFile(Da)? ili zelis pretvoriti nesta drugo u Ico(Ne)?", bg="black", fg="white", font="none 16 bold") .place(relx=0.5, rely=0.27, anchor=CENTER)
    Button(window2, image=daButton, command=imamIco) .place(relx=0.333, rely=0.55, anchor=CENTER)
    Button(window2, image=neButton, command=window2.destroy) .place(relx=0.666, rely=0.55, anchor=CENTER)
    window2.mainloop()

    if ico == True:
        odabirIcoa = easygui.fileopenbox("Odaberi Ico file: ", "", r"C:\Users\Ivan\Documents\GitHub\MyPrograms\DefaultOpener")
    else:
        odabirImagea = easygui.fileopenbox("Odaberi Image file: ", "", r"C:\Users\Ivan\Documents\GitHub\MyPrograms\DefaultOpener")

else:
    print("WIP")

