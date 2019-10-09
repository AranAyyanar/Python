def check(i,j):
    if (i==0):
        return j
    return check(j%i,i)

def main(j):
    out=1
    for i in range(2,j):
        if(check(i,j)==1):
            out=out+1
    return out

T=int(input())
for i in range(T):
    N_terms=int(input())
    for j in range(1,N_terms+1):
        print(main(j),end=" ")
    print()
