# A estrutura de repetição while é usada para repetir um bloco de codigo varias vezes,
# Faz sentido usar o while quando não sabemos o numero exato de vezes que o nosso bloco,
# de codigo deve ser executado.

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))

    if opcao == 1:
        print('Sacando..')
    elif opcao == 2:
        print('Exibindo o extrato..')
else:
    print('Obrigado por usar nosso sistema bancario, ate logo! ')

for numero in range(100):
    if numero == 88:
        break
    
    if numero % 2 == 0:
        continue

    print(numero, end=' ')