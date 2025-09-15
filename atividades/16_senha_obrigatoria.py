# Inicializa contador de tentativas

tentativas = 0

# Solicita a senha

senha = input('Digite sua senha: ')

# Loop para garantir que a senha tenha dois "##"

while senha.count('#') != 2:  # Verifica se a senha tem exatamente dois '#'

    tentativas += 1  # Incrementa o contador de tentativas

    print(f'Senha inválida! A senha "{senha}" deve conter dois "#".')
    senha = input('Digite novamente sua senha (deve conter dois "#"): ')

# Conta a última tentativa (quando a senha finalmente é válida)

tentativas += 1

# Exibe o número de tentativas feitas

print(f'Senha válida! Você digitou a senha {tentativas} vezes.')