print('Qual a sua idade?')
idade = int(input())

if idade >= 0 and idade <= 12:
    print('Você é criança.')
elif idade >= 13 and idade <=18:
    print('Você é adolescente.')
elif idade >= 18 and idade <= 122:
    print('Você é adulto.')
elif idade >= 200 and idade <= 5000:
    print('Você é um vampiro.')
else:
    print('ERRO')