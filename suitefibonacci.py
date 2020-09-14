def fibonacci(n):
    a=0
    b=1

    if n<=0:
        print('incorrect')
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b

print(fibonacci(9))



def fibonacci2(m):
    if m<=0:
        print('incorrect')
    elif m==1: 
        return 0
    elif m==2: 
        return 1
    else: 
        return fibonacci2(m-1)+fibonacci2(m-2)

print(fibonacci2(9))