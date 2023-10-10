#!/usr/bin/env python3

import sys #adicionei a biblioteca sys

a=int(sys.argv[1]) #foi adicionado o comando int, que faz com que somente sejam aceitos valores inteiros e quando fornecido valor difirente disso, é escrita uma mensagem de erro ao usuário pedindo para que seja fornecidos valores inteiros
b=int(sys.argv[2]) #a e b correspondem aos valores que o usuário fornecerá na linha de comando

A = a*b/2  #operação que deseja-se calcular

if a < 500 and b < 500:  #verificando se os valores fornecidos pelo usuário são ambos menores que 500, caso sejam, o resultado já é trasmitido
    print('A área do triangulo retângulo com lados', a ,'=X e', b ,'=Y, é', A)

elif a > 500 and b < 500: #verificando se a é maior que 500 e avisando o usuário
    print(a,'é maior que 500, digite um número menor que 500 para a operação prosseguir')

elif b > 500 and a < 500: #verificando se b é maior que 500 e avisando o usuário
    print(b ,'é maior que 500, digite um número menor que 500 para a operação prosseguir')

elif a > 500 and b > 500:#verificando se a e b são maiores que 500 e avisando o usuário
    print('ambos valores digitados são maiores que 500, troque-os por números menores que 500 para a operação prosseguir')

else: #avisando que um ou os dois números fornecidos são iguais a 500 e que a operação só funciona para números menores que 500 diferente de 500
    print('algum valor digitado é igual a 500, substitua-o por um número menor que 500 para a operação prosseguir')


