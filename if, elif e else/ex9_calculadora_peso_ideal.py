altura = float(input('Digite sua altura'))
sexo = str(input('Digite o seu sexo: ')).upper()
if sexo == 'M':
    pesoideal = (72.8*altura)-58
elif sexo == 'F':
    pesoideal = (62.1*altura)-44.7
print(pesoideal)

