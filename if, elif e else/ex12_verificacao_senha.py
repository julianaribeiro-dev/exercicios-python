senha_mestra = 1234

senha = input('Digite a senha para acessar o sistema: ')

if senha.isnumeric():
    senha = int(senha)
    if senha == senha_mestra:
        print('Acesso permitido')
    elif senha != senha_mestra:
        print('Senha incorreta')
else:
    print('Entrada inválida.')