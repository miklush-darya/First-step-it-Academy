
def pr_number (k):
   a=[]
   for i in range(2, k+1):
      if  i%2>0 or i/2==1:
         if i%3>0 or i/3==1:
            if i%5>0 or i/5==1:
               if i%7>0 or i/7==1:
                  a.append(i)
   print ('простые числа - ', a)

print('введите число')
numbers=int(input())
pr_number (numbers)


#n = int(input())
#s = {i for i in range(2, n+1) if i not in [j for sub in [list(range(2*j, n+1, j)) for j in range(2, n//2)] for i in sub]}
#print(s)
