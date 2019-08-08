N=int(input())
list1=[" " for i in range(0,N)]
sum1=""
for i in range(len(list1)-1,-1,-1):
  for j in range(i,i-1,-1):
    list1[j]="*"
    for k in list1:
      sum1=sum1+k
    print(sum1)
    sum1=''
