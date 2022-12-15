import numpy as np

def VetorB(A): 
  lista = []
  for linhas in range(len(A)): 
      soma = 0
      for colunas in range(len(A[linhas])):
            soma += A[linhas][colunas]
      lista.append(soma)
  return lista


def eGauss(A, b): 
  numTm = len(b) 
  for k in range(0, numTm-1):
      for linhas in range(k+1, numTm):
          m = A[linhas][k]/A[k][k]
          for colunas in range(k, numTm):
            A[linhas][colunas] = A[linhas][colunas]-m*A[k][colunas]
          b[linhas] = b[linhas]-m*b[k]
  return A, b


def subReversa(A, b): 
   numTm = len(b)
   x = numTm*[0]
   x[numTm-1] = b[numTm-1]/A[numTm-1][numTm-1]
   for k in range(numTm-2, -1, -1):
     s = 0
     for colunas in range(k+1, numTm):
       s = s + A[k][colunas]*x[colunas]
     x[k] = (b[k]-s)/A[k][k]
   return x


def mHills(a, z): 
    if a == z:
      return [[1 / (L + C + 1) for C in range(z)] for L in range(a)]
    else:
      print("matriz não valida")


numLinhas = int(input("insira o número de linhas da sua matriz: "))
numColunas = int(input("insira o número de colunas da sua matriz: "))
print("Sua matriz é do tamanho ",numLinhas ,"x",numColunas)
A = mHills(numLinhas, numColunas)
b = VetorB(A)

print("-------------------------- GAUSS ---------------------------------------\nSua matriz após o método de eliminação de gauss é :", eGauss(A, b))
print("------------------------- SUBSREVERSA ----------------------------------\nSua matriz após o método da substituição reversa é :",subReversa(A, b),"\n------------------------------------------------------------------------")