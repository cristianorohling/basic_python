from datetime import datetime, timedelta

data_atual = datetime.now()

print(data_atual)

dias_futuro = float(input("Digite o numero de dias: "))

print(data_atual + timedelta(dias_futuro) )