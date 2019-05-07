#g=list(map(int,input('Enter the value').split(' ')))
g=[23,3,-3,4,-2,-6,-7,3,7,-2,-24,-5,34]
count=0
f=len(g)
e=0
for i in range(0,f):
    if g[i]<0 and g[i+1]<0 and g[i+2]<0 and i>=e:
        count=count+1
        c=g[i]
        d=g[i+1]
        q=g[i+2]
        e=i+3
        print((c,d,q))
        if e==(f-1) or e==(f-2) or e==f:
            break
        
print('The pair of three conscutive :',count)
