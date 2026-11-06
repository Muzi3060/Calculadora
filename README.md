# Controle de gastos (Calculadora)

A ideia desse mini projeto surgiu com o intuito de me ajudar a praticar POO e me ajudar com questões pessoais.

O uso dele é simples. Ele calcula utilizando os 4 operadores padrão, e também tem uma funcionalidade que, para caso vá pagar alguma dívida com alguém, pode colocar quantas pessoas vão participar, e quanto cada um vai pagar. Com isso ele calcula quanto cada um vai ter que pagar.

## O que o programa faz

Ao abrir, aparece um menu com três opções:

1. **Calcular**: informa o orçamento, o total dos gastos e quantas pessoas vão dividir. Para cada pessoa, informa nome e salário, e o programa mostra um resumo e quanto cada um deve pagar.
2. **Calcular gastos**: calculadora com soma, subtração, divisão e multiplicação.
3. **Sair**.

## Como executar

Requer Python 3. No terminal, dentro da pasta do projeto:

```bash
pip install -r requirements.txt
python main.py
```

## Estrutura do projeto

```
main.py                  menu e fluxo principal
funcoes.py               funções auxiliares (tela, leitura de valores, resultados)
classes/calculadora.py   classe Calculadora (operações e divisão de gastos)
classes/pessoa.py        classe Pessoa
ControleFinanceiro.spec  receita do PyInstaller para gerar o executável
```

## Gerar o executável (Windows)

```bash
pip install pyinstaller
pyinstaller ControleFinanceiro.spec
```

O executável é criado na pasta `dist/`. As pastas `build/` e `dist/` não são versionadas (veja o `.gitignore`).
