def plus(x,y):
    z = generateZero()
    for i in range(0,300):
        z[i] = x[i] + y[i]
    return z

def product(x, y):
    inner = 0.0
    for i in range(0, len(x)):
        inner += x[i] * y[i]
    return inner

def cosvalue(x,y):
    return (product(x,y)/((product(x,x)**0.5)*(product(y,y)**0.5)))

def generateZero():
    x = []
    for i in range(0,300):
        x.append(0.0)
    return x
def generateI():
    x = []
    for i in range(0, 300):
        x.append(1.0)
    return x

def mean(x,size):
    for i in range(0,300):
        x[i] = x[i]/size
    return x