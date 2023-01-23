import random
print("==============================================================")
valor = int(input("Digite o Valor do atributo que deseja rolar"))

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





dado = random.randint(1,int(20))


resultado = (mod + dado) 

print("==============================================================")
print("O D20 caiu no..... ", dado)
print("O Resultado do teste foi: ", resultado)
