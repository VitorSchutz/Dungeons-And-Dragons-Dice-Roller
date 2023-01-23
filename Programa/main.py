repetir = "S"
loop = False

print("Bem-Vindo ao programa de rolagem e desenvolvimento de fichas de D&D")

while repetir == "S" :
    print("==============================================================")
    print("Digite 'D' para rolar um Dado")
    print("Digite 'F' para rolar um valor de atributo")
    res = input("Digite: ").lower()
    
    try:
        if res == "d" : 
                exec(open("DiceRoller.py").read())

        if res == "f" :
            exec(open("modifier.py").read())


    except: 
        print("==============================================================")
    

