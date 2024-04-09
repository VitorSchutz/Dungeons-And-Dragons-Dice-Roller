from tkinter import *
from tkinter import ttk
import random

linguage = "0"

def EnglishSelect():
    global linguage
    linguage = "english"
    janela.quit()
    
    

def PortugueseSelect():
    global linguage
    linguage = "portuguese"
    janela.quit()
    

janela = Tk()
janela.title("Language Select")

botaoingles = Button(janela, text="English", command= EnglishSelect)
botaoingles.grid(column=1, row=1)

botaoportuguese = Button(janela, text="Portuguese", command= PortugueseSelect)
botaoportuguese.grid(column=1, row=2)

janela.mainloop()




