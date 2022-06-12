def fibonacci(n):
    secuence = []
    a =1
    b=1
    if n==1:
        secuence.append(0)
    elif n==2:
        secuence.append(0,1)
    else:
        secuence.append(0)
        secuence.append(a)
        secuence.append(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            secuence.append(total)
    return secuence
print(fibonacci(100))