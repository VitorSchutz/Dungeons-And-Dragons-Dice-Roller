import random

Força = 0
Destreza = 0
Constituição = 0
Sabedoria = 0
Carisma = 0
repetir = "S"
loop = False



print("Bem-Vindo ao programa de rolagem e desenvolvimento de fichas de D&D")
print("==============================================================")
print("Agora irei fazer algumas perguntas sobre o seu personagem, responda todas elas")

Força = int(input("Qual o valor do seu atributo de Força?"))
Destreza = int(input("Qual o valor do seu atributo de Destreza?"))
Constituição = int(input("Qual o valor do seu atributo de Constituição?"))
Sabedoria = int(input("Qual o valor do seu atributo de Sabedoria?"))
Carisma = int(input("Qual o valor do seu atributo de Carisma?"))


print("==============================================================")
print("Muito bem, agora você esta pronto para usar o sistema de rolagem de dados & atributos")



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
        print("Formato Invalido, insira um valor correto")
    

