import tkinter as tk
import time

class DiagnosticoMedico:
    def __init__(self, root):
        self.sintomas = self.definir_sintomas()
        self.diagnosticos = self.definir_diagnosticos()
        
        self.sintomas_presentes = []
        self.sintoma_atual = iter(self.sintomas.items())
        self.root = root
        self.root.title("IA - Diagnóstico Médico")
        self.diagnostico_encontrado = False  

        self.configurar_interface()
        self.exibir_mensagem_inicial()
        self.exibir_proxima_pergunta()

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
        }

    def definir_diagnosticos(self):
        return {
            "Gripe": ["febre", "tosse", "dor_cabeca", "fadiga", "calafrios"],
            "COVID-19": ["febre", "tosse", "dificuldade_respirar", "fadiga", "perda_de_paladar"],
            "Resfriado": ["tosse", "dor_garganta", "fadiga", "congestao_nasal"],
            "Gastrite": ["nausea", "dor_cabeca", "dor_abdominal"],
            "Alergia": ["erupcao_cutanea", "tosse", "sudorese", "congestao_nasal"],
            "Infecção Alimentar": ["nausea", "vomito", "diarreia", "dor_abdominal"],
            "Sinusite": ["dor_cabeca", "dor_garganta", "tosse", "fadiga", "congestao_nasal"],
            "Dengue": ["febre", "dor_muscular", "calafrios", "fadiga", "erupcao_cutanea"],
            "Hepatite": ["fadiga", "nausea", "perda_de_apetite", "dor_abdominal"],
            "Apendicite": ["dor_abdominal", "nausea", "vomito"],
            "Zika": ["febre", "erupcao_cutanea", "fadiga", "dor_articulacoes", "manchas_na_pele"],
            "Chikungunya": ["febre", "dor_muscular", "dor_articulacoes", "fadiga"],
            "Malária": ["febre", "calafrios", "dor_cabeca", "fadiga", "dor_muscular"],
            "Tuberculose": ["tosse", "dificuldade_respirar", "febre", "suor_noturno", "perda_de_peso"],
            "Pneumonia": ["tosse", "dificuldade_respirar", "febre", "calafrios", "dor_abdominal"],
            "Leptospirose": ["febre", "dor_cabeca", "fadiga", "dor_abdominal", "vomito"],
            "Câncer de pulmão": ["tosse", "dificuldade_respirar", "febre", "perda_de_peso"],
            "Asma": ["tosse", "dificuldade_respirar", "sibilo"],
            "DPOC": ["tosse", "dificuldade_respirar", "expiracao_prolongada", "sibilo"],
            "Brucelose": ["febre", "dor_muscular", "suor", "fadiga", "dor_abdominal"],
            "Meningite": ["febre", "dor_cabeca", "rigidez_nucal", "nausea", "vomito"],
            "Síndrome de Guillain-Barré": ["fraqueza_muscular", "dificuldade_respirar", "formigamento"],
            "Mononucleose": ["febre", "dor_garganta", "linfadenopatia", "fadiga"],
            "Doença de Lyme": ["erupcao_cutanea", "febre", "dor_cabeca", "fadiga", "dor_muscular"],
            "Psoríase": ["erupcao_cutanea", "coceira", "lesoes_escamosas"],
            "Artrite reumatoide": ["dor_articulacoes", "inchaço_articular", "rigidez_morning"],
            "HIV/AIDS": ["febre", "fadiga", "linfadenopatia", "perda_de_peso"],
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

    def exibir_mensagem_inicial(self):
        self.adicionar_mensagem("Bem-vindo ao Diagnóstico Médico!\nResponda às perguntas para encontrar possíveis diagnósticos.", "sistema")

    def adicionar_mensagem(self, texto, tipo="sistema"):
        cor_fundo = "#DCF8C6" if tipo == "usuario" else "#ECECEC"
        alinhamento = "e" if tipo == "usuario" else "w"
        msg_label = tk.Label(self.messages_container, text=texto, bg=cor_fundo, fg="black", anchor=alinhamento,
                             padx=10, pady=5, wraplength=300, justify="left" if tipo == "sistema" else "right",
                             font=("Arial", 10))
        msg_label.pack(anchor=alinhamento, pady=2, padx=5)
        self.root.update_idletasks()
        self.canvas.yview_moveto(1)

    def exibir_proxima_pergunta(self):
        if self.diagnostico_encontrado:
            return

        try:
            self.sintoma_chave, pergunta = next(self.sintoma_atual)
            self.adicionar_mensagem(pergunta, "sistema")
        except StopIteration:
            self.sugerir_diagnostico()

    def sim(self):
        self.sintomas_presentes.append(self.sintoma_chave)
        self.adicionar_mensagem("Sim", "usuario")
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
        else:
            self.adicionar_mensagem("Nenhum diagnóstico possível encontrado com base nos sintomas.\n\nConsulte um médico para confirmação.", "sistema")
        self.diagnostico_encontrado = True

    def obter_diagnostico(self):
        possiveis_diagnosticos = []
        for diagnostico, sintomas in self.diagnosticos.items():
            if all(sintoma in self.sintomas_presentes for sintoma in sintomas):
                possiveis_diagnosticos.append(diagnostico)
        return possiveis_diagnosticos

    def recomeçar(self):
        self.sintomas_presentes = []
        self.sintoma_atual = iter(self.sintomas.items())
        self.diagnostico_encontrado = False  

        for widget in self.messages_container.winfo_children():
            widget.destroy()

        self.exibir_mensagem_inicial()
        self.exibir_proxima_pergunta()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x600")  
    root.configure(bg="#f0f0f0")
    app = DiagnosticoMedico(root)
    root.mainloop()