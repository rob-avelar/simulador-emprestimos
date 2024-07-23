''' 
Empréstimos
Seu desafio será implementar um serviço que determine quais modalidades de empréstimo uma pessoa tem acesso.

Exemplo
As modalidades de empréstimo que serão analisadas são:

Empréstimo pessoal: Taxa de juros de 4%.
Empréstimo consignado: Taxa de juros de 2%.
Empréstimo com garantia: Taxa de juros de 3%.
As modalidades de empréstimo disponíveis para uma pessoa são baseadas em algumas variáveis específicas, são elas:

Idade
Salário
Localização
Seu serviço recebe uma chamada para determinar quais modalidades de empréstimo uma pessoa tem acesso.

Requisitos

Conceder o empréstimo pessoal se o salário do cliente for igual ou inferior a R$ 3000.
Conceder o empréstimo pessoal se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP).
Conceder o empréstimo consignado se o salário do cliente for igual ou superior a R$ 5000.
Conceder o empréstimo com garantia se o salário do cliente for igual ou inferior a R$ 3000.
Conceder o empréstimo com garantia se o salário do cliente estiver entre R$ 3000 e R$ 5000, se o cliente tiver menos de 30 anos e residir em São Paulo (SP).'''




import re

lista_clientes = []

estados_brasileiros = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 
    'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 
    'SP', 'SE', 'TO'
]

def formatar_cpf(cpf):
    # Formata o CPF no padrão 000.000.000-00
    cpf = re.sub(r'\D', '', cpf)  # Remove tudo que não é dígito
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

def cadastrar_clientes():  # Cadastro de clientes
    while True:
        cpf = input('Digite o seu CPF (apenas números): ')
        if len(cpf) == 11 and cpf.isdigit():
            cpf = formatar_cpf(cpf)
            break
        else:
            print("CPF inválido. Por favor, insira exatamente 11 números.")

    nome = input('Qual é o seu nome: ')
    idade = int(input('Qual é a sua idade: '))
    salario = float(input('Qual é o seu salário: R$ '))
    
    while True:
        estado = input('Estado em que reside (digite a sigla do estado, por exemplo, SP): ').upper()
        if estado in estados_brasileiros:
            break
        else:
            print("Sigla de estado inválida. Por favor, insira uma sigla válida (por exemplo, SP).")

    cliente = {
        'cpf': cpf,
        'nome': nome,
        'idade': idade,
        'salario': salario,
        'estado': estado
    }

    lista_clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")

def simular_emprestimo():  # Simulação de empréstimo
    while True:
        cpf = input('Digite o CPF do cliente (apenas números): ')
        if len(cpf) == 11 and cpf.isdigit():
            cpf = formatar_cpf(cpf)
            break
        else:
            print("CPF inválido. Por favor, insira exatamente 11 números.")

    cliente = next((c for c in lista_clientes if c['cpf'] == cpf), None)
    
    if not cliente:
        print("Cliente não encontrado!")
        return

    opcoes_disponiveis = []
    if requisitos_emprestimo_pessoal_e_com_garantia(cliente):
        opcoes_disponiveis.append(1)
    if requisitos_emprestimo_consignado(cliente):
        opcoes_disponiveis.append(2)
    if requisitos_emprestimo_pessoal_e_com_garantia(cliente):
        opcoes_disponiveis.append(3)
    
    if not opcoes_disponiveis:
        print("Nenhuma linha de crédito disponível.")
        return

    while True:
        print('Escolha o tipo de empréstimo que deseja simular')
        if 1 in opcoes_disponiveis:
            print('1 - Empréstimo pessoal')
        if 2 in opcoes_disponiveis:
            print('2 - Empréstimo consignado')
        if 3 in opcoes_disponiveis:
            print('3 - Empréstimo com garantia')
        print('4 - Sair')

        opcao = int(input('Escolha a opção desejada: '))

        if opcao == 1 and 1 in opcoes_disponiveis:
            emprestimo_pessoal(cliente)  # Empréstimo pessoal
        elif opcao == 2 and 2 in opcoes_disponiveis:
            emprestimo_consignado(cliente)  # Empréstimo consignado
        elif opcao == 3 and 3 in opcoes_disponiveis:
            emprestimo_garantia(cliente)  # Empréstimo com garantia
        elif opcao == 4:
            break
        else:
            print('Opção inválida ou não disponível para este cliente')

def requisitos_emprestimo_pessoal_e_com_garantia(cliente):  # Requisitos para empréstimo pessoal e com garantia
    if cliente['salario'] <= 3000:
        return True
    elif 3000 < cliente['salario'] <= 5000 and cliente['idade'] <= 30 and cliente['estado'] == 'SP':
        return True
    else:
        return False

def requisitos_emprestimo_consignado(cliente):  # Requisitos para empréstimo consignado
    if cliente['salario'] >= 5000:
        return True
    else:
        return False

def validar_valor_emprestimo(cliente, valor_emprestimo):
    if valor_emprestimo > 5 * cliente['salario']:
        print(f"Valor do empréstimo excede o limite de 5 vezes o salário ({5 * cliente['salario']}).")
        return False
    return True

def confirmar_emprestimo():
    while True:
        confirmacao = input('Deseja confirmar o empréstimo? (s/n): ').lower()
        if confirmacao in ['s', 'n']:
            return confirmacao == 's'
        else:
            print('Opção inválida. Digite "s" para sim ou "n" para não.')

def solicitar_valor_emprestimo(cliente):
    while True:
        valor_emprestimo = float(input('Qual é o valor do empréstimo: R$ '))
        if validar_valor_emprestimo(cliente, valor_emprestimo):
            return valor_emprestimo

def emprestimo_pessoal(cliente):  # Empréstimo pessoal
    if requisitos_emprestimo_pessoal_e_com_garantia(cliente):
        valor_emprestimo = solicitar_valor_emprestimo(cliente)
        taxa_juros = 4
        valor_juros = valor_emprestimo * (taxa_juros / 100)
        valor_total = valor_emprestimo + valor_juros
        print(f'Valor dos juros: R$ {valor_juros}')
        print(f'Valor total do empréstimo: R$ {valor_total}')
        if confirmar_emprestimo():
            print('Empréstimo pessoal confirmado.')
        else:
            print('Empréstimo pessoal não confirmado.')
    else:
        print('Não é possível realizar o empréstimo')

def emprestimo_consignado(cliente):  # Empréstimo consignado
    if requisitos_emprestimo_consignado(cliente):
        valor_emprestimo = solicitar_valor_emprestimo(cliente)
        taxa_juros = 2
        valor_juros = valor_emprestimo * (taxa_juros / 100)
        valor_total = valor_emprestimo + valor_juros
        print(f'Valor dos juros: R$ {valor_juros}')
        print(f'Valor total do empréstimo: R$ {valor_total}')
        if confirmar_emprestimo():
            print('Empréstimo consignado confirmado.')
        else:
            print('Empréstimo consignado não confirmado.')
    else:
        print('Não é possível realizar o empréstimo')

def emprestimo_garantia(cliente):  # Empréstimo com garantia
    if requisitos_emprestimo_pessoal_e_com_garantia(cliente):
        valor_emprestimo = solicitar_valor_emprestimo(cliente)
        taxa_juros = 3
        valor_juros = valor_emprestimo * (taxa_juros / 100)
        valor_total = valor_emprestimo + valor_juros
        print(f'Valor dos juros: R$ {valor_juros}')
        print(f'Valor total do empréstimo: R$ {valor_total}')
        if confirmar_emprestimo():
            print('Empréstimo com garantia confirmado.')
        else:
            print('Empréstimo com garantia não confirmado.')
    else:
        print('Não é possível realizar o empréstimo')

# Menu principal
def menu():
    while True:
        print("1 - Cadastrar cliente")
        print("2 - Simular empréstimo")
        print("3 - Sair")

        opcao = int(input("Escolha a opção desejada: "))

        if opcao == 1:
            cadastrar_clientes()
        elif opcao == 2:
            simular_emprestimo()
        elif opcao == 3:
            break
        else:
            print("Opção inválida")

# Executar menu principal
menu()





