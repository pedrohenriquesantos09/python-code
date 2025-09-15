# Importações necessárias

import matplotlib.pyplot as plt

# Solicitar ao usuário a produção de cada item na fazenda

trigo = float(input("Digite a quantidade produzida de Trigo (em toneladas): "))
soja = float(input("Digite a quantidade produzida de Soja (em toneladas): "))
abacaxi = float(input("Digite a quantidade produzida de Abacaxi (em toneladas): "))
mandioca = float(input("Digite a quantidade produzida de Mandioca (em toneladas): "))
tomate = float(input("Digite a quantidade produzida de Tomate (em toneladas): "))

# Dados para o gráfico

produtos = ['Trigo', 'Soja', 'Abacaxi', 'Mandioca', 'Tomate']
producoes = [trigo, soja, abacaxi, mandioca, tomate]

# Exibir os valores digitados

for produto, producao in zip(produtos, producoes):
    print(f'{produto}: {producao} toneladas')

# Plotando o gráfico de pizza

plt.figure(figsize=(8, 8))
plt.pie(

    producoes,  # valores a serem plotados
    labels=produtos,  # rótulos dos produtos
    autopct='%1.2f%%',  # mostrar a porcentagem com 2 casas decimais
    textprops={'fontsize': 14},  # aumentar o tamanho da fonte
    colors=['yellowgreen', 'gold', 'orange', 'purple', 'red']  # cores para cada fatia
)

# Adicionar título ao gráfico

plt.title(
    label="Distribuição da Produção na Fazenda",
    fontdict={"fontsize": 16},
    pad=20
)

# Exibir o gráfico

plt.show()