## Exibindo Números Pares
# Crie um programa que leia um número e mostre os números pares até esse número, inclusive ele mesmo.

n = int(input('Enter a number: '))
for number in range(1, n + 1):
    if number % 2 == 0:
        print(number)