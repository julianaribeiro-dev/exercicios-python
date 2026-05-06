print('CALCULADORA DE MONETIZAÇÃO POR VIEW')
print()
input('Pressione ENTER para iniciar...\n')

visualizacoes = int(input('Digite a quantidade de visualizações atual: '))

if visualizacoes < 0:
    print('As visualizações não podem ser negativas.')
    print('Programa encerrado.')
    exit()
elif visualizacoes > 1000000:
    monetizacao = 0.05
elif visualizacoes >= 100001:
    monetizacao = 0.03
elif visualizacoes >= 10001:
    monetizacao = 0.02
else:
    monetizacao = 0

valor_base = visualizacoes*monetizacao
valor_total = valor_base
print(f'Valor por views: R$ {monetizacao:.2f}')
print(f'Valor base: R$ {valor_base:.2f}')

if visualizacoes > 500000:
    valor_total += 500
    print('Bônus: R$ 500.00')

print(f'Valor total: R$ {valor_total:.2f}')