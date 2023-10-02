import random
from tkinter import *
from tkinter import ttk



def DiceRoller20():
    Resultado20 = ("=", random.randint(1,int(20)))
    texto_d20["text"] = Resultado20

def DiceRoller12():
    Resultado12 = ("=", random.randint(1,int(12)))
    texto_d12["text"] = Resultado12


def modifier():
    valor = () #Adicionar o valor do atributo

#region Valores
    if valor == 1 :
     mod = -5
    elif valor == 2 or valor == 3 :
        mod = -4
            
    elif valor == 4 or valor == 5 :
        mod = -3
                
    elif valor == 6 or valor == 7 :
        mod = -2
                
    elif valor == 8 or valor == 9 :
        mod = -1
                
    elif valor == 10 or valor == 11 :
        mod = 0
                
    elif valor == 12 or valor == 13 :
        mod = 1
                
    elif valor == 14 or valor == 15 :
        mod = 2
                
    elif valor == 16 or valor == 17 :
        mod = 3
                
    elif valor == 18 or valor == 19 :
        mod = 4
                
    elif valor == 20 or valor == 21 :
        mod = 5
                
    elif valor == 22 or valor == 23 :
        mod = 6
                
    elif valor == 24 or valor == 25 :
        mod = 7
                
    elif valor == 26 or valor == 27 :
        mod = 8
                
    elif valor == 28 or valor == 29 :
        mod = 9
                
    elif valor >= 30:
        mod = 10
#endregion
    dado = random.randint(1,int(20))

    Resultado = (mod + dado)


janela = Tk()
janela.title("Dungeon & Dragons Dice Roller ver2.0")

#Botão do D20
botaod20 = Button(janela, text="Rolar um D20", command= DiceRoller20)
botaod20.grid(column=2, row=1)
texto_d20 = Label(janela,text="")
texto_d20.grid(column=3, row=1)

#botão do D12
botaod12 = Button(janela, text="Rolar um D12", command= DiceRoller12)
botaod12.grid(column=2, row=2)
texto_d12 = Label(janela,text="")
texto_d12.grid(column=3, row=2)
janela.mainloop()