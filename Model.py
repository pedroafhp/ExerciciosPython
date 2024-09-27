
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
        if num % 2 == 0:
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

    def exercicioOnze(self,num):
        if num == 2 or num == 3 or num == 5:
            return f'O {num} é primo'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return f'O {num} é primo'
        else:
            return f'O {num} não é primo'

    def exercicioDoze(self, num):
        resultado = ""
        if num < 0:
            return "Favor digitar um número maior que zero."
        elif num == 0 or num == 1:
            return 1
        else:
            resultado = 1
            for i in range(2, num + 1, 1):
                    resultado *= i
        return resultado
    def exercicioTreze(self):
        fib1 = 0
        fib2 = 1
        fib3 = 0
        resultado = f'0\n1\n'
        for fib3 in range(1, 9, 1):
            fib3 = fib1 + fib2
            resultado = f'{fib3}'
            fib1 = fib2
            fib2 = fib3
        return resultado
    def exercicioQuatorze(self, num):
        resultado = ""
        fib1 = 0
        fib2 = 1
        fib3 = 0
        resultado = f'0\n1\n'
        for fib3 in range (1, 100, 1):
            fib3 = fib1 + fib2
            resultado = f'{fib3}'
            fib1 = fib2
            fib2 = fib3
            if num == fib3:
                return f'{num} está dentro da sequência de Fibonacci'
        return f'{num} não está dentro da sequência de Fibonnaci'
    def exercicioQuinze(self, num):
        resto = 0
        num % 10
        while num / 10 != 0:
            resto += num % 10
            num = int (num / 10)
        return resto
    def exercicioDezesseis(self, num):
        impar = ""
        par = ""
        for i in range(1, num, 1):
            if i % 2 == 0:
                par += f'\n {i}'
            else:
                impar += f'\n {i}'
        return f'Os valores pares são: {par} \n Os valores impares são {impar}'
    def exercicioDezessete(self, num):
        primos = ""
        notPrimos = ""
        for i in range(1, num, 1):
            if i == 2 or i == 3 or i == 5:
                primos += f'\n {i}'
            elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primos += f'\n {i}'
            else:
                notPrimos += f'\n {i}'
        return f'Os números primos são: {primos} \n Os numeros não primos são: {notPrimos}'
    def exercicioDezoito(self, num):
            if num % 2 == 0:
                return f'O resultado da sequencia de Collatz é: {num / 2}'
            else:
                return f'O resultado da sequencia de Collatz é: {3 * num + 1}'
    def exercicioDezenove(self, num):
        soma = 0
        for i in range(1, num + 1, 1):
            soma += i
        return f'A soma dos números pares e impares de 1 até {num} é: {soma}'
    def exercicioVinte(self, num):
        somaDiv = 0
        for i in range(1, num, 1):
            if num % i == 0:
                somaDiv += i

        if num == somaDiv:
           return f'{num} é um número perfeito'
        else:
            return f'{num} não é um número perfeito'

