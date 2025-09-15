# Criando um conjunto vazio para armazenar os nomes

nomes = set()

# Solicita 5 nomes ao usuário

for i in range(5):
    nome = input(f'Digite o nome {i+1}: ')
    nomes.add(nome)  # Adiciona o nome ao conjunto

# Exibe os nomes no conjunto

print("Os nomes digitados foram: ")
for nome in nomes:
    print(nome)