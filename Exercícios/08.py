### 8. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre
# uma mensagem dizendo que o número é inválido.

def calculo(num):
  if num >= 0:
    raiz = num ** 0.5
    print("A raiz quadrada do numero é: ",raiz)
  else:
    print("Número invalido")

num = int(input("Digite o numero: "))

calculo(num)
