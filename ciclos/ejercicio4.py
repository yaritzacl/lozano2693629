#Determinar cual y cuantos numeros perfectos hay entre 1 y 1000
suma=0
cont=0
divisores=[]
num=1001
for i in range(1,num):
    for j in range(1,i):
        if num%j==0:
            suma+=j
    if num % i == 0:
        divisores.append(i)
        print(divisores)
    

    

    