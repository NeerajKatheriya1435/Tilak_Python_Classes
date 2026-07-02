
# import os

# for i in range(100):
#     os.mkdir(f"Day {i}")

# for i in range(100):
#     os.rename(f"Day {i}",f"MyFolder {i}")

# for i in range(100):
#     os.rmdir(f"MyFolder {i}")

# a=5

# def greet(name):
#     global a
#     a=3
#     print("Good Morning",name)
#     print(a)

# greet("Rohan")
# print(a)

# f=open("data.txt","r")

# print(f.read())

# print(f.readline())
# print(f.readline())

# f=open("rohan.txt","r+")
# f.write("Hello tilak kais eho")
# f.write("how are you \nnext tilak")
# f.write("\nMy name rohan")

# print(f.read())
# f.close()

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']

# f.writelines(lines)

# f.close()

# f = open('myfile.txt', 'w')
# inp1=input("Enter the text: ")
# lines = [inp1, 'line 2', 'line 3']

# for line in lines:
#     f.write(line + '\n')
# f.close()

# f = open('myfile.txt', 'r')

# f.seek(6)
# print(f.readline())
# print(f.tell())

# with open("data.txt","w") as f:
#     f.write("Hello Tilak")
#     f.truncate(5)

# def adTwoNum(num1,num2):
#     print(num1+num2)

# adTwoNum(5,8)

# sum=lambda a,b:a+b

# print(sum(5,3))

lis1=[4,7,3,9]

# map1=list(map(lambda x:x+5,lis1))
# print(map1)

# map1=list(filter(lambda x:x>5,lis1))
# print(map1)

# from functools import reduce
# list1=[2,5,6]
# print(list1)
# st=reduce(lambda a,b:a*b,list1)
# print(st)