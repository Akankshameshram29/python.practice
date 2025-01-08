#even number generator
def generator_exp(n):
    for i in range (1,n):
        if i%2 ==0:
            yield i

n = int(input("enter number"))
for value in generator_exp(n):
    print(value)

#square number

def square_generator(n):
    for i in range(1,n):
        yield i**2

n = int(input("enter number"))
for val in square_generator(n):
    print(val)

#count down generator

def countdown_generator(count):
    for i in range(count,0,-1):
        yield i

count = int(input("enter couter number"))
for val in countdown_generator(count):
    print(val)
