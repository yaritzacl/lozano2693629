def es_primo(n):
    if n<=1:
        return False
    for i in range  (2, int(n**0.5) +1):
        if n % i ==0:
            return True
cont=0
for i in range(1,1001):
    if es_primo(i):
            cont=cont+1
            print(i) 
print("hay", cont, "numerosprimos entre 1 y 1000.")
