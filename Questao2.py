lista = ['Suponha que você tenha uma lista de strings', 'representando frases', 'Crie uma função em Python',
            'que recebe essa lista', 'e duas funções de ordem superior como argumentos']

def separar_palavras(lista):
    return [frase.split() for frase in lista]

def gritar(lista):
    return [word.upper() for phrase in lista for word in phrase]

def main():
    frase_separada = separar_palavras(lista)
    resultado = gritar(frase_separada)
    return resultado

print(main())
