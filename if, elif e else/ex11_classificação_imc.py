# Calcular o Índice de Massa Corporal (IMC) de um usuário/
# Perguntar altura (metros) e peso (kg).
# Classificar o usuário: Abaixo do peso, Peso normal, Sobrepeso, Obesidade.
# Deve exibir o valor do IMC e sua classificação.
print('CLASSIFICAÇÃO DE IMC')
print('Por favor, informe seu peso e altura.')
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC: ',imc,' - Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('IMC: ',imc,' - Peso ideal')
elif imc >= 25 and imc <= 29.9:
    print('IMC: ',imc, ' - Sobrepeso.')
elif imc >= 30:
    print('IMC: ',imc, ' - Obesidade')
