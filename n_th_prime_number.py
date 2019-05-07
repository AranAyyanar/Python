N=int(input('Enter the value'))
count=0
count1=0
for i in range(2,N*10):
    for j in range(1,N*10):
           if i%j==0:
               count=count+1
    if count==2:
        count1=count1+1
        count=0
        if count1==N:
            print(i)
            break
    else:
        count=0
