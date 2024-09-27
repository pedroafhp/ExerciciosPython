from Model import Model

class Control:
    def __init__(self):
        self.modelo = Model() #Instanciando a Classe Model
        self.opcao = 0

    def mostrarMenu(self):
        print ('Escolha uma das opções abaixo: '     +
                '\n1.   Sair'                        +
                '\n2.   Trocar'                      +
                '\n3.   Tabuada'                     +
                '\n4.   Média de Três Notas'         +
                '\n5.   Exercício 01'                +
                '\n6.   Exercicio 02'                +
                '\n7.   Exercicio 03'                +
                '\n8.   Exercicio 04'                +
                '\n9.   Exercicio 05'                +
                '\n10.  Exercicio 06'                +
                '\n11.  Exercicio 07'                +
                '\n12.  Exercicio 08'                +
                '\n13.  Exercicio 09'                +
                '\n14.  Exercicio 10'                +
                '\n15.  Exercicio 11'                +
                '\n16.  Exercicio 12'                +
                '\n17.  Exercicio 13'                +
                '\n18.  Exercicio 14'                +
                '\n19.  Exercicio 15'                +
                '\n20.  Exercicio 16'                +
                '\n21.  Exercicio 17'                +
                '\n22.  Exercicio 18'                +
                '\n23.  Exercicio 19'                +
                '\n24.  Exercicio 20'                )

    def operacoes(self):
        while(self.opcao != 1):
            self.mostrarMenu()
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 1:
                print('Obrigado')

            elif self.opcao == 2:
                valorA = int(input('Informe um valor para A'))
                valorB = int(input('Informe um valor para B'))
                print(self.modelo.trocar(valorA,valorB))

            elif self.opcao == 3:
                num = int(input('Informe um número: '))
                print(self.modelo.tabuada(num))

            elif self.opcao == 4:
                nota1 = float(input('Primeira Nota: '))
                while(nota1 < 0 or nota1 > 10):
                    print('ERRO! Informe uma nota entre 0 e 10')
                    nota1 = float(input('Primeira Nota: '))

                nota2 = float(input('Segunda Nota: '))
                while (nota2 < 0 or nota2 > 10):
                    print('ERRO! Informe uma nota entre 0 e 10')
                    nota2 = float(input('Segunda Nota: '))

                nota3 = float(input('Terceira Nota: '))
                while (nota3 < 0 or nota3 > 10):
                    print('ERRO! Informe uma nota entre 0 e 10')
                    nota3 = float(input('Terceira Nota: '))

                print(self.modelo.mediaTres(nota1,nota2,nota3))

            elif self.opcao == 5:
                num = int(input("Informe um número"))
                print(self.modelo.exercicioUm(num))

            elif self.opcao == 6:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioDois(num))

            elif self.opcao == 7:
                print(f'A soma dos números entre 1 e 100 é: {self.modelo.exercicioTres()}')

            elif self.opcao == 8:
                print(f'Os multiplos de 5, de 1 a 50 são: \n{self.modelo.exercicioQuatro()}')

            elif self.opcao == 9:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioCinco(num))

            elif self.opcao == 10:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioSeis(num))

            elif self.opcao == 11:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioSete(num))

            elif self.opcao == 12:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioOito(num))

            elif self.opcao == 13:
                num = int(input("Informe um número: "))
                print(f'A soma dos números é: {self.modelo.exercicioNove(num)}')

            elif self.opcao == 14:
                print(f'Os números primos são: \n{self.modelo.exercicioDez()}')

            elif self.opcao == 15:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioOnze(num))

            elif self.opcao == 16:
                resultado = ""
                num = int(input("Informe um número: "))
                print(f'O fatorial de {num} é:{resultado} {self.modelo.exercicioDoze(num)}')

            elif self.opcao == 17:
                print(self.modelo.exercicioTreze())

            elif self.opcao == 18:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioQuatorze(num))

            elif self.opcao == 19:
                num = int(input("Informe um número: "))
                print(f'A soma de {num} é: {self.modelo.exercicioQuinze(num)}')

            elif self.opcao == 20:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioDezesseis(num))

            elif self.opcao == 21:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioDezessete(num))

            elif self.opcao == 22:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioDezoito(num))

            elif self.opcao == 23:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioDezenove(num))

            elif self.opcao == 24:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioVinte(num))
            else:
                print('Opção escolida não é válida!')