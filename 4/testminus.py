
#if n<0:
def minus_number(N):
    if N <= 2:
        k=list(range(-N, 0))
        #print ('часть2 = ', k)
        return k
    else:
        num=[-N] #часть5
        d=minus_number(N-2)+num+number_f(N-2)+minus_number(N-1)# номера клеток с минусом (снимаем фишки)
        #print ('часть3 = ', d)
    return d

def number_f(N):
    #t=-1*(n-2) #для минус, если 1>=n>=4
    if N <= 2:
       # if n<0: #работает для 1>=n>=4, но тогда number_cell=number_f(N-1)+number_f(t)+g+number_f(N-2)
            #k=list(range(n, 0))
            #print(k)
            #return k
        m=list(range(1, N + 1))
        #print ('часть1=', m)
        return m
    else:
        g=[N] # часть4
        number_cell=number_f(N-1)+minus_number(N-2)+g+number_f(N-2) #номера ячеек
        #print(number_cell)
    return number_cell

print ('Введите число от 1 до 10: ')
n=int(input())
print('изменяемые номера клеток -', number_f(n))