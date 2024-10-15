nome = 'Carlos'
idade = 30
profissao = 'Programador'
linguagem = 'Python'
saldo = 88.960

dados = { 'nome': 'Carlos', 'idade': 30}

print("Nome': %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
#print("Nome: {1} Idade: {0} Nome: {1} {1}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f'Nome: {nome} Idade: {idade}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:12.2f}')