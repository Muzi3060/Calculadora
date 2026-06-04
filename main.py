from rich import print
from rich.panel import Panel
import os

from classes.calculadora import Calculadora
from classes.pessoa import Pessoa


# ADICIONAR UM LOOP NA HORA DE PEDIR NUMERO 1 E 2, PARA ENTÃO PERMITIR O USUARIO FAZER UMA CONTA COM VARIOS NUMEROS AO INVÉS DE SÓ 2.
# QUANDO O USUARIO TERMINAR E NÃO QUERER MAIS ADICIONAR NUMEROS A CONTA, ELE SÓ DIGITA "TERMINAR" E PRONTO, VAI EXIBIR O TOTAL DE TODOS OS NÚMEROS QUE ELE PASSOU!


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
            print(
                '[red]Digite um número válido![/]\n' 
                '[yellow]Exemplo: 5000,25[/]'
            )


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('[red]Digite um número inteiro válido![/]')

def moeda(valor, cor="green"):
    return f'[{cor}]R$ {valor:.2f}[/]'.replace('.', ',')

def mostrar_calculo(gastos, simbolo, resultado):
    expressao = f' {simbolo} '.join(
        str(valor).replace('.', ',')
        for valor in gastos
    )

    print(
        Panel(
            f'[yellow]Expressão:[/]\n'
            f'[cyan]{expressao}[/]\n\n'
            f'[yellow]Quantidade de valores:[/] [white]{len(gastos)}[/]\n'
            f'[bold green]Resultado:[/] {moeda(resultado)}',
            title='[bold blue]RESULTADO DA OPERAÇÃO[/]',
            border_style='blue'
        )
    )

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


def calculos(config):
    gastos = []
    count = 1

    while True:

        if count == 1:
            gasto = ler_float(f'{config["primeiro"]}: ')
        else:
            gasto = ler_float(f'{config["outros"]}: ')

        duvida = input(
            '\nDigitou o Gasto correto? (sim/não): '
        ).lower()

        if duvida == 'sim':
            gastos.append(gasto)

            print(
                Panel(
                    f'[green]Valor adicionado:[/] {moeda(gasto)}\n'
                    f'[cyan]Quantidade:[/] {len(gastos)}',
                    title='[bold green]SUCESSO[/]',
                    border_style='green'
                )
            )

            while True:
                resposta = str(input('\nAdicionar outro? (sim/não) '))

                if resposta == 'sim':
                    print('\n[blue]Ok, continuando calculos...[/]')
                    break

                elif resposta == 'não':
                    texto = ''

                    for i, valor in enumerate(gastos, start=1):
                        texto += (
                            f'[cyan]Valor {i}:[/] '
                            f'{moeda(valor)}\n'
                        )

                        texto += (
                            f'\n[bold yellow]Total informado:[/] '
                            f'{moeda(sum(gastos))}'
                        )

                    print(
                        Panel(
                            texto,
                            title='[yellow]VALORES INFORMADOS[/]',
                            border_style='blue'
                        )
                    )

                    return gastos

                else:
                    print('\n[red]Resposta inválida! Digite sim ou não.[/]')

        elif duvida == 'não':
            print('Digite novamente!')

        count += 1

def validacao(config):

    print(
        Panel(
            f'[cyan]{config["nome"]}[/]',
            title='[bold yellow]OPERAÇÃO ESCOLHIDA[/]',
            border_style='green'
        )
    )

    print(
        Panel(
            f'[bold cyan]{config["nome"]}[/]\n\n'
            f'[yellow]Primeiro valor:[/] {config["primeiro"]}\n'
            f'[yellow]Demais valores:[/] {config["outros"]}',
            title='[green]COMO FUNCIONA[/]',
            border_style='cyan'
        )
    )
    
    while True:

        gastos = calculos(config)

        resultado = config['função'](gastos)

        mostrar_calculo(
            gastos,
            config['simbolos'],
            resultado
        )

        pausar()
        break



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