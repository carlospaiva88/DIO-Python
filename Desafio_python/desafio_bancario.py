menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
cliente = "Carlos"
saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_saque = saldo
movimentacoes = []



while True:
    opcao = input(menu)

    if opcao == "d":
    
        try:
            depositar = float(input('Quanto quer depositar?\n'))
            if depositar >0:
                saldo += depositar
                movimentacoes.append(f'Deposito: R$ {depositar:.2f}')
                print("Deposito realizado com sucesso!")
            else:
                print('Valor invalido! O deposito precisa ser positivo!')
        except ValueError:
            print('Por favor, insira um valor numerico valido.')

    elif opcao == "s":
        try:    
            sacar = float(input('Qual valor deseja sacar?\n'))
            if sacar > saldo:
                print('Saldo insuficiente!')
            elif sacar > limite_diario:
                print('O valor maximo para saque é de R$ {limite_diario:.2f} por transação.')
            elif numero_saques >= LIMITE_SAQUES:
                print('Número máximo de saques diários excedido.')
            else:
                saldo -= sacar
                numero_saques += 1
                movimentacoes.append(f'Saque: R$ {sacar:.2f}')
                print(f'Saque de R$ {sacar:.2f} realizado com sucesso!')
        except ValueError:
            print('Por favor insira um valor numerico valido!')
        


    elif opcao == "e":
        print("\n =============== EXTRATO ===============")
        if movimentacoes:
            for movimentacao in movimentacoes:
                print(movimentacao)
            else:
                print("Não foram realizadas movimentações.")
            print(f'\n Saldo atual: R$ {saldo:.2f}')
            print('=============================\n')


    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione uma das opções!")