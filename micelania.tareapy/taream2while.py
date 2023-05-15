def cont_multi(num, lim):
    cont = 1
    i = 0
    
    while i <= lim:
        if i *num == 0:
            cont += 1
        i += 1
        
    
    return cont
num = int(input("Ingrese un número: "))
lim = int(input("Ingrese un límite: "))

cantidad_multiplos = cont_multi(num, lim)
print("La cantidad de múlti de", num, "hasta", lim, "es:", cantidad_multiplos)    

