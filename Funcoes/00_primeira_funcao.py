def exibir_mensagem():
    print('Hello, World!')

def exibir_mensagem_2(nome):
    print(f'Welcome! {nome}')

def exibir_mensagem_3(nome='Anonymus'):
    print(f'Welcome {nome}')

exibir_mensagem()
exibir_mensagem_2(nome='Carlos')
exibir_mensagem_3()
exibir_mensagem_3(nome='Antonio')