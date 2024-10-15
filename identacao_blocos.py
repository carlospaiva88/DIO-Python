def sacar(valor: float):
    saldo = 500
    
    if saldo >= valor:
        print('Valor sacado com sucesso!')
    else:
        print('Valor insuficiente!')

sacar(600)

def depositar(valor: float):
    saldo = 500
    saldo += valor

    