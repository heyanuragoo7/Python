import pandas as pd
import numpy as np

# a = [1,4,3,2,5,6]
# def sortinglist(a):
#     a.sort()
#     print(a)
# sortinglist(a)

# a = [2,1,3,5,4,7]
# def swap(a, i, j):
#     temp = a[i]
#     a[i] = a[j]
#     a[j] = temp
# def sortinga(a):
#     for i in range(len(a)):
#         for j in range(i+1, len(a)):
#             if(a[i] > a[j]):
#                 swap(a,i,j)
# sortinga(a)
# print(a)

# with open('students.json', 'r') as f:
#     da = f.read()
#     print(da)

# with open('students.csv', 'r') as f:
#     data = f.read()
#     print(data)

# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
    
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

# s1 = Student("Alice", 20, 85)
# s1.display()

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def speak():
#         print("Animal Speaking")

# class Human(Animal):
#     def __init__(self, name):
#         self.name = name
    
#     @staticmethod
#     def speak():
#         print("Human Speaking")

# # obj = Human("John")
# # obj.speak()

# obj = Animal("John")
# obj.speak()

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def speak():
#         print("Animal Speaking")

#     @staticmethod
#     def speak():
#         print("AA Speaking")

# obj = Animal("John")
# obj.speak()

# ll = [2,4,6,4,6,1,1,2]

# ou = list(map(lambda x: x*x, ll))
# print(ou)

# o = list(filter(lambda x: (x & 1) == 1, ll))
# print(o)

# from functools import reduce
# o = reduce(lambda x, y: x + y, ll)
# print(o)

# li = [1,2,3,4,7,8,5,6,9]
# it = iter(li)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def gg():
#     yield 1
#     yield 2

# g = gg()
# print(next(g))
# print(next(g))

# with open("requirement.txt", 'r') as f:
#     data = f.read()
#     print(data)

# Context Manager Example
# class Student:
#     def __enter__(self):
#         print("Entering the context")
#         return self
    
#     @staticmethod
#     def done():
#         print("Doing something in the context")

#     @staticmethod
#     def done1():
#         print("Doing something in the context2")
    

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting the context")

# with Student() as s:
#     s.done1()

# li = [1,2,3,4]
# it = iter(li)

# print(next(it))
# print(next(it))
# print(next(it))

# def gen():
#     for i in li:
#         yield i
# for i in gen():
#     print(i)
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))

# import pandas as pd

# d = pd.read_csv('students.csv')
# b = pd.read_json('students.json')
# print(d)
# print(b)

