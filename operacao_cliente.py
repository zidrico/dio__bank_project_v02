def menu():
    menu_text = """
    ||===================== MENU =====================||
    [Novo]   Novo usuário   
    [User]   Menu Usuário   
    [E]      Extrato        
    [S]      Sacar
    [D]      Depósito       
    [SAIR]   Sair da operação
    """
    return menu_text

def imprimir_extrato(extrato):
    print('\n----EXTRATO BANCÁRIO----')
    print(f'Saldo atual: {extrato["saldo"]}')
    print(f'Limite: {extrato["limite"]}')
    print('Movimentações:')
    for mov in extrato['movimentações']:
        print("--------------------")
        print(f'{mov[0]}: {mov[1]}')

def sacar(saldo_atual, limite, numero_saques, limite_saque_diário, extrato):
    valor_sacado = float(input('Informe o valor do saque: '))
    if valor_sacado > saldo_atual:
        print(f'Você não possui saldo suficiente para sacar. Seu saldo atual é de {saldo_atual}.') 
    elif valor_sacado > limite:
        print(f'Saque maior que o limite de {limite} reais')
        print('Tente novamente um valor abaixo do limite')
    elif numero_saques < limite_saque_diário and valor_sacado <= saldo_atual:
        saldo_atual -= valor_sacado
        numero_saques += 1
        extrato['saldo'] = saldo_atual
        print(f'Saldo atual: {extrato["saldo"]}')
        extrato['movimentações'].append(('Saque', f'-{valor_sacado}'))
    return saldo_atual, numero_saques, extrato

def depositar(saldo_atual, extrato):
    valor_depositado = float(input('Informe o quanto deseja depositar: '))
    if valor_depositado > 0:
        saldo_atual += valor_depositado
        extrato['saldo'] = f'{saldo_atual:.2f}'
        extrato['movimentações'].append(('Depósito', f'+{valor_depositado}'))
        print(f'Saldo atual: {extrato["saldo"]}')
        print('Depósito realizado com sucesso!')      
    else:
        print('Falha na operação. Tente novamente.')
    return saldo_atual, extrato

def criar_usuario(lista_usuarios, contas):
    while True:
        nome = input('Nome: ')
        cpf = input('Informe o CPF: ')
        conta = input('Conta: ')
        agencia = input('Agência: ')
        if not cpf in lista_usuarios:
            if cpf.isdigit():
                if not filtrar_usuario(cpf, lista_usuarios):
                    lista_usuarios.append({'nome': nome, 'cpf': cpf, 'conta': conta, 'agencia': agencia})
                    break
                print('CPF inválido. Por favor, digite apenas números.')
            else:
                print('CPF inválido. Por favor, digite apenas números.')
        else:
            print('CPF JÁ CADASTRADO!!!. Escolha um CPF válido.')

    return nome, cpf, conta, agencia

def filtrar_usuario(cpf, lista_usuarios):
    if cpf in lista_usuarios:
        print('CPF já cadastrado.')
        return True
    else:
        return False

def menu_usuario(conta, nome, saldo_atual):
    print(f'Nome: {nome}')
    print(f'Conta: {conta}')
    print(f'Saldo atual: {saldo_atual:.2f}')

def sair():
    print("Você escolheu sair. Até a próxima!")
    return False

def main():
    numero_saques = 0
    limite_saque_diário = 3
    saldo_atual = 0
    limite = 1000
    extrato = {'saldo': saldo_atual, 'limite': limite, 'movimentações': []}
    continuar = True
    lista_usuarios = []  # Lista de usuários (cada usuário é um dicionário)
    contas = ['1010', '1011', '1012']  # Contas válidas

    while continuar:
        print(menu())  # Exibir o menu para o usuário
        opcao = input("Escolha uma opção: ").upper()  # Capturar a entrada do usuário e converter para maiúsculas

        if opcao == 'E':
            imprimir_extrato(extrato)
        elif opcao == 'S':
            saldo_atual, numero_saques, extrato = sacar(saldo_atual, limite, numero_saques, limite_saque_diário, extrato)
        elif opcao == 'D':
            saldo_atual, extrato = depositar(saldo_atual, extrato)
        elif opcao == 'NOVO':
            # filtrar_usuario(cpf, lista_usuarios)
            nome, cpf, conta, agencia = criar_usuario(lista_usuarios, contas)
            lista_usuarios.append({'nome': nome, 'cpf': cpf, 'conta': conta, 'agencia': agencia})
        elif opcao == 'USER':
            menu_usuario(conta, nome, saldo_atual)
        elif opcao == 'SAIR':
            print(sair())
if __name__ == "__main__":
    main()
