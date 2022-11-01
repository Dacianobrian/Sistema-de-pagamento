#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
valor=float(input(' Quanto custo o produto '))
print('digite a opçao que voce gostaria ')
print('[1] A vista no dinheiro 10% de desconto')
print('[2] A vista no cartao 5 % de desconto')
print('[3] em ate 2x no carta:preço formal')
print('[4] em 3x ou mais no cartao 20% com juros')
opçao=int(input(' qual opçao voce escolha ? '))
if opçao==1:
    total= valor - (valor *10 / 100)
    print(' seu produto fica de R${:.2F} com 10% de desconto R%{:.2F}'.format(valor,total))
elif opçao==2:
    total= valor - (valor *5/100)
    print(' seu preço de R${:.2F}  com 5% de desconto fica R${:.2F} '.format(valor,total))
elif opçao==3:
    total=valor/2
    print('seu produto em 2x no cartao fica R${:.2F} '.format(total))
elif opçao==4:
    total= valor + (valor*20/100)
    parcela=int(input('quantas vezes vai parcela?'))
    parc= total/parcela
    print( 'seu preço é de R${:.2F} R${:.2F} em {}x '.format(valor,parc,parcela))
