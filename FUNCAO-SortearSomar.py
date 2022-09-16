from random import randint

numeros = list()


def sorteia():
   for c in range(0,5):
    numeros.append(randint(1,20))

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares deu um total de {soma}')

sorteia()
print(numeros)
somaPar(numeros)
