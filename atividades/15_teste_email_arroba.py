#Entrada email

email = input('Digite seu email: ')

#Verificando se o email possui '@'

if '@' in email:
    print('Seu email possui @.')

#Criando looping para sempre solicitar o e-mail correto

while '@' not in email:
    print('Seu e-mail está inválido, pois não possui o @.')
    email = input('Por favor digite um e-mail válido: ')

print('Agora seu e-mail está correto e possui o @.')
