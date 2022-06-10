print("\t----Tabuada----")
numero = int(input("Informe o número para ver a tabuada: "))
print("\nTabuada de",numero, ":")
for i in range(1, 11):
  print(numero, "X", i, "=", (numero * i))
print("\n")
#------------------------------------------------------------#
print("\t----Cálculo do Novo SALÁRIO----")
salario_atual = float(input("Informe o salário atual: "))
if (salario_atual<500):
  salario_novo=salario_atual+(salario_atual*0.15)
  print("Salário com reajustes = ", salario_novo)

if ((salario_atual>=500) and (salario_atual <=1000)):
  salario_novo=salario_atual+(salario_atual*0.10)
  print("Salário com reajuste = ",salario_novo)

if (salario_atual>1000):
  salario_novo=salario_atual+(salario_atual*0.05)
  print("Salário com reajuste = ",salario_novo)
print("\n")
#------------------------------------------------------------#
print("\t--Números entre 5 e 100 que são divisíveis por 7--")
for num in range(5, 100):
  if (num % 7 == 0 and num % 5 != 0):
    print(num)
print("\n")
#------------------------------------------------------------#
print("\t----Soma de 1 até o valor digitado----")
soma_numeros = 0
numero = int(input("Por favor,insira um número: "))
for i in range(1, numero + 1, 1):
  soma_numeros += i
print("A soma é = ", soma_numeros)
print("\n")
#------------------------------------------------------------#
print("\t----A Dança dos Números----")
x = int(input("Informe um número para brincar: "))
if x < 0:
  print("É um número negativo!")
elif x == 0:
  print("É um número neutro!")
elif x > 0:
  print("É um número positivo!")
print("\n")
#------------------------------------------------------------#
print("\t----Contagem dos Dígitos----")
digitos = int(input("Digite um número para contar seus dígitos: "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador += 1
print("Total de Dígitos = ",contador)
print("\n")
