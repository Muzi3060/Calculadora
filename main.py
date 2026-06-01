from rich import print
from rich.panel import Panel
import os

from classes.calculadora import Calculadora
from classes.pessoa import Pessoa


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input('\nPressione ENTER para continuar...')


def mostrar_menu():
    print(
        Panel(
            '[blue]1 - Calcular[/]    [red]2 - Sair[/]',
            title='[green]CONTROLE DE GASTOS[/]',
            subtitle='Escolha uma opção'
        )
    )


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('[red]Digite um número válido![/]')


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('[red]Digite um número inteiro válido![/]')


def mostrar_resumo(orcamento, gastos):
    print(
        Panel(
            f'Orçamento: [green]R${orcamento:.2f}[/]\n'
            f'Gastos: [red]R${gastos:.2f}[/]\n'
            f'Sobra: [cyan]R${orcamento - gastos:.2f}[/]',
            title='[yellow]RESUMO[/]'
        )
    )


def mostrar_resultado(resultado):
    texto = ''

    for nome, valor in resultado.items():
        texto += f'{nome} deve pagar [green]R${valor:.2f}[/]\n'

    print(
        Panel(
            texto,
            title='[blue]DIVISÃO DOS GASTOS[/]'
        )
    )


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

                print(f'\n[cyan]Pessoa {i + 1}[/]')

                nome = input('Nome: ')
                salario = ler_float('Salário: R$ ')

                pessoa = Pessoa(nome, salario)

                c1.adicionar_pessoa(pessoa)

            resultado = c1.dividir_gastos()

            limpar_tela()

            mostrar_resumo(orcamento, gastos)

            mostrar_resultado(resultado)

            pausar()

        elif opcao == '2':

            print('\n[green]Até logo![/]')
            break

        else:

            print('[red]Opção inválida![/]')
            pausar()


if __name__ == '__main__':
    main()