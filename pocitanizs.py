"""
Created on Tue Jan 22 09:53:37 2019

@author: vyk35227
"""

import tkinter as tk
from random import randint, randrange

main = tk.Tk()
main.title("Počítání")

global dobre
global spatne
dobre = 0
spatne = 0

def plus():
    global vysledek
    x = randint(0,99)
    y = randint(0, 100 - x)
    vysledek = x + y
    
    cisloAentry.config(state="normal")
    cisloBentry.config(state="normal")
    znamenkoEntry.config(state="normal")
    vysledekEntry.config(state="normal")
    
    znamenkoEntry.delete(0, tk.END)
    znamenkoEntry.insert(0, "  +")
    cisloAentry.delete(0, tk.END)
    cisloAentry.insert(0, x)
    cisloBentry.delete(0, tk.END)
    cisloBentry.insert(0, y)
    cisloAentry.config(state="readonly")
    cisloBentry.config(state="readonly")
    znamenkoEntry.config(state="readonly")
    


def minus():
    global vysledek
    x = randint(1, 100)         
    y = randrange(0, x)
    
    vysledek = x - y
    
    cisloAentry.config(state="normal")
    cisloBentry.config(state="normal")
    znamenkoEntry.config(state="normal")
    vysledekEntry.config(state="normal")
    
    znamenkoEntry.delete(0, tk.END)
    znamenkoEntry.insert(0, "  -")
    cisloAentry.delete(0, tk.END)
    cisloAentry.insert(0, x)
    cisloBentry.delete(0, tk.END)
    cisloBentry.insert(0, y)
    
    cisloAentry.config(state="readonly")
    cisloBentry.config(state="readonly")
    znamenkoEntry.config(state="readonly")
    
def krat():
    global vysledek
    x = randint(0, 10)         
    y = randint(0, 9)
    vysledek = x * y
    
    cisloAentry.config(state="normal")
    cisloBentry.config(state="normal")
    znamenkoEntry.config(state="normal")
    vysledekEntry.config(state="normal")
    
    znamenkoEntry.delete(0, tk.END)
    znamenkoEntry.insert(0, "  *")
    cisloAentry.delete(0, tk.END)
    cisloAentry.insert(0, x)
    cisloBentry.delete(0, tk.END)
    cisloBentry.insert(0, y)
    
    cisloAentry.config(state="readonly")
    cisloBentry.config(state="readonly")
    znamenkoEntry.config(state="readonly")        
    
def deleno():
    global vysledek
    vysledek = randrange(1, 11)
    y = randint(1, 10)
    x = vysledek * y                      
    
    cisloAentry.config(state="normal")
    cisloBentry.config(state="normal")
    znamenkoEntry.config(state="normal")
    vysledekEntry.config(state="normal")
    
    znamenkoEntry.delete(0, tk.END)
    znamenkoEntry.insert(0, "  /")
    cisloAentry.delete(0, tk.END)
    cisloAentry.insert(0, x)
    cisloBentry.delete(0, tk.END)
    cisloBentry.insert(0, y)
    
    cisloAentry.config(state="readonly")
    cisloBentry.config(state="readonly")
    znamenkoEntry.config(state="readonly")        
    
def kontrola():
    global vysledek
    global dobre
    global spatne
    
    cisloAentry.config(state="normal")
    cisloBentry.config(state="normal")
    znamenkoEntry.config(state="normal")
    vysledekEntry.config(state="normal")
    
    try:
        spravne = int(vysledekEntry.get())
        cisloAentry.delete(0, tk.END)
        cisloBentry.delete(0, tk.END)
        
        if vysledek == spravne:
            print("Správně")
            stavLabel.config(text="Správně!")
            dobre += 1
            dobreLabel.config(text="Správně: %d" % dobre)
            
        else:
            print("Nesprávně")
            stavLabel.config(text="Špatně!")
            spatne += 1
            spatneLabel.config(text="Špatně: %s" % spatne)
        
    except ValueError:
        stavLabel.config(text="Chyba!")
          
    cisloAentry.delete(0, tk.END)
    cisloBentry.delete(0, tk.END)
    znamenkoEntry.delete(0, tk.END)
    cisloAentry.config(state="readonly")
    cisloBentry.config(state="readonly")
    znamenkoEntry.config(state="readonly")
    vysledekEntry.delete(0, tk.END)
    vysledekEntry.config(state="readonly")
    
def enter(event):
    kontrola()
main.bind('<Return>', enter)



#výběr operace
tk.Label(main, text="Operace:").grid()
tk.Radiobutton(main, text="Plus", value=0, command=plus).grid(row=0, column=1)
tk.Radiobutton(main, text="Mínus",value=1, command=minus).grid(row=1, column=1)
tk.Radiobutton(main, text="Krát",value=2, command=krat).grid(row=2, column=1)
tk.Radiobutton(main, text="Děleno",value=3, command=deleno).grid(row=3, column=1)
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
vysledekEntry=tk.Entry(main, width=3, state="readonly")
vysledekEntry.grid(row=5, column=4)
#kontrola a statistika
tk.Button(main, text="Kontrola", command=kontrola).grid(column=1)
stavLabel = tk.Label(main, text="")
stavLabel.grid(row=7)
dobreLabel = tk.Label(main, text="Dobře: 0")
dobreLabel.grid(row=7, column = 1)
spatneLabel = tk.Label(main, text="Špatně: 0")
spatneLabel.grid(row=7, column = 2)
main.mainloop()
