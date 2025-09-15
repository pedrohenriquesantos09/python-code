sexo = (input('Qual o seu sexo(F para feminino e M para masculino)? '))

if sexo == 'F':
    print('Não precisa se alistar')

else:
    idade = int(input('Digite sua idade: '))

    if idade < 18:
        print('Devido sua idade o indivíduo foi dispensado.')
    
    elif 18 <= idade <= 50:
        print('O indivíduo foi selicionada para ir á Ucrania')

    else:
        print('O indivíduo vai para Israel')



