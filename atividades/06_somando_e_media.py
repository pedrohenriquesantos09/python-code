# Inicializa a soma
soma = 0

# Captura 5 números inteiros
for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    soma += numero

# Calcula a média
media = soma / 5

# Exibe a soma e a média
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media:.2f}")