from tkinter import *
from tkinter.ttk import *

root = Tk()

Label(root, text='Click on defeated BOSSES!', font=('Verdana', 15)).pack(side=TOP, pady=10)

background = PhotoImage(file=r"C:\Users\Ivan\Documents\GitHub\MyPrograms\TemporaryPyFiles\DS3_Bosses\ds3_wallpaper_blue.png")
photo0 = PhotoImage(file=r"C:\Users\Ivan\Documents\GitHub\MyPrograms\TemporaryPyFiles\DS3_Bosses\Iudex_Gundyr.png")
photo1 = PhotoImage(file=r"C:\Users\Ivan\Documents\GitHub\MyPrograms\TemporaryPyFiles\DS3_Bosses\Vordt_of_the_Boreal_Valley.png")

backgroundLabel = Label(root, image=background)
backgroundLabel.pack(side='top', fill='both', expand='yes')

panel = Label(root).pack(side='top', fill='both', expand='yes')

Button(panel, text='', image=photo0).pack(side=TOP)
Button(panel, text='', image=photo1).pack(side=TOP)


root.mainloop()
