import random  #faz o computador escolheu uma opção
from time import sleep # faz dar uma pausa na linha que eu escolher

print('''Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

num = int(input('Qual sua opção? '))

print('JO')
sleep(1)  # dar um apausa de 1 segundo
print('KEN')
sleep(1) # pausa de 1 segundo
print('PO!!!')
sleep(1) # pausa de 1 segundo
print('==' * 20)

opc = ['PEDRA', 'PAPEL', 'TESOURA'] # estou dando as opções para o computador
jogador = opc[num] # ta convertendo o que a pessoa escolheu

computador = random.choice(opc) #computador vai escolher aleatoriamente um aopção
print(f'O computador jogou {computador}')
print(f'Você jogou {jogador}')
print('==' * 20)

if jogador == computador: # vai ferificar se minha escolha e semelhante a do computador
    print('EMPATE')
elif (jogador == 'PEDRA' and computador == 'TESOURA') or \
     (jogador == 'PAPEL' and computador == 'PEDRA') or \
     (jogador == 'TESOURA' and computador == 'PAPEL'): # vai verificar outras condições para o vencedor
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU')
