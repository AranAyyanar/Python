N=input()
k=input()
g=N.lower()
l=k.lower()
list1=[]
list2=[]
T="Yes"
for i in g:
  list1.append(i)
for i in l:
  list2.append(i)
list1.sort()
list2.sort()
for i in range(0,len(list1)):
  if list1[i]!=list2[i]:
    T="No"
    break
print(T)
