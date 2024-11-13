import tkinter as tk
import time
from datetime import datetime

class DiagnosticoMedico:
    def __init__(self, root):
        self.sintomas = self.definir_sintomas()
        self.diagnosticos = self.definir_diagnosticos()
        self.sintoma_dependencias = self.definir_dependencias_sintomas()
        
        self.sintomas_presentes = []
        self.sintoma_prioritarios = []
        self.sintoma_atual = iter(self.sintomas.items())
        self.root = root
        self.root.title("IA - Diagnóstico Médico")
        self.diagnostico_encontrado = False
        self.sintomas_ja_perguntados = set()   

        self.configurar_interface()
        self.exibir_mensagem_inicial()
        self.exibir_proxima_pergunta()
        self.atualizar_hora() 

    def definir_sintomas(self):
        return {
            "febre": "Você tem febre?",
            "tosse": "Você tem tosse?",
            "dificuldade_respirar": "Você está tendo dificuldade para respirar?",
            "dor_cabeca": "Você tem dor de cabeça?",
            "dor_garganta": "Você tem dor de garganta?",
            "fadiga": "Você está se sentindo muito cansado?",
            "nausea": "Você está sentindo náuseas?",
            "diarreia": "Você está tendo diarreia?",
            "vomito": "Você está vomitando?",
            "erupcao_cutanea": "Você tem alguma erupção cutânea?",
            "dor_abdominal": "Você tem dor abdominal?",
            "calafrios": "Você está tendo calafrios?",
            "perda_de_apetite": "Você está tendo perda de apetite?",
            "dor_muscular": "Você está sentindo dor muscular?",
            "sudorese": "Você está suando excessivamente?",
            "congestao_nasal": "Você tem congestão nasal?",
            "perda_de_paladar": "Você perdeu o paladar?",
            "dor_articulacoes": "Você tem dor nas articulações?",
            "manchas_na_pele": "Você tem manchas na pele?",
            "suor_noturno": "Você está tendo suor noturno?",
            "linfadenopatia": "Você está com aumento dos gânglios linfáticos?",
            "formigamento": "Você está sentindo formigamento nas extremidades?",
            "rigidez_nucal": "Você está sentindo rigidez no pescoço?",
            "expiracao_prolongada": "Você está tendo dificuldade ao expirar?",
            "sibilo": "Você está sentindo um chiado no peito?",
            "coceira": "Você está com coceira?",
            "lesoes_escamosas": "Você tem lesões escamosas na pele?",
            "inchaço_articular": "Você está com inchaço nas articulações?",
            "rigidez_morning": "Você sente rigidez nas articulações pela manhã?",
            "perda_de_peso": "Você está percebendo perda de peso?",
            "dor_urinaria": "Você sente dor ao urinar?",
            "frequencia_urinaria": "Você tem necessidade frequente de urinar?",
            "tontura": "Você está sentindo tontura?",
            "aumento_sede": "Você está sentindo sede excessiva?",
            "aumento_fome": "Você está sentindo fome excessiva?",
            "inchaco": "Você está com inchaço nas articulações?",
            "disturbios_sono": "Você está tendo distúrbios do sono?",
            "fraqueza_muscular": "Você está sentindo uma fraqueza muscular?",
            "cheiro_urina": "Você percebeu um cheiro forte na urina?"
        }

    def definir_diagnosticos(self):
        return {
            "Gripe": {"febre": 2, "tosse": 2, "dor_cabeca": 1, "fadiga": 1, "calafrios": 2},
            "COVID-19": {"febre": 2, "tosse": 2, "dificuldade_respirar": 3, "fadiga": 1, "perda_de_paladar": 3},
            "Resfriado": {"tosse": 2, "dor_garganta": 2, "fadiga": 1, "congestao_nasal": 2},
            "Gastrite": {"nausea": 2, "dor_cabeca": 1, "dor_abdominal": 3, "perda_de_apetite": 3, "vomito": 3,},
            "Alergia": {"erupcao_cutanea": 2, "tosse": 2, "sudorese": 1, "congestao_nasal": 2},
            "Infecção Alimentar": {"nausea": 2, "vomito": 3, "diarreia": 3, "dor_abdominal": 3},
            "Sinusite": {"dor_cabeca": 1, "dor_garganta": 2, "tosse": 2, "fadiga": 1, "congestao_nasal": 2},
            "Dengue": {"febre": 2, "dor_muscular": 2, "calafrios": 2, "fadiga": 1, "erupcao_cutanea": 2},
            "Hepatite": {"fadiga": 1, "nausea": 2, "perda_de_apetite": 3, "dor_abdominal": 3},
            "Apendicite": {"febre": 2, "dor_abdominal": 3, "nausea": 2, "vomito": 3, "perda_de_apetite": 3,},
            "Zika": {"febre": 2, "erupcao_cutanea": 2, "fadiga": 1, "dor_articulacoes": 2, "manchas_na_pele": 3},
            "Chikungunya": {"febre": 2, "dor_muscular": 2, "dor_articulacoes": 2, "fadiga": 1},
            "Malária": {"febre": 2, "calafrios": 2, "dor_cabeca": 1, "fadiga": 1, "dor_muscular": 2},
            "Tuberculose": {"tosse": 2, "dificuldade_respirar": 3, "febre": 2, "suor_noturno": 2, "perda_de_peso": 3},
            "Pneumonia": {"tosse": 2, "dificuldade_respirar": 3, "febre": 2, "calafrios": 2, "dor_abdominal": 3},
            "Leptospirose": {"febre": 2, "dor_cabeca": 1, "fadiga": 1, "dor_abdominal": 3, "vomito": 3},
            "Câncer de pulmão": {"tosse": 2, "dificuldade_respirar": 3, "febre": 2, "perda_de_peso": 3},
            "Asma": {"tosse": 2, "dificuldade_respirar": 3, "sibilo": 3, "dor_muscular": 2,},
            "DPOC": {"tosse": 2, "dificuldade_respirar": 3, "expiracao_prolongada": 3, "sibilo": 3},
            "Brucelose": {"febre": 2, "dor_muscular": 2, "sudorese": 2, "fadiga": 1, "dor_abdominal": 3},
            "Meningite": {"febre": 2, "dor_cabeca": 1, "rigidez_nucal": 3, "nausea": 2, "vomito": 3},
            "Síndrome de Guillain-Barré": {"fraqueza_muscular": 3, "dificuldade_respirar": 3, "formigamento": 3, "dor_muscular": 2,},
            "Mononucleose": {"febre": 2, "dor_garganta": 2, "linfadenopatia": 3, "fadiga": 1},
            "Doença de Lyme": {"erupcao_cutanea": 2, "febre": 2, "dor_cabeca": 1, "fadiga": 1, "dor_muscular": 2},
            "Psoríase": {"erupcao_cutanea": 2, "coceira": 2, "lesoes_escamosas": 3, "inchaço_articular": 2,},
            "Artrite reumatoide": {"dor_articulacoes": 2, "inchaço_articular": 2, "rigidez_morning": 3, "fadiga": 1,},
            "HIV/AIDS": {"febre": 2, "fadiga": 1, "linfadenopatia": 3, "perda_de_peso": 3},
            "Infecção Urinária": {"dor_urinaria": 2, "frequencia_urinaria": 2, "cheiro_urina": 1, "coceira": 2,},
            "Diabetes Tipo 2": {"aumento_sede": 2, "aumento_fome": 2, "fadiga": 1, "tontura": 1, "perda_peso": 1},
            "Fibromialgia": {"dor_muscular": 2, "fadiga": 2, "disturbios_sono": 2},
        }
        
    def definir_dependencias_sintomas(self):
        return {
            "febre": ["calafrios", "suor_noturno", "fadiga"],
            "tosse": ["dificuldade_respirar", "congestao_nasal", "dor_garganta"],
            "dor_abdominal": ["vomito", "diarreia", "nausea"],
            "dificuldade_respirar": ["sibilo", "expiracao_prolongada"],
            "fadiga": ["perda_de_apetite", "perda_de_peso"],
            "nausea": ["vomito", "diarreia"],
            "erupcao_cutanea": ["coceira", "manchas_na_pele"],
            "dor_muscular": ["fadiga", "calafrios"],
            "linfadenopatia": ["febre", "fadiga"],
            "rigidez_nucal": ["dor_cabeca", "nausea"],
            "sibilo": ["dificuldade_respirar", "tosse"],
            "coceira": ["erupcao_cutanea", "lesoes_escamosas"],
            "inchaço_articular": ["dor_articulacoes", "rigidez_morning"],
            "perda_de_paladar": ["fadiga", "nausea"],
            "suor_noturno": ["febre", "perda_de_peso"],
            "rigidez_morning": ["dor_articulacoes", "inchaço_articular"],
            "formigamento": ["fraqueza_muscular", "dificuldade_respirar"],
            "calafrios": ["febre", "suor_noturno"],
            "perda_de_apetite": ["fadiga", "perda_de_peso"],
            "diarreia": ["vomito", "nausea"],
            "dor_urinaria": ["frequencia_urinaria"],
            "frequencia_urinaria": ["dor_urinaria"],
            "tontura": ["fadiga", "dificuldade_respirar"],
            "aumento_sede": ["aumento_fome"],
            "aumento_fome": ["aumento_sede"],
            "inchaco": ["dor_articulacoes"],
            "disturbios_sono": ["fadiga"],
        }
    def definir_detalhes_diagnosticos(self):
    # Detalhes dos diagnósticos, incluindo sintomas típicos, causas e recomendações
        return {
            "Gripe": {
                "sintomas": "Febre, tosse, dor de cabeça, fadiga, calafrios.",
                "causas": "Vírus respiratório, geralmente transmitido pelo ar.",
                "recomendacao": "Repouso, hidratação e consulta médica se necessário."
            },
            "COVID-19": {
                "sintomas": "Febre, tosse, dificuldade para respirar, fadiga, perda de paladar.",
                "causas": "Vírus SARS-CoV-2, transmitido principalmente por gotículas respiratórias.",
                "recomendacao": "Faça um teste para COVID-19, consulte um médico."
            },
            "Resfriado": {
                "sintomas": "Tosse, dor de garganta, fadiga, congestão nasal.",
                "causas": "Vírus respiratório, como o rinovírus.",
                "recomendacao": "Repouso e ingestão de líquidos. Consulte um médico se houver complicações."
            },
            "Gastrite": {
                "sintomas": "Náusea, dor de cabeça, dor abdominal.",
                "causas": "Inflamação da mucosa do estômago, geralmente causada por infecção bacteriana ou uso excessivo de anti-inflamatórios.",
                "recomendacao": "Evite alimentos irritantes, consulte um médico para prescrição de medicamentos."
            },
            "Alergia": {
                "sintomas": "Erupção cutânea, tosse, sudorese, congestão nasal.",
                "causas": "Reações do sistema imunológico a substâncias como pólen, poeira, ou alimentos.",
                "recomendacao": "Evitar alérgenos conhecidos e utilizar anti-histamínicos. Consulte um alergista."
            },
            "Infecção Alimentar": {
                "sintomas": "Náusea, vômito, diarreia, dor abdominal.",
                "causas": "Bactérias, vírus ou parasitas presentes em alimentos contaminados.",
                "recomendacao": "Hidratação oral e descanso. Consulte um médico se os sintomas persistirem."
            },
            "Sinusite": {
                "sintomas": "Dor de cabeça, dor de garganta, tosse, fadiga, congestão nasal.",
                "causas": "Inflamação dos seios nasais, geralmente causada por uma infecção viral ou bacteriana.",
                "recomendacao": "Descongestionantes, repouso, e consulta médica se houver piora."
            },
            "Dengue": {
                "sintomas": "Febre, dor muscular, calafrios, fadiga, erupção cutânea.",
                "causas": "Vírus transmitido por mosquitos Aedes aegypti.",
                "recomendacao": "Hidratação adequada e repouso. Consulte um médico se houver sinais de complicações."
            },
            "Hepatite": {
                "sintomas": "Fadiga, náusea, perda de apetite, dor abdominal.",
                "causas": "Inflamação do fígado causada por vírus, álcool ou medicamentos.",
                "recomendacao": "Consulte um médico para diagnóstico e tratamento adequado."
            },
            "Apendicite": {
                "sintomas": "Dor abdominal intensa, náusea, vômito.",
                "causas": "Inflamação do apêndice, geralmente causada por uma infecção.",
                "recomendacao": "Procure atendimento médico imediatamente. A cirurgia pode ser necessária."
            },
            "Zika": {
                "sintomas": "Febre, erupção cutânea, fadiga, dor nas articulações, manchas na pele.",
                "causas": "Vírus transmitido por mosquitos Aedes aegypti.",
                "recomendacao": "Repouso, hidratação e evitar picadas de mosquito. Consulte um médico para confirmação."
            },
            "Chikungunya": {
                "sintomas": "Febre, dor muscular, dor nas articulações, fadiga.",
                "causas": "Vírus transmitido por mosquitos Aedes.",
                "recomendacao": "Repouso, analgésicos para dor e consulta médica em caso de complicações."
            },
            "Malária": {
                "sintomas": "Febre, calafrios, dor de cabeça, fadiga, dor muscular.",
                "causas": "Parasitas transmitidos por mosquitos Anopheles.",
                "recomendacao": "Procure um médico para diagnóstico e tratamento com antimaláricos."
            },
            "Tuberculose": {
                "sintomas": "Tosse, dificuldade para respirar, febre, suor noturno, perda de peso.",
                "causas": "Infecção bacteriana geralmente nos pulmões.",
                "recomendacao": "Tratamento com antibióticos por longo período. Consulte um médico."
            },
            "Pneumonia": {
                "sintomas": "Tosse, dificuldade para respirar, febre, calafrios, dor abdominal.",
                "causas": "Infecção pulmonar, pode ser causada por bactérias ou vírus.",
                "recomendacao": "Antibióticos (para pneumonia bacteriana) e repouso. Consulte um médico imediatamente."
            },
            "Leptospirose": {
                "sintomas": "Febre, dor de cabeça, fadiga, dor abdominal, vômito.",
                "causas": "Bactérias transmitidas por água ou alimentos contaminados com urina de animais.",
                "recomendacao": "Antibióticos são necessários. Consulte um médico para tratamento adequado."
            },
            "Câncer de pulmão": {
                "sintomas": "Tosse, dificuldade para respirar, febre, perda de peso.",
                "causas": "Exposição ao fumo, poluição ou outros agentes cancerígenos.",
                "recomendacao": "Consulta médica para exames e tratamento adequado. Evite o tabagismo."
            },
            "Asma": {
                "sintomas": "Tosse, dificuldade para respirar, sibilo.",
                "causas": "Doença inflamatória crônica das vias aéreas.",
                "recomendacao": "Uso de broncodilatadores e anti-inflamatórios. Consulte um pneumologista."
            },
            "DPOC": {
                "sintomas": "Tosse, dificuldade para respirar, expiração prolongada, sibilo.",
                "causas": "Principalmente causada pelo tabagismo, com destruição dos pulmões.",
                "recomendacao": "Tratamento com medicamentos e reabilitação pulmonar. Evite o fumo."
            },
            "Brucelose": {
                "sintomas": "Febre, dor muscular, sudorese, fadiga, dor abdominal.",
                "causas": "Infecção bacteriana transmitida de animais para humanos.",
                "recomendacao": "Antibióticos são necessários. Consulte um médico para tratamento."
            },
            "Meningite": {
                "sintomas": "Febre, dor de cabeça, rigidez no pescoço, náusea, vômito.",
                "causas": "Infecção das membranas que envolvem o cérebro e a medula espinhal, por vírus ou bactérias.",
                "recomendacao": "Tratamento imediato com antibióticos ou antivirais. Consulte um médico."
            },
            "Síndrome de Guillain-Barré": {
                "sintomas": "Fraqueza muscular, dificuldade para respirar, formigamento.",
                "causas": "Doença autoimune que afeta os nervos periféricos, geralmente após uma infecção viral.",
                "recomendacao": "Tratamento hospitalar, incluindo terapias imunológicas."
            },
            "Mononucleose": {
                "sintomas": "Febre, dor de garganta, linfadenopatia, fadiga.",
                "causas": "Vírus Epstein-Barr.",
                "recomendacao": "Repouso e hidratação. Consulte um médico para tratamento adequado."
            },
            "Doença de Lyme": {
                "sintomas": "Erupção cutânea, febre, dor de cabeça, fadiga, dor muscular.",
                "causas": "Infecção bacteriana transmitida por carrapatos.",
                "recomendacao": "Antibióticos são eficazes no tratamento. Consulte um médico para confirmação."
            },
            "Psoríase": {
                "sintomas": "Erupção cutânea, coceira, lesões escamosas.",
                "causas": "Doença autoimune que afeta a pele.",
                "recomendacao": "Tratamento com cremes e medicamentos imunossupressores. Consulte um dermatologista."
            },
            "Artrite reumatoide": {
                "sintomas": "Dor nas articulações, inchaço articular, rigidez pela manhã.",
                "causas": "Doença autoimune que afeta as articulações.",
                "recomendacao": "Medicamentos imunossupressores e fisioterapia. Consulte um reumatologista."
            },
            "HIV/AIDS": {
                "sintomas": "Febre, fadiga, linfadenopatia, perda de peso.",
                "causas": "Vírus da imunodeficiência humana, transmitido por fluidos corporais.",
                "recomendacao": "Tratamento antirretroviral contínuo. Consulte um médico para acompanhamento."
            },
            "Infecção Urinária": {
            "sintomas": "Dor ao urinar, necessidade frequente de urinar, dor na parte inferior do abdômen.",
            "causas": "Bactérias que entram no trato urinário.",
            "recomendacao": "Aumento da ingestão de líquidos e consulta médica para possível tratamento com antibióticos."
            },
            "Diabetes Tipo 2": {
                "sintomas": "Aumento da sede, aumento da fome, fadiga, perda de peso inexplicada.",
                "causas": "Resistência à insulina, fatores genéticos e estilo de vida.",
                "recomendacao": "Controle da dieta, exercícios regulares e consulta médica para monitoramento da glicose."
            },
            "Fibromialgia": {
                "sintomas": "Dor muscular generalizada, fadiga, distúrbios do sono.",
                "causas": "A causa exata é desconhecida, mas pode estar relacionada a alterações na forma como o cérebro processa a dor.",
                "recomendacao": "Tratamento com medicamentos, terapia física e técnicas de gerenciamento de estresse."
            },
        }



    def configurar_interface(self):
        self.messages_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.messages_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(self.messages_frame, bg="white", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.messages_frame, orient="vertical", command=self.canvas.yview)
        self.messages_container = tk.Frame(self.canvas, bg="white")

        self.messages_container.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.messages_container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.buttons_frame.pack(fill="x", pady=5)

        self.sim_button = tk.Button(self.buttons_frame, text="Sim", command=self.sim, width=10, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), borderwidth=0)
        self.sim_button.pack(side="left", padx=5, pady=5)

        self.nao_button = tk.Button(self.buttons_frame, text="Não", command=self.nao, width=10, bg="#f44336", fg="white", font=("Arial", 12, "bold"), borderwidth=0)
        self.nao_button.pack(side="left", padx=5, pady=5)

        self.recomecar_button = tk.Button(self.buttons_frame, text="Limpar", command=self.recomeçar, width=10, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), borderwidth=0)
        self.recomecar_button.pack(side="right", padx=5, pady=5)

        self.sair_button = tk.Button(self.buttons_frame, text="Sair", command=self.root.quit, width=10, bg="#FF5722", fg="white", font=("Arial", 12, "bold"), borderwidth=0)
        self.sair_button.pack(side="right", padx=5, pady=5)
        
        self.label_hora = tk.Label(self.root, font=("Arial black", 18), bg="#f0f0f0")
        self.label_hora.pack(pady=5)

    def exibir_mensagem_inicial(self):
        self.adicionar_mensagem("Bem-vindo ao Diagnóstico Médico!\nResponda às perguntas para encontrar possíveis diagnósticos.", "sistema")

    def adicionar_mensagem(self, texto, tipo="sistema"):
        cor_fundo = "#DCF8C6" if tipo == "usuario" else "#ECECEC"
        alinhamento = "e" if tipo == "usuario" else "w"
        msg_label = tk.Label(self.messages_container, text="", bg=cor_fundo, fg="black", anchor=alinhamento,
                            padx=10, pady=5, wraplength=300, justify="left" if tipo == "sistema" else "right",
                            font=("Arial", 10))
        msg_label.pack(anchor=alinhamento, pady=2, padx=5)

        def digitar_animacao(index=0):
            if index < len(texto):
                msg_label.config(text=msg_label.cget("text") + texto[index])
                self.root.after(50, lambda: digitar_animacao(index + 1))  # Ajuste a velocidade aqui
            else:
                self.canvas.yview_moveto(1)  # Rola para baixo ao final

        digitar_animacao()
        self.root.update_idletasks()
        self.canvas.yview_moveto(1)  # Rola automaticamente para o fim
 

    def exibir_proxima_pergunta(self):
        if self.diagnostico_encontrado:
            return

        if self.sintoma_prioritarios:
            self.sintoma_chave = self.sintoma_prioritarios.pop(0)
            pergunta = self.sintomas[self.sintoma_chave]
            self.adicionar_mensagem(pergunta, "sistema")
            self.sintomas_ja_perguntados.add(self.sintoma_chave)
        else:
            try:
                while True:
                    self.sintoma_chave, pergunta = next(self.sintoma_atual)
                    if self.sintoma_chave not in self.sintomas_ja_perguntados:  # Verifica se já foi perguntado
                        self.adicionar_mensagem(pergunta, "sistema")
                        self.sintomas_ja_perguntados.add(self.sintoma_chave)  
                        break
            except StopIteration:
                self.sugerir_diagnostico()

    def sim(self):
        self.sintomas_presentes.append(self.sintoma_chave)
        self.adicionar_mensagem("Sim", "usuario")

        sintomas_relacionados = self.sintoma_dependencias.get(self.sintoma_chave, [])
        for sintoma in sintomas_relacionados:
            if sintoma not in self.sintomas_presentes and sintoma not in self.sintoma_prioritarios:
                self.sintoma_prioritarios.append(sintoma)

        self.verificar_diagnostico_automatico()
        self.exibir_proxima_pergunta()

    def nao(self):
        self.adicionar_mensagem("Não", "usuario")
        self.exibir_proxima_pergunta()

    def verificar_diagnostico_automatico(self):
        if self.diagnostico_encontrado:
            return

        possiveis_diagnosticos = self.obter_diagnostico()
        if possiveis_diagnosticos:
            diagnosticos_str = "\n".join(f"- {d}" for d in possiveis_diagnosticos)
            self.adicionar_mensagem(f"Possíveis diagnósticos:\n{diagnosticos_str}\n\nConsulte um médico para confirmação.", "sistema")
            self.diagnostico_encontrado = True
            
            detalhes_diagnosticos = self.definir_detalhes_diagnosticos()

            for diagnostico in possiveis_diagnosticos:
                detalhes = detalhes_diagnosticos.get(diagnostico, {})
                sintomas = detalhes.get("sintomas", "Informações não disponíveis.")
                causas = detalhes.get("causas", "Informações não disponíveis.")
                recomendacao = detalhes.get("recomendacao", "Consulte um médico para mais informações.")

                self.adicionar_mensagem(f"\nDetalhes sobre {diagnostico}:\n"
                                        f"Sintomas típicos: {sintomas}\n"
                                        f"Causas: {causas}\n"
                                        f"Recomendações: {recomendacao}\n", "sistema")

            # Link para buscar mais informações ou consultas médicas
            self.adicionar_mensagem("\nPara mais informações e para confirmação do diagnóstico, consulte um médico. "
                                    "Você pode buscar ajuda médica em um hospital próximo ou em telemedicina.", "sistema")

    def sugerir_diagnostico(self):
        if self.diagnostico_encontrado:
            return

        possiveis_diagnosticos = self.obter_diagnostico()
        if possiveis_diagnosticos:
            diagnosticos_str = "\n".join(f"- {d}" for d in possiveis_diagnosticos)
            self.adicionar_mensagem(f"Diagnóstico Final:\n{diagnosticos_str}\n\nConsulte um médico para confirmação.", "sistema")

            # Acessando os detalhes do diagnóstico corretamente
            detalhes_diagnosticos = self.definir_detalhes_diagnosticos()

            for diagnostico in possiveis_diagnosticos:
                detalhes = detalhes_diagnosticos.get(diagnostico, {})
                sintomas = detalhes.get("sintomas", "Informações não disponíveis.")
                causas = detalhes.get("causas", "Informações não disponíveis.")
                recomendacao = detalhes.get("recomendacao", "Consulte um médico para mais informações.")

                self.adicionar_mensagem(f"\nDetalhes sobre {diagnostico}:\n"
                                        f"Sintomas típicos: {sintomas}\n"
                                        f"Causas: {causas}\n"
                                        f"Recomendações: {recomendacao}\n", "sistema")

            # Link para buscar mais informações ou consultas médicas
            self.adicionar_mensagem("\nPara mais informações e para confirmação do diagnóstico, consulte um médico. "
                                    "Você pode buscar ajuda médica em um hospital próximo ou em telemedicina.", "sistema")

        else:
            self.adicionar_mensagem("Nenhum diagnóstico possível encontrado com base nos sintomas.\n\nConsulte um médico para confirmação.", "sistema")
        
        self.diagnostico_encontrado = True


    def obter_diagnostico(self):
        pontuacao_diagnosticos = {}
        for diagnostico, sintomas in self.diagnosticos.items():
            pontuacao = sum(peso for sintoma, peso in sintomas.items() if sintoma in self.sintomas_presentes)
            if pontuacao >= 6:  
                pontuacao_diagnosticos[diagnostico] = pontuacao
        return sorted(pontuacao_diagnosticos, key=pontuacao_diagnosticos.get, reverse=True)

    def recomeçar(self):
        self.sintomas_presentes = []
        self.sintoma_atual = iter(self.sintomas.items())
        self.diagnostico_encontrado = False  

        for widget in self.messages_container.winfo_children():
            widget.destroy()

        self.exibir_mensagem_inicial()
        self.exibir_proxima_pergunta()
        
    def atualizar_hora(self):
        agora = datetime.now()
        hora_atual = agora.strftime("%H:%M:%S")
        self.label_hora.config(text=hora_atual)
        self.label_hora.after(1000, self.atualizar_hora)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  
    root.configure(bg="#f0f0f0")
    app = DiagnosticoMedico(root)
    root.mainloop() 