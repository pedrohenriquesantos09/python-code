import matplotlib.pyplot as plt

# Coordenadas do Eixo X e Eixo Y para a primeira linha

x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]

# Coordenadas do Eixo X e Eixo Y para a segunda linha

x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 8, 6, 9]

# Plotar a primeira linha (azul)

plt.plot(x1, y1, marker='o', linestyle='-', color='b', label="Linha 1")

# Plotar a segunda linha (vermelha)

plt.plot(x2, y2, marker='o', linestyle='-', color='r', label="Linha 2")

# Adicionar título e rótulos aos eixos

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.title('Gráfico de Linha')

# Adicionar grade

plt.grid(True)

# Adicionar uma legenda para identificar as linhas

plt.legend()

# Mostrar o gráfico

plt.show()