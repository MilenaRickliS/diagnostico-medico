import networkx as nx
import pandas as pd
import nltk
from tkinter import Tk, Label, Listbox, Button, messagebox, font, Scrollbar, Frame

nltk.download('punkt')

# Load medical data into a pandas DataFrame with all symptoms, diseases, and treatments aligned
data = pd.DataFrame({
    'sintoma': ['febre', 'tosse', 'dor de cabeça', 'dor de garganta', 'coriza',
                'dor muscular', 'fadiga', 'dor no peito', 'falta de ar', 'tontura',
                'suor noturno', 'perda de peso', 'inchaço', 'confusão mental', 'visão turva',
                'náusea', 'vômito', 'diarreia', 'erupção cutânea', 'dificuldade para engolir',
                'suor frio', 'sede excessiva', 'coceira', 'icterícia', 'ansiedade',
                'palpitações', 'fraqueza muscular', 'manchas vermelhas', 'dor articular'],
    'doenca': ['gripe', 'gripe', 'enxaqueca', 'amigdalite', 'resfriado',
               'gripe', 'anemia', 'doença cardíaca', 'asma', 'vertigem',
               'tuberculose', 'câncer', 'doença renal', 'AVC', 'diabetes',
               'gastroenterite', 'intoxicação alimentar', 'alergia', 'esofagite', 'faringite',
               'ataque cardíaco', 'diabetes descontrolada', 'alergia severa', 'hepatite viral', 'ataque de pânico',
               'ataque cardíaco', 'hipotensão', 'zika vírus', 'zika vírus'],
    'tratamento': ['repouso e hidratação', 'xarope para tosse', 'analgésicos',
                   'antibióticos', 'descongestionantes', 'analgésicos',
                   'suplementos de ferro', 'monitoramento cardíaco', 'bombinha',
                   'medicamento para vertigem', 'antibióticos', 'quimioterapia',
                   'diuréticos', 'atendimento emergencial', 'controle de glicose',
                   'hidratação e repouso', 'medicamentos antieméticos', 'antihistamínicos',
                   'inibidores de bomba de prótons', 'antibióticos',
                   'atendimento emergencial', 'controle de glicose', 'antihistamínicos',
                   'medicamentos antivirais', 'calmantes', 'atendimento emergencial',
                   'suplementação de sódio', 'repouso e hidratação', 'analgésicos']
})

# Adicionando doenças com combinações específicas de sintomas
doencas_especificas = {
    frozenset(['febre', 'tosse', 'fadiga']): 'tuberculose',
    frozenset(['dor de cabeça', 'confusão mental', 'visão turva']): 'AVC',
    frozenset(['fadiga', 'perda de peso', 'suor noturno']): 'câncer',
    frozenset(['dor no peito', 'falta de ar', 'inchaço']): 'doença cardíaca grave',
    frozenset(['náusea', 'vômito', 'diarreia']): 'gastroenterite',
    frozenset(['febre', 'dor muscular', 'dor de cabeça']): 'dengue',
    frozenset(['tosse', 'falta de ar', 'febre']): 'pneumonia',
    frozenset(['dor de garganta', 'febre', 'dificuldade para engolir']): 'faringite estreptocócica',
    frozenset(['dor de cabeça', 'tontura', 'fadiga']): 'hipoglicemia',
    frozenset(['dor no peito', 'falta de ar', 'suor frio']): 'ataque cardíaco',
    frozenset(['visão turva', 'fadiga', 'sede excessiva']): 'diabetes descontrolada',
    frozenset(['erupção cutânea', 'coceira', 'inchaço']): 'alergia severa',
    frozenset(['febre', 'náusea', 'icterícia']): 'hepatite viral',
    frozenset(['dor muscular', 'fadiga', 'inchaço']): 'fibromialgia',
    frozenset(['dor abdominal', 'vômito', 'diarreia']): 'apendicite',
    frozenset(['dor no peito', 'ansiedade', 'palpitações']): 'ataque de pânico',
    frozenset(['tontura', 'confusão mental', 'fraqueza muscular']): 'hipotensão',
    frozenset(['febre', 'manchas vermelhas', 'dor articular']): 'zika vírus'
}

# Preprocess data
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

# Create a knowledge base dictionary
base_conhecimento = {}
for index, row in data.iterrows():
    sintoma = row['sintoma'].strip().lower()
    doenca = row['doenca']
    tratamento = row['tratamento']
    if doenca not in base_conhecimento:
        base_conhecimento[doenca] = {'sintomas': set(), 'tratamento': tratamento}
    base_conhecimento[doenca]['sintomas'].add(sintoma)

# Function to diagnose based on selected symptoms
def diagnosticar(sintomas):
    melhor_diagnostico = None
    max_correspondencias = 0

    # Check for specific combinations first
    for combinacao, doenca in doencas_especificas.items():
        if combinacao.issubset(set(sintomas)):
            melhor_diagnostico = doenca
            break

    # If no specific combination is found, look for the disease with the most matching symptoms
    if not melhor_diagnostico:
        for doenca, info in base_conhecimento.items():
            correspondencias = len(info['sintomas'].intersection(sintomas))
            if correspondencias > max_correspondencias:
                max_correspondencias = correspondencias
                melhor_diagnostico = doenca

    # Get the corresponding treatment
    if melhor_diagnostico:
        tratamento = base_conhecimento[melhor_diagnostico]['tratamento']
        return melhor_diagnostico, tratamento
    else:
        return None, None

# Function to handle symptom selection
def obter_diagnostico():
    sintomas_selecionados = listbox.curselection()
    sintomas = [listbox.get(i) for i in sintomas_selecionados]
    
    diagnostico, tratamento = diagnosticar(sintomas)
    
    if diagnostico and tratamento:
        resposta = f'Diagnóstico mais provável: {diagnostico}\n\nTratamento recomendado: {tratamento}'
    else:
        resposta = 'Nenhum diagnóstico ou tratamento correspondente foi encontrado para os sintomas fornecidos.'
    
    messagebox.showinfo("Resultado", resposta)

# Create the graphical interface
root = Tk()
root.title("Sistema de Diagnóstico Médico")
root.geometry("600x500")

# Configure fonts
titulo_font = font.Font(family="Helvetica", size=16, weight="bold")
texto_font = font.Font(family="Helvetica", size=12)
texto_font2 = font.Font(family="Helvetica", size=10)

# Title
titulo_label = Label(root, text="Bem-vindo ao Sistema de Diagnóstico Médico", font=titulo_font)
titulo_label.pack(pady=10)

# Explanation
explicacao_label = Label(root, text="Selecione seus sintomas na lista abaixo e clique em 'Obter Diagnóstico'.", font=texto_font)
explicacao_label.pack(pady=5)

# Frame for the Listbox and Scrollbar
frame = Frame(root)
frame.pack(pady=10)

# Listbox for symptom selection
listbox = Listbox(frame, selectmode='multiple', font=texto_font, width=50, height=10)
for sintoma in sorted(set(symptom for info in base_conhecimento.values() for symptom in info['sintomas'])):
    listbox.insert('end', sintoma)

# Add a scrollbar
scrollbar = Scrollbar(frame, orient="vertical", command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
listbox.pack(side='left', fill='both')

# Button to get the diagnosis
botao_diagnostico = Button(root, text="Obter Diagnóstico", command=obter_diagnostico, font=texto_font)
botao_diagnostico.pack(pady=10)

# Information label
informacao_label = Label(root, text="Nota: Este sistema é apenas informativo.", font=texto_font2, fg="red")
informacao_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
