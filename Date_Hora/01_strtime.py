from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2024-10-16 17:00'
mascara_ptbr = '%d/%m/%Y %a'
mascara_eng = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_eng)
print(data_convertida)