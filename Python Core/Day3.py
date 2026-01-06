# i = 1
# while i<=100:
#     print("Print No:", i)
#     i += 1

# num = int(input("Enter a number: "))
# val = num
# print(val)
# for i in range(9):
#     val = val + num
#     i += 1
#     print(val)

# for i in range(1, 11):
#     print(i * i)

# tupple = (1,2,3,4,5,6,7,8,9)
# num = int(input("Enter a number: "))

# for i in tupple:
#     if(i == num):
#         print("Found")
#         break


# 1. WHILE LOOP – Print numbers from 1 to 100
# i = 1
# while i <= 100:            # Loop runs until i becomes 101
#     print("Print No:", i)
#     i += 1                 # Increment i each iteration


# # 2. FOR LOOP – Print first 10 multiples of a number
# num = int(input("Enter a number: "))
# val = num                  # Start with the first multiple
# print(val)

# for i in range(9):         # We already printed the first one
#     val = val + num        # Add the number to get next multiple
#     print(val)


# # 3. FOR LOOP – Print squares of numbers from 1 to 10
# for i in range(1, 11):      # Loop from 1 to 10
#     print(i * i)            # Print square of i


# # 4. SEARCH IN TUPLE – Check if a number exists
# tupple = (1,2,3,4,5,6,7,8,9)
# num = int(input("Enter a number to search: "))

# for i in tupple:
#     if i == num:
#         print("Found")
#         break               # Exit loop as soon as match found

# 6. FOR LOOP – Factorial of a number
# num = int(input("Enter a number for factorial: "))
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print("Factorial:", fact)


# # 7. NESTED LOOP – Print a star pattern
# rows = int(input("Enter rows for star pattern: "))
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()                  # New line after each row


# # 8. LOOP WITH CONTINUE – Skip number 5
# for i in range(1, 11):
#     if i == 5:
#         continue            # Skip printing 5
#     print(i)


# # 9. LOOP WITH BREAK – Stop at 7
# for i in range(1, 11):
#     if i == 7:
#         break              # Stop loop when reaching 7
#     print(i)


# # 10. REVERSE LOOP – Countdown
# for i in range(10, 0, -1):  # Start, stop, step
#     print("Countdown:", i)


# # 11. PRINT TABLE OF ANY NUMBER
# table_num = int(input("Enter a number for table: "))
# for i in range(1, 11):
#     print(table_num, "x", i, "=", table_num * i)


# # 12. LOOP – Count even & odd numbers
# limit = int(input("Enter limit to check even & odd: "))
# even = 0
# odd = 0

# for i in range(1, limit + 1):
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even count:", even)
# print("Odd count:", odd)

# Some Brain Storming

# class abc:
#     __i = 10          # private class variable
 
#     def display(self):
#         return self.__i
 
#     def display2(self):
#         print("---------------", self.__i)
 
# obj = abc()
# obj.__i = 84
# print(obj.__i)
# print(obj.display())

class abc:
    __i = 10          # private class variable
 
    def display(self):
        return self.__i
 
    def display2(self):
        print("---------------", self.__i)

obj = abc()
obj._abc__i = 84
# print(obj.__i)
print(obj.display())
obj.display2()