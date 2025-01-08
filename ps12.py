#que-1 Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same

try:
    with open("file1.txt") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("file2.txt") as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open("file3.txt") as f1:
        print(f3.read())
except Exception as e:
    print(e)

print('thank you')

#que-2 Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1,2,3,4,5,6,7]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)

#que-3 Write a list comprehension to print a list which contains the multiplication table of a user entered number.abs
#que-5 Store the multiplication tables generated in problem 3 in a file named Tables.txt.
n = int(input("enter num:"))

table = [n*i for i in range (1,11)]
print(table)

with open("file1.txt","a") as f:
    f.write(f"table of {n}: {str(table)}\n")

#que-4 Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
try:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    print(a/b)

except ZeroDivisionError as v:
    print("infinte")



