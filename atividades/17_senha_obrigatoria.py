# Inicializa contador de tentativas e o contador de "#"

tentativas = 0

# Solicita a senha

senha = input('Digite sua senha: ')

# Loop para garantir que a senha tenha dois "##"

while True:
    
    # Inicializa o contador de "#" em cada tentativa

    num_hashes = 0
    
    # Conta quantos "#" existem na senha

    for char in senha:
        if char == '#':
            num_hashes += 1
    
    # Verifica se a senha tem exatamente dois "#"

    if num_hashes == 2:
        break  # Senha válida, sai do loop

    
    # Se a senha for inválida, incrementa as tentativas e pede novamente

    tentativas += 1
    print(f'Senha inválida! A senha "{senha}" deve conter dois "#".')
    senha = input('Digite novamente sua senha (deve conter dois "#"): ')

# Conta a última tentativa (quando a senha finalmente é válida)

tentativas += 1

# Exibe o número de tentativas feitas

print(f'Senha válida! Você digitou a senha {tentativas} vezes.')