import math
import numpy_financial as np


def valor_futuro():
  NumPeriodo = float(input("digite o numero de periodos: "))
  juros = float(input("digite a taxa de juros compostos: ")) / 100
  valorPresente = float(input("digite o valor atual: "))
  valorFinal = valorPresente * math.pow((1 + juros), NumPeriodo)
  print("o valor final é: %.2f" % valorFinal)


def valor_presente():
  NumPeriodo = float(input("digite o numero de periodos: "))
  juros = float(input("digite a taxa de juros compostos: ")) / 100
  valorFinal = float(input("digite o valor atual: "))
  valorPresente = valorFinal / math.pow((1 + juros), NumPeriodo)
  print("o valor presente é: %.2f" % valorPresente)


def valor_presente_liquido():
  juros = float(input("digite a taxa de juros compostos: ")) / 100
  valorInicial = float(input("digite o investimento inicial: "))
  valorPresenteLiquido = valorInicial * -1
  i = 1
  j = 1
  while i == 1:
    valorPeriodo = float(
      input("digite o Fluxo de Caixa do periodo " + str(j) + ":"))
    valorPresenteLiquido = valorPresenteLiquido + (valorPeriodo / math.pow(
      (1 + juros), j))
    i = int(
      input(
        "deseja adicionar mais um periodo?\n 1 - SIM\n 2 - NÃO\n escolha:"))
    j = j + 1
  print("O valor presente liquido é: %.2f" % valorPresenteLiquido)


def paypay():
  j = 0
  juros = float(input("digite a taxa de juros compostos: ")) / 100
  valorInicial = float(input("digite o investimento inicial: "))
  valorPeriodoInicial = (valorInicial / math.pow((1 + juros), j)) * -1
  i = 1
  while i == 1:
    j = j + 1
    valorPer = float(
      input("digite o Fluxo de Caixa do periodo " + str(j) + ":"))
    valorPeriodo = valorPer / math.pow((1 + juros), j)
    valorPeriodoInicial = valorPeriodoInicial + valorPeriodo
    if valorPeriodoInicial >= 0:
      payback = (j - 1) + ((
        (valorPeriodoInicial - valorPeriodo) * -1) / valorPeriodo)
      i = 2

  print("Payback = %.2f" % payback + " Anos")


def TIR():
  investimento = float(input("digite o investimento inicial: ")) * -1
  anos = []
  quantiaAnos = int(input("digite a quantidade de anos: "))
  anos.append(investimento)
  for i in range(0, quantiaAnos):
    quantia = float(input("digite a quantidade de dinheiro gerado no ano %d:  "  % (i+1)))
    anos.append(quantia)
  Solution = np.irr(anos)
  print('o resultado é: %.6f' % Solution)


opc = 1
while opc < 6 or opc > 0:
  print(
    "1 - valor futuro\n2 - valor presente\n3 - valor presente líquido\n4 - payback\n5 - TIR\n6 - sair"
  )
  opc = int(input("opção: "))
  if opc == 1:
    valor_futuro()
  if opc == 2:
    valor_presente()
  if opc == 3:
    valor_presente_liquido()
  if opc == 4:
    paypay()
  if opc == 5:
    TIR()
  if opc == 6:
    exit()
