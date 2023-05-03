#
man=0 
num_posi= int(input("introduce un numero"))
num_posi= int(input("introduce otro numero positivo o negativo"))

while num_posi >=0:
    if num_posi> man:
        man=num_posi
print("el maimo numero positivo introducido es:", man)