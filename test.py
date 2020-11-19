
def perm(a, k=0):
    n=len(a)
    if k >= n:
      print ('a в условии - ', a)
    else:
        for i in range(k, n):
            a[k], a[i] = a[i] ,a[k]
            print('a в цикле - ', a)
            perm(a, k+1)
            a[k], a[i] = a[i] ,a[k]
            print('a в цикле 2 замена - ', a)
            
            
  #print(a)

m=input().split()
perm(m)