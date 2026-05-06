print('Bem-vindo(a) ao verificador de tarifas do seu banco.')
inicio = input('Deseja verificar as tarifas aplicadas a sua conta? (S/N)').upper()
if inicio in ['S', 'SIM']:
    print()
    print('Para verificar, por favor, insira o tipo de conta. \n')
    tipo_conta = int(input('Pressione 1 para Conta Comum ou 2 para Conta Premium. '))

    # Conta Comum
    if tipo_conta == 1:
        saldo_medio = float(input('Insira o seu saldo: '))
        if saldo_medio < 1000:
            tarifa = 25
        elif saldo_medio < 5000:
            tarifa = 15
        else:
            tarifa = 0

    # Conta Premium
    elif tipo_conta == 2:
        saldo_medio = float(input('Insira o seu saldo: '))
        if saldo_medio < 5000:
            tarifa = 20
        else:
            tarifa = 0

    else:
        print('Tipo de conta inválido.')
        exit()
    print(f'Saldo médio: R$ {saldo_medio:.2f}')
    print(f'Tarifa: R$ {tarifa:.2f} \n')
    print('Obrigado por usar nossos serviços. Até logo!')
else:
    print()
    print('Obrigado por usar os nossos serviços. Até logo!')
    exit()

