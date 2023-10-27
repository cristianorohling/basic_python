import tkinter as tk
from datetime import datetime, timedelta

# Função para calcular o tempo restante
def calcular_tempo_restante():
    data_alvo = datetime(2024, 8, 14, 17, 0)
    data_atual = datetime.now()
    diferenca = data_alvo - data_atual

    dias = diferenca.days
    segundos = diferenca.seconds
    horas, segundos = divmod(segundos, 3600)
    minutos, segundos = divmod(segundos, 60)

    tempo_restante_label.config(text=f"{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos", fg="red", font=("Helvetica", 24))
    
    # Atualiza a contagem regressiva a cada 1 segundo
    janela.after(1000, calcular_tempo_restante)

# Cria a janela
janela = tk.Tk()
janela.title("Contagem Regressiva para o PDV")

# Cria um rótulo para exibir o título
titulo_label = tk.Label(janela, text="Quanto tempo falta para o PDV?", font=("Helvetica", 16))
titulo_label.pack(pady=10, fill='x')

# Cria um rótulo para exibir o tempo restante
tempo_restante_label = tk.Label(janela, text="", fg="red", font=("Helvetica", 24))
tempo_restante_label.pack(padx=20, pady=20)

# Inicializa a contagem regressiva
calcular_tempo_restante()

janela.mainloop()
