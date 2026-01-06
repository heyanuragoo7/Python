# def sum(a,b):
#     return a + b
# print(sum(3,5))

# def factorial(n):
#     for i in range(1, n):
#         n = n * i
#     return n
# print(factorial(5))

# def printName(a):
#     if a == 0:
#         return
#     print("Hello")
#     printName(a - 1)
# printName(5)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(11))  # True

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# print(gcd(48, 18))  # 6

# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)
# print(lcm(4, 6))  # 12

# def is_sorted(lst):
#     return lst == sorted(lst)
# print(is_sorted([1, 2, 3]))  # True
# print(is_sorted([3, 1, 2]))  # False

# def print_hello(n):
#     if n == 0:
#         return
#     print("Hello")
#     print_hello(n - 1)
# print_hello(5)

# with open("Day.txt", 'w') as file:
#     data = file.write("Fonix Technologies")

# with open("Day.txt", 'rt') as file:
#     read_data = file.read()
#     print(read_data)

# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
#     def average(self):
#         return (self.marks1 + self.marks2 + self.marks3) / 3
    
# s1 = Student("Anurag", 85, 90, 95)
# print(s1.average())

# class Printgame:
#     def __init__(self, name):
#         self.name = name
#     @staticmethod
#     def hello():
#         print("Hello from Printgame class")

# pg = Printgame("Game1")
# pg.hello()

# class Bank:
#     balance = 100
#     def __init__(self, debt, credit):
#         self.debt = debt
#         self.credit = credit
#     @staticmethod
#     def net_balance():
#         return Bank.balance
#     def debt_amount(self):
#         self.balance -= self.debt
#         return self.balance
#     def credit_amount(self):
#         self.balance += self.credit
#         return self.balance

# result = Bank(20, 50)
# print(result.net_balance())
# print(result.debt_amount())
# print(result.credit_amount())

# class Comapany:
#     def __init__(self, company_name='C', founder='A'):
#         self.name = company_name
#         self.founder = founder

#     @staticmethod
#     def printf():
#         print("Founder is Found")
    
# class Cars(Comapany):
#     def __init__(self, company_name, founder, model_name, price, quantity):
#         super().__init__(company_name, founder)
#         super().printf()
#         self.model_name = model_name
#         self.price = price
#         self.quantity = quantity

#     def which_company(self):
#         print(self.founder)

# s1 = Cars('Lala', "Sunder", "Thar", 1999, 5)
# s1.which_company()

# class Company:
#     def __init__(self, company_name, founder, balance=0):
#         self.company_name = company_name
#         self.founder = founder
#         self.balance = balance
    
#     def printFounder(self):
#         print(self.founder)
#         print(self.balance)
#         print(self.company_name)

# class Product(Company):
#     def __init__(self, company_name, founder, balance, product_name, price, quantity):
#         super().__init__(company_name, founder, balance)
#         self.product_name = product_name
#         self.price = price
#         self.quantity = quantity

#     def print_products(self):
#         print(self.company_name)
#         print(self.founder)
#         print(self.balance)
#         print(self.product_name)
#         print(self.price)
#         print(self.quantity)

# class Booking(Product):
#     def __init__(self, company_name, founder, balance, product_name, price, quantity):
#         super().__init__(company_name, founder, balance, product_name, price, quantity)

#     def booking_product(self):
#         if self.quantity > 0:
#             self.quantity -= 1
#             self.balance += self.price
#             print("Product Booked!")
#         else:
#             print("Out of stock!")

# class Refund(Product):
#     def __init__(self,  company_name, founder, balance, product_name, price, quantity):
#         super().__init__(company_name, founder, balance, product_name, price, quantity)
#         self.product_name = product_name
#         self.quantity = quantity

#     def refundstart(self):
#         self.quantity += 1
#         self.balance -= self.price
#         print("Refund Successful!")

# p1 = Booking("Google", "Sundar", 0, "Pixel 9", 50000, 2)

# p1.booking_product()
# print("Quantity left:", p1.quantity)
# print("Balance:", p1.balance)

# p1.booking_product()
# p1.booking_product()

# p2 = Company("Google", "Sundar", 0)
# p2.printFounder()

# p3 = Product("Google", "Sundar", 0, "Pixel 9", 50000, 2)

# p3.print_products()

# class Cat:
#     def sound(self):
#         return "Meow"

# class Car:
#     def sound(self):
#         return "Vroom"

# for obj in (Cat(), Car()):
#     print(obj.sound())

# class Person:
#     def __init__(self, name):
#         self._age = 20       # protected
#         self.__salary = 5000 # private

#     def get_salary(self):
#         return self.__salary

# p = Person("Anurag")
# print(p.get_salary())
# print(p._age)
# # print(p.__salary)

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self):
#         return 3.14 * 5 * 5

# c = Circle()
# # cc = Shape()
# print(c.area())
# # print(cc.area)

# class Parent:
#     def show(self):
#         print("Parent method")

# class Child(Parent):
#     def show(self):
#         print("Child method")

# obj = Child()
# obj.show()