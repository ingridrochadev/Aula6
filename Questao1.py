lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def dobrar(lista):
    return map(lambda x: x * 2, lista)

def pares(lista):
    return filter(lambda x: x % 2 == 0, lista)

def main():
    lista_dobrada = dobrar(lista)
    resultado = pares(lista_dobrada)
    return list(resultado)

print(main())