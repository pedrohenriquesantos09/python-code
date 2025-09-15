import math

#Perguntando ao usuário um número

numero = float(input('Digite um número para calcular sua raiz: '))

#Calculando a raiz quadrada do número 

raiz_quadrada = math.sqrt(numero)

#Imprimindo resultado 

print(f'A raiz quadrada de {numero} é {raiz_quadrada:.0f}')