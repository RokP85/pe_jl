# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox

jedilnik = [{}]

def dodaj_in_shrani():
    jedilnik = [{}]
    nov_meni = jedilnik.append((meni_vnos.get(), cena_vnos.get()))
    jedilni_list = open("menu.txt", "a") # zapis menijev v datoteko menu.txt
    jedilni_list.write("Danes nudimo:\n")
    jedilni_list.write(nov_meni)
    tkMessageBox.showinfo("Vnos shranjen")
    jedilni_list.close()
    meni_vnos.select_clear()
    cena_vnos.select_clear()

def meniji():
    tkMessageBox.Message(jedilnik)

window = Tkinter.Tk()

naslov = Tkinter.Label(window, text="Program za kreiranje jedilnika")
naslov.pack()

meni = Tkinter.Label(window, text="Vnesi meni:") # vnos menijev
meni.pack()
meni_vnos = Tkinter.Entry(window)
meni_vnos.pack()

cena = Tkinter.Label(window, text="Vpiši ceno (brez znaka €):")  # vnos cen
cena.pack()
cena_vnos = Tkinter.Entry(window)
cena_vnos.pack()

input = Tkinter.Button(window, text="Dodaj&shrani meni", command=dodaj_in_shrani)
input.pack()

datoteka = Tkinter.Label(window, text="Jedilnik lahko natisnete iz datoteke ˝menu.txt˝")
datoteka.pack()

seznam = Tkinter.Button(window, text="Pokaži seznam menijev", command=meniji)
seznam.pack()

window.mainloop()