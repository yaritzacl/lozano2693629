def obtener_valor_tipo(diccionario, clave):
    if clave in diccionario:
        valor = diccionario[clave]
        tipo = type(valor)  
        return valor, tipo
    else:
        return None, None

mi_diccionario = {'nombre': 'Raton', 'edad': 1, 'peso':'3kilos'}
clave = 'edad'
valor, tipo = obtener_valor_tipo(mi_diccionario, clave)

if valor is not None:
    print(f"El valor asociado a la clave '{clave}' es {valor} y su tipo es {tipo}.")
else:
    print(f"No se encontró la clave '{clave}' en el diccionario.")