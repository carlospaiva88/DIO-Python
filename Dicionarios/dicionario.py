# Um dicionario é um conjunto não ordenado de pares, chave e valor. Sendo delimitados por chave{}

pessoa = {'nome': 'Carlos', 'idade': 30}

pessoa = dict(nome='Carlos', idade=30)

pessoa['telefone'] = '48-991068048'

print(pessoa)


dados = {'nome': 'Carlos', 'idade': 30, 'telefone': '745555441'}

dados['nome']



contatos= {
    'carloscjr60@gmail.com': {'nome': 'Carlos', 'telefone': '944445211', 'endereco': 'Francisco Alves'},
    'macaxera@gmail.com': {'nome': 'Sebastian', 'telefone': '54887779'},
    'josefino@gmail.com': {'nome': 'Josevaldo', 'telefone': '877878436'},
    'ferdinando@gmail.com': {'nome': 'Ferdinando Rodrigues', 'telefone': '848778484'},
}

telefone = contatos['carloscjr60@gmail.com']['telefone']
print(telefone)

endereco = contatos['carloscjr60@gmail.com']['endereco']
print(endereco)

for chave in contatos:
    print(chave, contatos[chave])
print('=' *100)

for chave, valor in contatos.items():
    print(chave, valor)


contatos.get() # pega o item 
contatos.items() # lista os items
contatos.keys() # lista as chaves 
contatos.pop() # remove o valor fornecido
contatos.values() # retorna valores