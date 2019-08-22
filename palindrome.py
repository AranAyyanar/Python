#palindrome
n=int(input('Enter the value'))
g=[0,0,0,0,0,0,0,0,0,0]
while n>0:
    r=n%10
    n=n//10
    g[r]=g[r]+1
print(g)
count=0
count1=0
for i in g:
    if i==1:
        count=count+1
    elif i%2!=0:
        count1=count1+1
if count>1 or count1>1:
    print('The given no is not a palindrome')
else:
    print('The given no is a palindrome')
