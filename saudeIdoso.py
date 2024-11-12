class Diagnostico:
    def __init__(self):
        self.pontos = 0


    def pergunta_frequencia(self, pergunta, pontos):
        
        resposta = input(pergunta + " (Sempre, Quase sempre, Às vezes, Raramente, Nunca): ")
        if resposta.lower() == "sempre":
            self.pontos += pontos
        elif resposta.lower() == "quase sempre":
            self.pontos += pontos - 1
        elif resposta.lower() == "as vezes":
            self.pontos += pontos - 2
        elif resposta.lower() == "raramente":
            self.pontos += pontos - 3
        elif resposta.lower() == "nunca":
            self.pontos += 0

    def pergunta1ponto(self, pergunta, pontos):
        resposta = input(pergunta + " (Sim ou não): ")
        if resposta.lower() == "sim":
            self.pontos += pontos
        elif resposta.lower() == "não":
            self.pontos += pontos - 1

    def pergunta2ponto(self, pergunta, pontos):
        resposta = input(pergunta + " (Sim ou não): ")
        if resposta.lower() == "sim":
            self.pontos += pontos
        elif resposta.lower() == "não":
            self.pontos += pontos - 2

    def pergunta3ponto(self, pergunta, pontos):
        resposta = input(pergunta + " (Sim ou não): ")
        if resposta.lower() == "sim":
            self.pontos += pontos
        elif resposta.lower() == "não":
            self.pontos += pontos - 3

    def pergunta4ponto(self, pergunta, pontos):
        resposta = input(pergunta + " (Sim ou não): ")
        if resposta.lower() == "Sim":
            self.pontos += pontos
        elif resposta.lower() == "Não":
            self.pontos += pontos - 4

    def resultado(self):
        if self.pontos > 15:
            return "Alto risco de vulnerabilidade, ou fragilidade instalada, que exigem avaliação ampliada"
        elif self.pontos > 6:
            return "Risco aumentado de vulnerabilidade clínico-funcional, necessidade de uma avaliação mais ampla e atenção para identificação e tratamento de doenças crônicas"
        elif self.pontos >= 1:
            return "Baixa vulnerabilidade clínico-funcional, e não necessita de avaliação e acompanhamento especializados"
        elif self.pontos == 0:
            return "Nenhuma vulnerabilidade detectada"
        
diagnostico = Diagnostico()
diagnostico.pergunta_frequencia("Você tem febre?", 4)
diagnostico.pergunta_frequencia("Você tem dor de cabeça?", 4)
diagnostico.pergunta_frequencia("Você tem dor muscular?", 4)
diagnostico.pergunta_frequencia("Você tem falta de ar?", 4)

print("Perguntas de Cognição")
diagnostico.pergunta1ponto("Algum familiar ou amigo falou que você está ficando esquecido?", 1)
diagnostico.pergunta1ponto("Este esquecimento está piorando nos últimos meses?", 1)
diagnostico.pergunta2ponto("Este esquecimento está impedindo a realização de alguma atividade do cotidiano?", 2)

print("Perguntas de Humor")
diagnostico.pergunta2ponto("No último mês, você ficou com desanimo, tristeza ou desesperança?", 2)
diagnostico.pergunta2ponto("No último mês, você perdeu o interesse ou prazer em atividades anteriormente prazerosas?", 2)

print("Perguntas de Mobilidade")
diagnostico.pergunta2ponto("Você é incapaz de elevar os braços acima do nível do ombro?", 2)
diagnostico.pergunta2ponto("Você tem dificuldade para caminhar capaz de impedir a realização de alguma atividade do cotidiano?", 2)
diagnostico.pergunta2ponto("Você teve duas ou mais quedas no último ano?", 2)
diagnostico.pergunta2ponto("Você perde urina ou fezes, sem querer, em algum momento?", 2)

print("Perguntas de Comunicação")
diagnostico.pergunta2ponto("Você tem problemas de visão capazes de impedir a realização de alguma atividade do cotidiano?", 2)
diagnostico.pergunta2ponto("Você tem problemas de audição capazes de impedir a realização de alguma atividade do cotidiano?", 2)

print(diagnostico.resultado())