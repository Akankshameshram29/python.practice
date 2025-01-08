#square calculation

square = lambda x:x**2

num = int(input("Enter a number"))
print(square(num))

#string length

sentences = input("enter string-")

length = lambda y:len(y)
print(length(sentences))

#even odd

number = int(input("enter a number to check if it is even or odd"))
result = lambda z: True if z%2==0 else False


print("Even" if result(number) else "odd")