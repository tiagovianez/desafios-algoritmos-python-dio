#Entrada: A primeira linha contém um inteiro N (1 ≤ N ≤ 100).
#A segunda linha contém N inteiros T1, T2, ..., TN (0 ≤ Ti ≤ 20).

#Saída: Imprima uma linha contendo o número da pessoa que Theon deve dizer ser seu algoz.
#Se existe mais de uma resposta possível, imprima a menor.

N = int(input())
entrada = list(map(int,input().split()))
print(entrada.index(min(entrada)) + 1)