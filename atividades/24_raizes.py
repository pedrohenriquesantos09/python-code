import math

#Perguntando ao usuário os números 

numero1 = float(input('Digite um número para descobrir sua raiz quadrada: '))
numero2 = float(input('Digite um número para descobrir sua raiz quadrada: '))

#Calculando a raiz quadrada

raiz_quadrada1 = math.sqrt(numero1)
raiz_quadrada2 = math.sqrt(numero2)

#Somando os resultados

soma_raizes = raiz_quadrada1 + raiz_quadrada2
print(f'A soma das raízes dos numeros {numero1} e {numero2} é {soma_raizes}')