x = lambda x : x*10

print(x(8))

def myfunction(n):
    return lambda x : x * n


payload = myfunction(6)

print(payload(8))