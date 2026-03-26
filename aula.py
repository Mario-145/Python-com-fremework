# 4  tipos
# str      int             float    bool
# textos numeros inteiros reais lógicos
# 'texto',  10 ,  5.2 ,  True , False
# 'Bom dia', 2026,1.80, 1 , 0
# 'Seu nome:',1, 60.200, 
# 'R$'


# ESTRUTURAS DE DADOS ****


# espaços na memória ram da maquina
# variar
# variaveis são dados únicos
# interpertador 
# meio termo linguagem 
# força indentação = organização
# OUTPUT - SAIDA - print()
# nomear de forma semantica  -  boa pratica


# regras para criar variáveis:
# _ ou letra
# não pode começar por números 
# não pode carcateres especiais 
# pode utilizar números(só não pode começar)
# palavra composta snake_case


# linguagem alto nivel
# interpretada
# dinamica - variáveis


print('CADASTRO DE USUÁRIOS:')


nome = 'Lucas Lima'
idade  =  25
email_usuario = 'lucas@gmail.com'
peso = 80.50
altura =  1.90
endereco = 'Rua 10, Jd X'
graduacao = 'ADS'
casado = False 


# SAÍDA
print(nome)
print(idade)
print(email_usuario)
print(endereco)
print(graduacao)
print(peso)
print(altura)
print(casado)


# ENTRADA

print( 'IMC')

# peso =  float(input('Digite seu peso: '))
# altura  =  float(input('Digite sua altura: '))
imc  =  peso/altura**2
print('IMC', imc)

print('SINAIS DE CALCULOS ARITMÉTICO')

print(10+200) # soma
print(10-200) # subtração
print(10*200) # multiplicalçao8
print(10/200) # divisão
print('modulo', 10%200) #módulo
print(10**2) # potencia
print(10//200.0) # divisão c/ 2 barras


# sinais lógicos


print(10 == 200) # comparar
print(10 > 200) # verifa se 1º numero é maior
print(10<200) # verifa se 1º numero é menor
print(10>=200) # maior ou iguael
print(10<=200) # menor ou igual
print(10 != 2) # diferente80

# n1 = int(input('digite um numero'))
# n2 = int(input('digite um numeor'))

# print(20+20)
# print(20-20)
# print(20*20)
# print(20//20)

# print (n1 == n2)
# print(n1 > n2)
# print(n1 > 20)
# print(n2 > 10)

# Peça o valor de um produto e: 

# Calcule um desconto de 10%.


# Mostre o valor final.


# Verifique se o valor final é maior que 100.


# Verifique se o produto ficou barato (menor que 50).

produto =  float(input('Digite o valor do produto: '))


print(produto * 0.10)


print(produto > 100)

print(produto < 50)


# Peça o valor de um produto e:
produto =  float(input('Digite o valor do produto: '))


# Calcule um desconto de 10%.


print(produto * 0.10)


# Mostre o valor final.


valor_prod = produto - produto
print('Valor do produto R$', valor_prod)


# Verifique se o valor final é maior que 100.


print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# Verifique se o produto ficou barato (menor que 50).


print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)