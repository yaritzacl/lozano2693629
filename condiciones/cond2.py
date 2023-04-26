#este programa dra los diferentes resultados de los operadores
#inicio del ciclo
num1,num2=100,25
#podra seleccionar la opcion del operador 
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
selector=(input('Digite la opcion'))
match selector: #mostrar el resultado dependiendo la opcion seleccionada  
    case '1':
        print(num1+num2)
    case '2':
        print(num1-num2)
    case '3':
        print(num1*num2)
    case '4':
        print(num1/num2)
