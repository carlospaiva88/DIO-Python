# Estruturas de repetição com FOR devem ser utilizadas para 
# repetir um trecho de codigo por um determinado numero de vezes
# atraves de uma expressão logica, então faz sentido usarmos quando sabemos o numero exato de vezes,
# ou quando queremos percorrer um objeto iteravel.


texto = input('informe um texo:')
VOGAIS = 'AEIOU'

# exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print() # add uma quebra de linha


# exmplo utilizando a função built-in range

for numero in range(0, 55, 3):
    print(numero, end=' ')