def all_changes(a, k=0):
  n=len(a)
  if k >= n:
      print (a)
  else:
    for i in range(k, n):
      a[k], a[i] = a[i] ,a[k]
      all_changes(a, k+1)
      a[k], a[i] = a[i], a[k]

m=input().split()
all_changes(m)