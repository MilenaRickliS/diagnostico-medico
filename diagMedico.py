import networkx as nx
import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Carregar dados médicos em um dataframe pandas
data = pd.read_csv('medical_data.csv')

# Pré-processar os dados para criar uma base de conhecimento estruturada
data.dropna(inplace=True)  # Remove linhas com valores ausentes
data.drop_duplicates(inplace=True)  # Remove linhas duplicadas

# Criar um dicionário para armazenar a base de conhecimento, com sintomas em letras minúsculas
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

# Definir uma função para processar a entrada do usuário
def processar_entrada(texto_entrada):
    tokens = texto_entrada.lower().split()  # Normaliza para minúsculas e tokeniza
    return tokens

# Definir uma função para realizar diagnóstico e planejamento de tratamento
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

# Definir uma função para lidar com a entrada do usuário e perguntar sobre os sintomas
def lidar_entrada():
    # Perguntar ao usuário o que ele está sentindo
    texto_entrada = input("Por favor, descreva seus sintomas: ")
    tokens = processar_entrada(texto_entrada)
    sintomas = [token for token in tokens if token in base_conhecimento]
    
    # Obter diagnóstico e tratamento com base nos sintomas
    diagnostico, tratamento = diagnosticar(sintomas)
    
    # Gerar resposta com base no diagnóstico e tratamento
    if diagnostico and tratamento:
        resposta = 'Com base nos seus sintomas, os possíveis diagnósticos são: {}\nOs possíveis tratamentos são: {}'.format(diagnostico, tratamento)
    else:
        resposta = 'Nenhum diagnóstico ou tratamento correspondente foi encontrado para os sintomas fornecidos.'
    print(resposta)

# Executar a interação
lidar_entrada()
