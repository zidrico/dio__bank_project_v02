menu = """
[E] = extrato
[S] = sacar
[D] = depósito
[SAIR] = sair da operação
"""
saldo_atual = 0
limite = 1000
extrato = {
    'saldo': saldo_atual,
    'limite': limite,
    'movimentações': []  # Lista para armazenar todas as movimentações
}
numero_saques = 0
limite_saque_diário = 3

while True:
    print("\n" + "="*30)
    opcao = input(f'escolha uma opção:{menu}').upper()
    if opcao == 'E':
        print('\n----EXTRATO BANCÁRIO----')
        print(f'Saldo atual: {extrato["saldo"]}')
        print(f'Limite: {extrato["limite"]}')
        print('Movimentações:')
        for mov in extrato['movimentações']:
            print("--------------------")
            print(f'{mov[0]}: {mov[1]}')
    elif opcao == 'S':
        while True:
            print("\n" + "="*30)
            valor_sacado = float(input('Informe o valor do saque: '))
            limite_atual = limite
            if valor_sacado > limite:
                print(f'Saque maior que o limite de {limite} reais')
                print('Tente novamente um valor abaixo do limite')
            else:
                break
        if numero_saques < limite_saque_diário and valor_sacado <= saldo_atual:
            saldo_atual -= valor_sacado
            numero_saques += 1
            extrato['saldo'] = saldo_atual
            extrato['movimentações'].append(('Saque', valor_sacado))  # Adiciona a movimentação de saque no extrato
    elif opcao == 'D':
        valor_depositado = float(input('Informe o quanto deseja depositar: '))
        saldo_atual += valor_depositado
        extrato['saldo'] = saldo_atual
        extrato['movimentações'].append(('Depósito', valor_depositado))  # Adiciona a movimentação de depósito no extrato
        print('Depósito realizado com sucesso!')
    elif opcao == 'SAIR':
        break