class Calculadora():
    def __init__(self, gasto= 0, orcamento= 0):
        self.pessoas = []

        self.gasto = gasto
        self.orcamento = orcamento

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def somar_gastos(self, n1:float, n2:float):
        return n1 + n2

    def subtrair_gastos(self, n1:float, n2:float):
        return n1 - n2

    def divisao(self, n1:float, n2:float):
        return n1 / n2

    def multiplicar(self, n1:float, n2:float):
        return n1 * n2


    def total_salarios(self):
        total = 0

        for p in self.pessoas:
            total += p.salario

        return total

    def calcular_percentual(self):
        porcentual = []
        total = self.total_salarios()

        for p in self.pessoas:
            percent = p.salario / total
            porcentual.append(percent)

        return porcentual


    def dividir_gastos(self):
        percentuais = self.calcular_percentual()
        resultados = {}

        for i in range(len(self.pessoas)):
            pessoa = self.pessoas[i]
            percentual = percentuais[i]

            valor = self.gasto * percentual

            resultados[pessoa.nome] = valor

        return resultados