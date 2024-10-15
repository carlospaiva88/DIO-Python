def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no data base
    print(f'Carro inserido com sucesso! {marca}, {modelo}, {ano}, {placa}')

salvar_carro('Renault', 'Duster', 2013, 'OMJ8I88')

# metodo *args = tuplas **kwargs = dicionario