print('Введите число - ')
k= int(input())
def number (n):        
    if  n>0:
        print(n%10, end='')
        number(n//10)

number (k)