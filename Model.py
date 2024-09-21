
class Model:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def trocar(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A: {valorA} \nValor B: {valorB}'

    def tabuada(self, num):
        resultado = "" #Variavel String
        for i in range(0, 11, 1):
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def mediaTres(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3)/3

    def exercicioUm(self, num):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'{i}\n'
        return resultado

    def exercicioDois(self, num):
        resultado = ""
        for i in range(0, 20, 2):
            resultado += f'{i}\n'
        return resultado

    def exercicioTres(self):
        soma = 0
        for i in range(101):
            soma += i
        return soma

    def exercicioQuatro(self):
        resultado = ""
        for i in range(0, 51, 5):
            resultado += f'{i}\n'
        return resultado

    def exercicioCinco(self, num):
        if num %2 == 0:
            return f'O número {num} é par'
        else:
            return f'O número {num} é impar'

    def exercicioSeis(self, num):
        if num > 0:
            return f'O número é positivo'
        elif num < 0:
             return f'O número é negativo'
        else:
            return f'O número é zero'
    def exercicioSete(self, num):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def exercicioOito(self, num):
        resultado = ""
        for i in range(1, num+1, 1):
            resultado += f'{i}\n'
        return resultado

    def exercicioNove(self, num):
        soma = 0
        for i in range(1, num+1, 1):
            soma += i
        return soma

    def exercicioDez(self):
        resultado = "2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                resultado += f'\n{i}'
        return resultado