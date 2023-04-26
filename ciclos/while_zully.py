#inicio del programa para determinar la suma de i del 1 al 10 
i=1 #inicia ciclo 
sum=0 
while i<=10: # ejecuta bloque de codigo mientras 1 sea menor de 10 
    print(i)
    sum+=i #sum=sum+i # 
    i+=1 #i=i+1 # suma de variables de1 en 1 
print('la suma es:',sum)
# inicio de ciclo para deternimar los numeros pares, impares o iguales 
i=0 # inicio de ciclo
sp,si=0,0 # determina si los numeros son par o impar  
while i<=10:   
    print(i)
    if i%2==0: 
        sp+=i # determina si los numeros de i son par 
    else:
        si+=i #determina si los numeros de i son impar 
    i+=1 
print('la suma de los pares es:',sp)
print('la suma de los impares es:',si)