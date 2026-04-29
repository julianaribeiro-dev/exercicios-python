#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
print('CALCULO DO SALÁRIO')
valorhora = float(input('Quando você ganha por hora? '))
horastrab = float(input('Quantas horas você trabalhou no mês? '))
salario = valorhora * horastrab
print('Seu salário este mês é R$',salario)