#пузырьковая сортировка
def sort_bubble (m):
    n=len(m)
    for i in range(n-1):
        for j in range(n-1-i):
            if m[j]>m[j+1]:
                m[j], m[j+1]=m[j+1], m[j]
    #print (m)
    return m


#сортировка marge (сортировка слиянием)
def sort_marge (L, R):
  nl=len(L)
  nr=len(R)
  i=j=0
  mas_sort=[]
  while i<nl and j<nr:
    if L[i]<=R[j]:
      mas_sort.append(L[i])
      #print('i=', i)
      #print('mas_sortL=', mas_sort)
      i=i+1
    else:
      mas_sort.append(R[j])
      #print('j=', j)
      #print('mas_sortR=', mas_sort)
      j=j+1
  mas_sort+=L[i:]+R[j:]
  #print('mas_sortall=', mas_sort)
  return mas_sort

def funk_segment(mas):
  n=len(mas)
  if n<=1:
    #print(mas)
    return mas
  else:
    L= mas[:n//2]
    R= mas[n//2:]
    #print(L, R)
    return sort_marge(funk_segment(L), funk_segment(R))


mas = list(map(int, input().split()))
print ('пузырьковая сортировка - ', sort_bubble(mas))
print('сортировка marge -', funk_segment(mas))