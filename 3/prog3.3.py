# A - быки (угадано вплоть до позиции) B - коровы (угаданы числа на неверных позициях), 
 
x=list(str(input())) # загаданное число
y=list(str(input())) # угадываемое число

def bulls_cows(x, y):
    A=0
    B=0
    for k in range(len(x)):
        if x[k]==y[k]:
            A+=1
            B-=1
    for i in x:
        for j in y:
            if i==j:
                B+=1
    print(A, 'A', B,'B')

bulls_cows(x, y)