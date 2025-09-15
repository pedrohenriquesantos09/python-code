#elemento de trabalho

hora_metro = 2 #horas

largura = float(input('Digite a largura de seu lote: '))
comprimento = float(input('Digite o comprimeto do seu lote: '))

dimensao_lote = largura * comprimento

tempo_jardim = dimensao_lote / hora_metro

print(f'Serão necessárias {tempo_jardim:.2f} horas para plantar todas as flores')

