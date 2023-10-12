#!/usr/bin/env python3

import sys #adicionando biblioteca sys
dna=str(sys.argv[1])  #impondo que apenas strings possam ser digitadas no primeiro argumento
n1 = int(sys.argv[2]) #impondo que só números inteiros possam ser digitados nos argumentos de 2 ao 7
n2 = int(sys.argv[3])
n3 = int(sys.argv[4])
n4 = int(sys.argv[5])
n5 = int(sys.argv[6])
n6 = int(sys.argv[7])

if n1 > 124:  #aviso caso n seja maior que 124 que é o maior índice para o dna 
    print('o valor máximo é 124 e você inseriu',n1,',altere este valor para a operação prosseguir')
if n2 > 124:
    print('o valor máximo é 124 e você inseriu',n2,',altere este valor para a operação prosseguir')
if n3 > 124:
    print('o valor máximo é 124 e você inseriu',n3,',altere este valor para a operação prosseguir')
if n4 > 124:
    print('o valor máximo é 124 e você inseriu',n4,',altere este valor para a operação prosseguir')
if n5 > 124:
    print('o valor máximo é 124 e você inseriu',n5,',altere este valor para a operação prosseguir')
if n6 > 124:
    print('o valor máximo é 124 e você inseriu',n6,',altere este valor para a operação prosseguir')
 
cds1 = dna[n1:n2] #caracterizando cds1 , cds2 e cds3
cds2 = dna[n3:n4]
cds3 = dna[n5:n6]

print('Sequência cds1:',cds1) #extraindo cds1
if 'ATG' in cds1[0:3]:      #verificando se cds1 começa com ATG
    print('A sequência CDS1 inicia-se com o códon ATG')
else:
    print('A sequência CDS1 não se inicia com o códon ATG')
print('Sequência cds2:',cds2) #extraindo cds2
print('Sequência cds3:',cds3)#extraindo cds3 
if 'TAG' in cds3[31:]: #verificando se cds3 termina com TAG, TAA ou TGA
    print('A sequência CDS3 termina com o códon TAG')
if 'TAA' in cds3[31:]:
    print('A sequência CDS3 termina com o códon TAA')
if 'TGG' in cds3[31:]:
    print('A sequência CDS3 termina com o códon TGA')

if 'ATG' in cds1[0:3] and 'TAG' in cds3[31:]:  #caso cds1 comece com ATG e cds3 termine com TAG, TAA ou TGA fazer cds1 + cds2 + cds3
    print(cds1 + cds2 + cds3)
if 'ATG' in cds1[0:3] and 'TAA' in cds3[31:]:
    print(cds1 + cds2 + cds3)
if 'ATG' in cds1[0:3] and 'TGG' in cds3[31:]:
    print(cds1 + cds2 + cds3)




