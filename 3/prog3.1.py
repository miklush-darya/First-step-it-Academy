
def pr_number (k):
   num=[]
   for i in range(2, k+1):
      if  i%2>0 or i/2==1:
         if i%3>0 or i/3==1:
            if i%5>0 or i/5==1:
               if i%7>0 or i/7==1:
                  num.append(i)
   print ('простые числа - ', num)


def pr_number2 (k):
   numb=[]
   for i in range(2, k+1):
      for j in numb:
         if i%j == 0:
            break
      else:
         numb.append(i)
   print ('простые числа - ', numb)

print('введите число')
numbers=int(input())
pr_number (numbers)
pr_number2 (numbers)


#один из самых оптимизированнных способов является алгоритм Решето Эратосфена