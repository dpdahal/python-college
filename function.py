# def my_function():
#     return "hi"
#
#
# print(my_function())

#
# def take_value():
#     return [10, 10, 10]
#
#
# def calculate():
#     data = take_value()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p * t * r / 100
#
#
# def display():
#     print(calculate())
#
#
# display()


# def users(names):
#     print(names)
#
#
# users([1,2,3,45])

# arr

# def users(,**names*data):
#     print(names)
#     print(data)
#
#
# users(1,2,3,4,5,name='ram',age=20)

# n = int(input("Enter the number of items \t"))
# d = dict()
#
# for x in range(n):
#     key = input("Enter key\t")
#     d[key] = input("enter value\t")
#
#
# for key in d.keys():
#     print(d[key])
# args
# kargs

# def test(*name, **data):
#     print(type(name))
#     print(type(data))
#
#
# test()


# print(1,2,3,4,5,5,6,7,7,8)

# x = 10
#
#
# def test():
#     global x
#     x = x + 20
#     print(x)
#
#
# test()


# def res(n):
#     if n == 1:
#         return 1
#     else:
#         return n * res(n - 1)
#
#
# print(res(5))

# a = 5
# b = 4
#
# x = 0
#
# if a > b:
#     x += a
#     a = b
#     b = x
#
#
# print(a)
# print(b)


# a = lambda x, y: x + y


# def test():
#     def get(name):
#         return f"hello {name}"
#
#     print(get('hari'))
#
#


# a = test()('ram')
# print(a)
# a = test()
# print(a())

#
# def tet():
#     return  100
#
#
# def get():
#     print(tet())
#
# get()

# def get_doc(any_function):
#     def inner_function():
#         print(any_function.__doc__)
#
#     return inner_function
#
#
# @get_doc
# def add():
#     """
#     we are learning python function
#     """
#     return "welcome"
#
#
# add()
#
# def zero_check(any_function):
#     def inner_function(a, b):
#         if b == 0:
#             return "y is zero"
#         else:
#             return any_function(a, b)
#
#     return inner_function
#
#
# @zero_check
# def add(x, y):
#     return x + y
#
#
# print(add(20, 10))

#
# class Demo:
#     x = 10
#
#
#     def test(self):
#         obj = Demo
#         print(obj.x)
#
#
# obj = Demo()
# obj.test()


# import calculator
#
# print(calculator.add(20, 30))

# from calculator import add
# from introduction import add as a
#
# print(add(20, 20))
# print(a())


# from lib import *
#
#
# print(users.info())
# print(database.connection())

# import sys
# import os
#
# print(dir(os))

# print(os.getcwd())