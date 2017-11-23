# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox

def racun():
    km = float(vnos.get())
    milje = km * 0.62
    tkMessageBox.showinfo("Milje", milje)

def racun_enter(num):
    km = float(vnos.get())
    milje = km * 0.62
    tkMessageBox.showinfo("Milje", milje)

window = Tkinter.Tk()

pozdrav = Tkinter.Label(window, text="Dobrodošli v pretvorniku razdalj\n"
                                     "Vnesite število km")
pozdrav.pack()

window.bind("<Return>", racun_enter)

vnos = Tkinter.Entry(window)
vnos.pack()

pretvorba = Tkinter.Button(window, text="Pretvori v milje", command=racun)
pretvorba.pack()

window.mainloop()

