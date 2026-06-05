from classes.calculadora import Calculadora
from classes.pessoa import Pessoa

from funcoes import *

def main():

    while True:

        limpar_tela()
        mostrar_menu()

        opcao = input('Digite um número: ')

        if opcao == '1':

            limpar_tela()

            print(
                Panel(
                    '[yellow]Informe os dados abaixo[/]',
                    title='DADOS INICIAIS'
                )
            )

            orcamento = ler_float('Qual o total do orçamento? R$ ')
            gastos = ler_float('Qual o total dos gastos? R$ ')

            c1 = Calculadora(gastos, orcamento)

            pessoas = ler_int('\nQuantas pessoas vão dividir? ')

            for i in range(pessoas):

                while True:

                    print(f'\n[cyan]Pessoa {i + 1}[/]')

                    nome = input('Nome: ')
                    salario = ler_float('Salário: R$ ')

                    print(f'\nNome: {nome}')
                    print(f'Salário: {moeda(salario)}')

                    duvida = str(input('\nAs informações anteriores estão corretas?  (sim/não): ').lower())

                    if duvida == 'sim':

                        pessoa = Pessoa(nome, salario)
                        c1.adicionar_pessoa(pessoa)

                        break

                    elif duvida == 'não':

                        print(f'\nDigite novamente as informações... ')

                    else:
                        print('\nResposta inválida!!')


            resultado = c1.dividir_gastos()

            limpar_tela()

            mostrar_resumo(orcamento, gastos)

            mostrar_resultado(resultado)

            pausar()


        elif opcao == '2':

            limpar_tela()

            print(
                Panel(
                    '[yellow]Soma (1) - Subtração (2) - Divisão (3) - Multiplicação (4)[/]',
                    title='Qual conta deseja realizar? indique com um número'
                )
            )

            while True:
                try:
                    conta = int(input())
                except ValueError:
                    print('Digite um número válido.')
                    continue

                c1 = Calculadora()

                operacoes = {
                    1: {
                        'função': c1.somar_gastos,
                        'simbolos': '+',
                        'nome': 'Soma',
                        'primeiro': 'Valor 1',
                        'outros': 'Valor'
                    },

                    2: {
                        'função': c1.subtrair_gastos,
                        'simbolos': '-',
                        'nome': 'Subtração',
                        'primeiro': 'Número inicial',
                        'outros': 'Subtrair'
                    },

                    3: {
                        'função': c1.divisao,
                        'simbolos': '/',
                        'nome': 'Divisão',
                        'primeiro': 'Número inicial',
                        'outros': 'Dividir por'
                    },

                    4: {
                        'função': c1.multiplicar,
                        'simbolos': 'X',
                        'nome': 'Multiplicação',
                        'primeiro': 'Número inicial',
                        'outros': 'Multiplicar por'
                    }
                }

                if conta in operacoes:
                    validacao(operacoes[conta])
                    break
                else:
                    print('Número inválido.')

        elif opcao == '3':

            print('\n[green]Até logo![/]')
            break

        else:

            print('[red]Opção inválida![/]')
            pausar()


if __name__ == '__main__':
    main()