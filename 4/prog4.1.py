print('Введите число - ')
k= int(input())

def number (n):        
    if  n>0:
        number(n//10)
        print (n%10)
        
number (k)
