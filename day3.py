
# l1=[4,5,6,7,"Rohan",True,"Shivam",[4,5,6,7,9]]
# print(l1)
# print(type(l1))

# l1[3]=78

# print(l1[2])
# print(l1[4])
# print(l1)

# l1=[3,4,6,7,8,9,1]

# print(l1)
# print(l1[1:])
# print(l1[:])
# print(l1[::2])
# print(l1[-2])
# print(l1[-4:-1])

# l1=[i*i for i in range(1,11) if i>5]
# print(l1)

# str1="hello"

# if "9" in str1:
#     print("Present")
# else:
#     print("Not Present")

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if len(item)>4]
# print(namesWith_O)

# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# colors.reverse()
# newlist=colors.copy()
# colors.insert(2,899)
# print(colors)
# list2=[4,5,6,7]
# colors.extend(list2)
# print(colors)

# t1=(3,4,5,65,67,5,"Rohan",[4,5,6,3])

# t1=(3,4,5,65,67,5)

# t1=(12,4,2002)

# t1[2]=8999

# # l1=list(t1)
# l1.append(899)
# t1=tuple(l1)

# print(t1[3])
# print(t1)

# t1=(3,46,879)
# print(t1)
# print(type(t1))

name="Suman"
age=56

# str1="Hello my name is {1} and age is {0}"
# print(str1.format(name,age))
# print(str1)
# print(str1.format(age,name))
# print(f"My name is: {name} and age is: {age}")

# s1={4,5,6,8,8,4}
# print(s1)

# my_set = {56,"Rohan", 12,True,3, 54,"Hello"}

# my_set.add(90)
# my_set.add(90)
# my_set.remove(3)
# my_set.remove(2)
# my_set.add(34)
# my_set.remove(35)
# my_set.discard(35)
# print("Important line")

# my_set.pop()
# print(my_set)

# my_set = {56,"Rohan", 12,True,3, 54,"Hello"}
# myset={5,7,9,9,45,34}
# myset.update([6,5,6,7])
# print(myset)

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a | b) 
# print(a & b) 
# print(a - b) 
# print(a ^ b) 
# print(a.intersection(b))
# print(a.union(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))

# d1={
#     "Name":"Rohan",
#     "Age":78,
#     "City":"Hardoi"
# }
# d1["Age"]=899

# print(d1)
# print(d1["Age"])
# print(d1["City"])
# print(d1.get("Name"))

# for item in d1:
#     print(item)
# for item in d1:
#     print(d1[item])
# for item in d1.keys():
#     print(item)
# for item in d1.values():
#     print(item)
# for key,val in d1.items():
#     print(f"The key is {key} and value is {val}")

# d1.pop("Name")
# d1.popitem()
# del d1
# print(d1)

# age=int(input("Enter you age: "))

# # if(age<0):
# #     raise ValueError("Please Input Correct input")

# if(age>18):
#     print("You can drive the car")
# else:
#     print("You can drive the car")