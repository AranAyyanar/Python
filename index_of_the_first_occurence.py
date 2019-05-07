g=list(map(int,input('Enter the values').split(' ')))
print(g)
x=int(input('Enter the value to find'))
c=len(g)
count=0
d=[]
for i in range(0,c):
    if g[i]==x:
        count=count+1
        d.append(i)
f=d[0]
print('the count present is ',count)
print('the index of the first occurence is ',f)
