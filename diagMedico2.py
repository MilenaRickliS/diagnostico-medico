import tkinter as tk

class DiagnosticoMedico:
    def __init__(self, root):
        # Dicionário de sintomas e perguntas
        self.sintomas = {
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

        # Dicionário de diagnósticos baseados nos sintomas
        self.diagnosticos = {
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
            "Pneumonia": ["tosse", "dificuldade_respirar", "febre", "calafrios", "dor_peito"],
            "Leptospirose": ["febre", "dor_cabeca", "fadiga", "dor_abdominal", "vômito"],
            "Câncer de pulmão": ["tosse", "dificuldade_respirar", "febre", "perda_de_peso", "dor_torácica"],
            "Asma": ["tosse", "dificuldade_respirar", "chiado_no_peito"],
            "Doença pulmonar obstrutiva crônica (DPOC)": ["tosse", "dificuldade_respirar", "expiração_prolongada", "sibilo"],
            "Brucelose": ["febre", "dor_muscular", "suores", "fadiga", "dor_abdominal"],
            "Meningite": ["febre", "dor_cabeca", "rigidez_nucal", "nausea", "vomito"],
            "Síndrome de Guillain-Barré": ["fraqueza_muscular", "dificuldade_respirar", "formigamento"],
            "Mononucleose": ["febre", "dor_garganta", "linfadenopatia", "fadiga"],
            "Doença de Lyme": ["erupcao_cutanea", "febre", "dor_cabeca", "fadiga", "dor_muscular"],
            "Psoríase": ["erupcao_cutanea", "coceira", "lesões_escamosas"],
            "Artrite reumatoide": ["dor_articulacoes", "inchaço_articular", "rigidez_morning"],
            "HIV/AIDS": ["febre", "fadiga", "linfadenopatia", "perda_de_peso", "suores_noturnos"],
        }

        self.sintomas_presentes = []
        self.sintoma_atual = iter(self.sintomas.items())
        self.root = root
        self.root.title("Diagnóstico Médico - Estilo WhatsApp")
        self.diagnostico_encontrado = False  # Variável para verificar se já encontrou um diagnóstico

        # Configuração da área de mensagens
        self.messages_frame = tk.Frame(root, bg="#f0f0f0")
        self.messages_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(self.messages_frame, bg="white", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.messages_frame, orient="vertical", command=self.canvas.yview)
        self.messages_container = tk.Frame(self.canvas, bg="white")

        self.messages_container.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.messages_container, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Botões de resposta
        self.buttons_frame = tk.Frame(root, bg="#f0f0f0")
        self.buttons_frame.pack(fill="x", pady=5)

        # Configuração dos botões
        self.sim_button = tk.Button(self.buttons_frame, text="Sim", command=self.sim, width=10, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), borderwidth=0)
        self.sim_button.pack(side="left", padx=5, pady=5)

        self.nao_button = tk.Button(self.buttons_frame, text="Não", command=self.nao, width=10, bg="#f44336", fg="white", font=("Arial", 12, "bold"), borderwidth=0)
        self.nao_button.pack(side="right", padx=5, pady=5)

        # Botão de Recomeçar
        self.recomecar_button = tk.Button(self.buttons_frame, text="Limpar", command=self.recomeçar, width=10, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), borderwidth=0)
        self.recomecar_button.pack(side="right", padx=5, pady=5)

        # Exibir a primeira pergunta
        self.exibir_proxima_pergunta()

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
        # Se já encontrou um diagnóstico, não exibe mais perguntas
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
            self.diagnostico_encontrado = True  # Marca que o diagnóstico foi encontrado e interrompe o fluxo de perguntas

    def sugerir_diagnostico(self):
        if self.diagnostico_encontrado:
            return

        possiveis_diagnosticos = self.obter_diagnostico()
        if possiveis_diagnosticos:
            diagnosticos_str = "\n".join(f"- {d}" for d in possiveis_diagnosticos)
            self.adicionar_mensagem(f"Diagnóstico Final:\n{diagnosticos_str}\n\nConsulte um médico para confirmação.", "sistema")
            self.diagnostico_encontrado = True
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
        # Zera as variáveis
        self.sintomas_presentes = []
        self.sintoma_atual = iter(self.sintomas.items())
        self.diagnostico_encontrado = False

        # Limpa a interface de mensagens
        for widget in self.messages_container.winfo_children():
            widget.destroy()

        # Exibe a primeira pergunta novamente
        self.exibir_proxima_pergunta()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x600")  
    root.configure(bg="#f0f0f0")
    app = DiagnosticoMedico(root)
    root.mainloop()
