import re  # Importação do módulo para expressões regulares
import ttg  # Importação do módulo para geração de tabela verdade

# Definição dos operadores válidos na lógica proposicional
operators = {'and', 'or', 'not', '~', '=>', 'nand', 'nor', 'xor', '='}

while True:  # Início do loop principal
    # Requisito 1: Fazer a leitura da fórmula como string
    formula = input('Entre com a fórmula: ')  # Solicita a inserção da fórmula
    formula = formula.lower()  # Converte a fórmula para minúsculas

    print('\nFórmula = ', formula, '\n')

    # Encontrar todos os tokens na fórmula usando expressões regulares
    tokens = re.findall(r'[a-z]+|[^a-z\s]+', formula)

    # Filtrar os tokens para variáveis, removendo operadores e espaços
    variables = sorted(set(filter(lambda x: x.isalpha() and x not in operators, tokens)))

    print('Variáveis = ', variables)  # Apresenta as variáveis sem repetição

    # Mapeamento de operadores para exibição mais legível
    operation_mapping = {
        'and': 'AND', # Símbolo para representar o E
        'or': 'OR', # Símbolo para representar o OU 
        'not': 'NOT', # Símbolo para representar o Não
        '~': 'NOT', # Símbolo para representar o Não 
        '=>': 'Implicação', # Símbolo para representar a implicação 
        'nand': 'NAND', # Símbolo para representar o NAND 
        'nor': 'NOR', # Símbolo para representar o NOR
        'xor': 'XOR', # Símbolo para representar o XOR
        '=': 'Bicondicional'  # Símbolo para representar o bicondicional
    }

    # Contagem das operações presentes na fórmula
    operations = {}
    for token in tokens:
        if token in operators:
            operation = operation_mapping.get(token, token)
            if operation in operations:
                operations[operation] += 1
            else:
                operations[operation] = 1

    print('Operadores utilizados e suas frequências:')
    for operation, frequency in operations.items():
        print(f'{operation}: {frequency}')  # Apresenta os operadores e suas frequências

    # Geração da tabela verdade usando a biblioteca ttg
    table = ttg.Truths(variables, [formula])
    print('\nTabela Verdade:')  # Apresenta a tabela verdade da fórmula
    print(table)

    resp = input('\nPara continuar, tecle Enter. Para sair, digite "q": ')
    if resp == 'q':
        break  # Pergunta se o usuário quer encerrar o programa ou continuar inserindo fórmulas

print('\nFim\n')  # Mensagem de encerramento do programa