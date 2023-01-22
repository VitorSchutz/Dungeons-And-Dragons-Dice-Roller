import random

loop = 's'

while loop == 's':
     Dice = int(input("Digite o valor do dado que deseja rolar: "))
     Resultado = random.randint(1,int(Dice))
    
     print(Resultado)
     loop = input("Deseja Rolar mais um Dado? (S ou N)").lower()