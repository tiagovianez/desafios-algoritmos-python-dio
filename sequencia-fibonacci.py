##Entrada: O arquivo de entrada contém um valor inteiro N (0 < N < 46).
##Saída:Os valores devem ser mostrados na mesma linha, separados por um espaço em branco.
# Não deve haver espaço após o último valor.

n = int(input())
t1 = 0
t2 = 1
print('{} {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
