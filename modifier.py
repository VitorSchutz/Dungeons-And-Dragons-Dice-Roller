import random

valor = int(input("Digite o Valor do atributo que deseja rolar"))

if valor == 1 :
    mod = -5
if valor == 2 or 3 :
    mod = -4
if valor == 4 or 5 :
    mod = -3
if valor == 6 or 7 :
    mod = -2
if valor == 8 or 9 :
    mod = -1
if valor == 10 or 11 :
    mod = 0
if valor == 12 or 13 :
    mod = 1
if valor == 14 or 15 :
    mod = 2
if valor == 16 or 17 :
    mod = 3
if valor == 18 or 19 :
    mod = 4
if valor == 20 or 21 :
    mod = 5
if valor == 22 or 23 :
    mod = 6
if valor == 24 or 25 :
    mod = 7
if valor == 26 or 27 :
    mod = 8
if valor == 28 or 29 :
    mod = 9
if valor >= 30:
    mod = 10



dado = random.randint(1,int(20))

print(valor)
print(dado)
print(mod)
