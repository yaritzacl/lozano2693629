suma=0
cont=0
divisores=[]
num=1001
num2=1
for i in range(num2,num):
        suma=suma-i
        while not (i<=1000):
                if num % i == 0:
                        divisores.append(i)
print(divisores)
