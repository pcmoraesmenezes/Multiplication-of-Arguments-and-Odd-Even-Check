#Criar uma função que multiplica todos os argumentos não nomeados recebidos
#Retorne o total para uma variavel e mostre o valor da variavel 
def mult(*arg):
    total = 1
    for i in arg:
        total = total * i
        print(f'O valor atual é {total}')
    print("O total é ", end='')
    return total
print(mult(1,2,3))
u = []
while(True):
    print("Informe o numero que deseja adicionar: ")
    u.append(int(input()))
    print(u)
    print("Digite 1 para verificar o resultado da multiplicação dos argumentos. Ou  digite 2 para colocar mais argumentos")
    i = int(input())
    if i == 1:
        print(mult(*u))
        break
    if i == 2:
        continue


#Cria uma função que verifica se o numero é impar ou par
#Retonar par ou impar

def even(num):
    if num % 2 == 0:
        return print("O numero é par")
    else:
        return print("O numero é impar!")
print("Olá digite um numero e vamos verificar se o numero é impar ou par! ")
aux = input()
even(int(aux))