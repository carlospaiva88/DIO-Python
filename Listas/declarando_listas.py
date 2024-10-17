frutas = ['laranja', 'pera', 'maça,' 'banana']
print(frutas)

frutas = []
print(frutas)

letras = list('python')
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Reanult', 'Duster', 2013, 230000, 'Goiânia', True]

numeros = [1, 45, 556, 673, 45, 23, 35, 867]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

codigo = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(codigo)

