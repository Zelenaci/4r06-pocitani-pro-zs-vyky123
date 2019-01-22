"""
Created on Tue Jan 22 09:53:37 2019

@author: vyk35227
"""

import tkinter as tk
from random import randint

main = tk.Tk()

def plus():
    global vysledek
    x = randint(0,99)
    y = randint(0, 100 - x)
    vysledek = x + y
    
    cisloAentry.config(state="normal")
    cisloBentry.config(state="normal")
    znamenkoEntry.config(state="normal")
    
    znamenkoEntry.delete(0, tk.END)
    znamenkoEntry.insert(0, "  + ")
    cisloAentry.delete(0, tk.END)
    cisloAentry.insert(0, x)
    cisloBentry.delete(0, tk.END)
    cisloBentry.insert(0, y)
    
    cisloAentry.config(state="readonly")
    cisloBentry.config(state="readonly")
    znamenkoEntry.config(state="readonly")
    
def kontrola():
    global vysledek
    spravne = vysledekEntry.get()
    if vysledek == spravne:     #nefakčí
        print("Správně")
    else:
        print("Nesprávně")


#výběr operace
tk.Label(main, text="Operace:").grid()
tk.Radiobutton(main, text="Plus", value=0, command=plus).grid(row=0, column=1)
tk.Radiobutton(main, text="Mínus",value=1).grid(row=1, column=1)
tk.Radiobutton(main, text="Krát",value=2).grid(row=2, column=1)
tk.Radiobutton(main, text="Děleno",value=3).grid(row=3, column=1)
#číslo A
cisloAentry = tk.Entry(main, state="readonly", width=3)
cisloAentry.grid(row=5, column=0,  sticky=tk.W)
#znaménko
znamenkoEntry=tk.Entry(main, state="readonly", width=3)
znamenkoEntry.grid(row=5, column=1, sticky=tk.W)
#číslo B
cisloBentry = tk.Entry(main, state="readonly", width=3)
cisloBentry.grid(row=5, column=2,  sticky=tk.W)
#rovná se
tk.Label(main, text="=").grid(row=5,column=3)
#výsledek
vysledekEntry=tk.Entry(main, width=3)
vysledekEntry.grid(row=5, column=4)
#kontrola
tk.Button(main, text="Kontrola", command=kontrola).grid(column=1)

main.mainloop()
