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
            '[blue]1 - Calcular[/]    [blue]2 - Calcular gastos[/]    [red]3 - Sair',
            title='[green]CONTROLE DE GASTOS[/]',
            subtitle='Escolha uma opção'
        )
    )


def ler_float(mensagem):
    while True:
        try:
            valor = input(mensagem).replace(',', '.')
            return float(valor)
        except ValueError:
            print('[red]Digite um número válido![/]')


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('[red]Digite um número inteiro válido![/]')

def moeda(valor, cor="green"):
    return f'[{cor}]R$ {valor:.2f}[/]'.replace('.', ',')


def mostrar_resumo(orcamento, gastos):
    print(
        Panel(
            f'[yellow]Orçamento:[/] {moeda(orcamento, "green")}\n'
            f'[yellow]Gastos:[/] {moeda(gastos, "red")}\n'
            f'[yellow]Sobra:[/] {moeda(orcamento - gastos, "cyan")}',
            title='[bold green]RESUMO FINANCEIRO[/]',
            border_style='blue'
        )
    )

def mostrar_resultado(resultado):
    texto = ''

    for nome, valor in resultado.items():
        texto += (
            f'[blue]{nome}[/] deve pagar '
            f'{moeda(valor, "green")}\n'
        )

    print(
        Panel(
            texto,
            title='[bold yellow]DIVISÃO DOS GASTOS[/]',
            border_style='red'
        )
    )


def calculos():
    n1 = float(input('Número 1: ').replace(',', '.'))
    n2 = float(input('Número 2: ').replace(',', '.'))

    duvida = input(
        'Digitou o número correto? (sim/não): '
    ).lower()

    return n1, n2, duvida

def validacao(operacao):

    while True:

        n1, n2, duvida = calculos()

        if duvida == 'sim':


            resultado = operacao(n1, n2)

            print(
                Panel(
                    f'Resultado: {moeda(resultado, "green")}',
                    title='[bold blue]RESULTADO[/]',
                    border_style='green'
                )
            )

            pausar()
            break

        elif duvida == 'não':
            print('[yellow]Informe os dados novamente...[/]')

        else:
            print('[red]Resposta inválida! Digite sim ou não.[/]')



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
                    1: c1.somar_gastos,
                    2: c1.subtrair_gastos,
                    3: c1.divisao,
                    4: c1.multiplicar
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