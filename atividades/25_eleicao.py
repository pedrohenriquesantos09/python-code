import matplotlib.pyplot as plt

# Solicitar os valores de Y para cada candidato

Y1 = float(input("Digite o valor Y para LEO22: "))
Y2 = float(input("Digite o valor Y para RENATO10: "))
Y3 = float(input("Digite o valor Y para CORONEL22: "))

# Definindo as coordenadas X (nomes dos candidatos) e Y (valores fornecidos)

candidatos = ['LEO22', 'RENATO10', 'CORONEL22']
intencao_votos = [Y1, Y2, Y3]

# Criando o gráfico

plt.figure(figsize=(8, 6))
plt.bar(candidatos, intencao_votos, color=['blue', 'green', 'red'])

# Adicionando título e rótulos aos eixos

plt.title('Gráfico de Intenção de Votos')
plt.xlabel('Candidatos')
plt.ylabel('Intenção de Votos (Valores Y)')

# Exibindo o gráfico

plt.show()
