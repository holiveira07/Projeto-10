# funcao +

def adicao(a, b):
  return a + b

# funcao -

def subtracao(a, b):
  return a - b

# funcao *

def multiplicacao(a, b):
  return a * b

# funcao /

def divisao(a, b):
  return a / b

  print('\nEntra: \n1 para adicao \n2 para subtracao \n3 para multiplicacao \n4 para divisao')

a=int(input("Digite o primeiro número: " ))
b=int(input("Digite o segundo número: " ))

escolha = (input("Escolha a operação: "))

# adicao
if escolha == "1":
  print(adicao(a, b)) 

# subtracao
if escolha == "2":
  print(subtracao(a, b))

# multplicacao
if escolha == "3":
  print(multiplicacao(a, b))

# diviao
if escolha == "4":
  print(divisao(a, b)) 