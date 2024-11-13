import tkinter as tk
from datetime import datetime

def atualizar_hora():
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M:%S")
    label_hora.config(text=hora_atual)
    label_hora.after(1000, atualizar_hora)  # Atualiza a cada 1000 milisegundos (ou 1 segundo)

janela = tk.Tk()
janela.title("Relógio em Tempo Real")

label_hora = tk.Label(janela, font=("Helvetica", 48), fg="black")
label_hora.pack()

atualizar_hora()
janela.mainloop()