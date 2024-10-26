import networkx as nx
import pandas as pd
import nltk
from tkinter import Tk, Label, Listbox, Button, messagebox, font

nltk.download('punkt')

# Carregar dados médicos em um dataframe pandas
data = pd.DataFrame({
    'sintoma': ['febre', 'tosse', 'dor de cabeça', 'dor de garganta', 'coriza', 
                'dor muscular', 'fadiga', 'dor no peito', 'falta de ar', 'tontura'],
    'doenca': ['gripe', 'gripe', 'enxaqueca', 'amigdalite', 'resfriado', 
               'gripe', 'anemia', 'doença cardíaca', 'asma', 'vertigem'],
    'tratamento': ['repouso e hidratação', 'xarope para tosse', 'analgésicos', 
                   'antibióticos', 'descongestionantes', 'analgésicos', 
                   'suplementos de ferro', 'monitoramento cardíaco', 
                   'bombinha', 'medicamento para vertigem']
})

# Pré-processar os dados para criar uma base de conhecimento estruturada
data.dropna(inplace=True)  # Remove linhas com valores ausentes
data.drop_duplicates(inplace=True)  # Remove linhas duplicadas

# Criar um dicionário para armazenar a base de conhecimento
base_conhecimento = {}
for index, row in data.iterrows():
    sintoma = row['sintoma'].strip().lower()  # Normaliza para minúsculas
    doenca = row['doenca']
    tratamento = row['tratamento']
    base_conhecimento[sintoma] = {'doenca': doenca, 'tratamento': tratamento}

# Criar uma rede semântica usando NetworkX
G = nx.Graph()
for index, row in data.iterrows():
    sintoma = row['sintoma'].strip().lower()  # Normaliza para minúsculas
    doenca = row['doenca']
    tratamento = row['tratamento']
    
    # Adicionar nós com atributos
    G.add_node(sintoma, label='sintoma')
    G.add_node(doenca, label='doenca')
    G.add_node(tratamento, label='tratamento')
    
    # Adicionar arestas entre os nós com base nos relacionamentos
    G.add_edge(sintoma, doenca)
    G.add_edge(doenca, tratamento)

# Função para diagnosticar com base nos sintomas selecionados
def diagnosticar(sintomas):
    diagnosticos_possiveis = set()
    tratamentos_possiveis = set()
    
    for sintoma in sintomas:
        if sintoma in G:  # Verificar se o nó do sintoma existe no grafo
            vizinhos = list(G.neighbors(sintoma))
            for doenca in vizinhos:
                if G.nodes[doenca].get('label') == 'doenca':
                    diagnosticos_possiveis.add(doenca)
                    # Encontrar tratamentos ligados à doença
                    for tratamento in G.neighbors(doenca):
                        if G.nodes[tratamento].get('label') == 'tratamento':
                            tratamentos_possiveis.add(tratamento)
                            
    return list(diagnosticos_possiveis), list(tratamentos_possiveis)

# Função para lidar com a seleção de sintomas
def obter_diagnostico():
    sintomas_selecionados = listbox.curselection()  # Obtém os índices dos sintomas selecionados
    sintomas = [listbox.get(i) for i in sintomas_selecionados]  # Converte os índices em sintomas
    
    # Obter diagnóstico e tratamento com base nos sintomas
    diagnostico, tratamento = diagnosticar(sintomas)
    
    # Gerar resposta com base no diagnóstico e tratamento
    if diagnostico and tratamento:
                resposta = 'Com base nos seus sintomas, os possíveis diagnósticos são: {}\nOs possíveis tratamentos são: {}'.format(diagnostico, tratamento)
    else:
        resposta = 'Nenhum diagnóstico ou tratamento correspondente foi encontrado para os sintomas fornecidos.'
    
    messagebox.showinfo("Resultado", resposta)

# Criar a interface gráfica
root = Tk()
root.title("Sistema de Diagnóstico Médico")

# Configurar a fonte
titulo_font = font.Font(family="Helvetica", size=16, weight="bold")
texto_font = font.Font(family="Helvetica", size=12)
texto_font2 = font.Font(family="Helvetica", size=10)  # Definindo uma fonte menor

# Título
titulo_label = Label(root, text="Bem-vindo ao Sistema de Diagnóstico Médico", font=titulo_font)
titulo_label.pack(pady=10)

# Explicação
explicacao_label = Label(root, text="Selecione seus sintomas na lista abaixo e clique em 'Obter Diagnóstico'.", font=texto_font)
explicacao_label.pack(pady=5)

# Listbox para seleção de sintomas
listbox = Listbox(root, selectmode='multiple', font=texto_font, width=50, height=10)
for sintoma in base_conhecimento.keys():
    listbox.insert('end', sintoma)  # Adiciona cada sintoma à Listbox

listbox.pack(pady=10)

# Botão para obter o diagnóstico
botao_diagnostico = Button(root, text="Obter Diagnóstico", command=obter_diagnostico, font=texto_font)
botao_diagnostico.pack(pady=10)

# Exemplo de uso de cor no texto
informacao_label = Label(root, text="Nota: Este sistema é apenas informativo.", font=texto_font2, fg="red")  # Usando a cor vermelha
informacao_label.pack(pady=5)

# Iniciar o loop da interface gráfica
root.mainloop()