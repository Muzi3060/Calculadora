from rich import print, inspect
from rich.panel import Panel
import os
from classes.calculadora import Calculadora
from classes.pessoa import Pessoa



# IDEIAS NOVAS -- AO INVÉS DE SÓ TER OPÇÃO DE CALCULAR E SAIR, ADICIONAR UMA 3 OPÇÃO PARA CALCULAR AS DIVIDAS UMA POR UMA E DIZER QUAL O TOTAL DE DIVIDAS
# IDEIAS NOVAS -- ADICIONAR UMA OPÇÃO PARA DIZER QUANTO DO TOTAL DA DIVIDA SERA PARCELADO, POR EXEMPLO, SE A DIVIDA É 6000 E A PESSOA SÓ VAI DIVIDIR EM 3 2000, TER UMA OPÇÃO PARA DIVIDIR SÓ OS 2000 E O RESTANTE DA DIVIDA SER PAGA POR 1 PESSOA, OU PELA QUANTIDADE X DE PESSOAS QUE VÃO PARCELAR O RESTO

def main():
    print(
        Panel(
            '[blue]1 - Calcular[/]   [red]2 - Sair[/]',
            title='[green]CONTROLE DE GASTOS[/]',
            subtitle='Escolha uma opção'
        )
    )

    while True:

        opcao = str(input('Digite um número: '))

        if opcao == '1':
            os.system('cls')
            orcamento = float(input('Qual o total do seu orçamento? '))
            gastos = float(input('Qual o total dos gastos? '))

            print(
                Panel(
                    '[blue]Sim[/]   [red]Não[/]',
                    title='[yellow]Os gastos serão divididos?[/]'
                )
            )
            while True:

                pergunta = str(input())

                if pergunta.lower() == 'sim':
                    print('sim')

                elif pergunta.lower() == 'não':
                    print('não')

                else:
                    print('Por favor, digite novamente...')

        elif opcao == '2':
            break

        else:
            print('Por favor, digite novamente uma das opções acima!')




if __name__ == '__main__':
    main()