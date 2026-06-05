from rich import print
from rich.panel import Panel
import os


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