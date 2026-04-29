#Transforma celsius em fahrenheit.
print('CONVERSOR DE CELSIUS PARA FAHRENHEIT')
x = input('Digite 1 para começar e 2 para cancelar.')
if x == '1':
    celsius = float(input('Digite um valor em graus Celsius (ºC): '))
    fahrenheit = (celsius * 9 / 5) + 32
    print(celsius, 'ºC para Fahrenheit é: ', fahrenheit, 'ºF')
else:
    print('Programa encerrado.')
    exit()
