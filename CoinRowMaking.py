def coin_row(c):
    n=len(c)

    F=[0]*(n+1)

    F[0]=0
    F[1]=c[0]

    for i in range(2,n+1):
        F[i]=max(c[i-1]+F[i-2],F[i-1])

    return F[n]

coins=[7,11,2,3,8,4]
result=coin_row(coins)
print("Maximum amount",result)    