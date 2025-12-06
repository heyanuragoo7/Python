#INFORMATION

# List -> Mutable, Ordered, Allows Duplicates(Array)
# Tupple -> Immutable, Ordered, Allows Duplicates
# Set -> Mutable, Unordered, No Duplicates (Set Are Mutable but Elements Are Immutable)
# Dict -> Mutable, Unordered, Key-Value Pair

# list = [5,3,2,1,4]

# list.append(6)         #Add element at the end
# print(list)
# list.insert(3, 0)  #Insert element at specific index
# print(list)
# list.remove(6)      #Remove specific element
# print(list)
# list.pop(3)         #Remove element at specific index
# print(list)
# list.sort(reverse=True)  #Sort in Descending Order
# print(list)
# list.sort()             #Sort the list
# print(list)
# count = list.count(1)        #Count occurrences of an element
# print(count)

# tupple = (5)        #Single element considered as Ineger
# print(type(tupple))
# tupple = (5,)       #Single element tupple as Tupple
# print(type(tupple))

# tupple = (5,7,9,3,4,7) 
# print(tupple[5-1])
# tupple = (5,7,9,3,4) 
# print(tupple[1:3])
# print(tupple.index(9))   #Get index of an element
# print(tupple.count(7))   #Count occurrences of an element

# list = []
# movie1 = input("Enter first movie name: ")
# movie2 = input("Enter second movie name: ")
# movie3 = input("Enter third movie name: ")

# for i in {movie1, movie2, movie3}:
#     list.append(i)

# print("Your movies are:", list)


# list1 = [1,2,3,2,1]
# list2 = [1, "abc", "abc", 1]
# count = 0

# for i in range(len(list1)):
#     for j in range(len(list1)-i-1,len(list1)-i):
#         if(list1[j] == list1[i]):
#             count+=1
#         else: 
#             print("Not A Palindrome")

# if(count == len(list1)):
#     print("Palindrome")


# dict = {}
# print(type(dict))
# print(dict)
# dict["Name"] = "Anurag"
# print(dict)

# dicts = {
#     "Name": "Anurag",
#     "Age": 23,
#     "City": "Jaipur",
#     "list": [1,2,3,4,5],
#     "Tupple": (6,7,8,'9','10'),
#     1: "One",
#     "nested_dict": {    #Nested Dictionarty Allowed
#         "hey": "hello",
#         1: "You pressed One"
#     }
# }
# print(dict)
# print(dict["Name"])
# print(dict[1]) 
# print(dicts["nested_dict"][1]) #Nested Dict Access

# keys = list(dicts)  # allowed type conversion
# for i in range(len(keys)):
#     key = keys[i]
#     if type(key) == str:
#         print(dicts[key])

# print(dicts.keys()) #Dict Keys
# print(dicts.values()) #Dict Values
# print(dicts.items())  #Dict Items (Key-Value Pair)
# dicts.pop("Age")    #Remove Key-Value Pair
# print(dicts)

# print(dicts["City"])
# print(dicts.get("Cityw")) #If key not found, returns None instead of Error (Thats why we need Methods)

# dict = {}
# set = {1,2,2}
# dict1 = {}
# set1 = {} #This is considered as Dict not Set
# set1 = set() #Correct way to declare empty Set
# print(type(dict))
# print(set)
# print(type(dict1))
# print(type(set))
# print(type(set1))

# set = {5,5,5,5,5,5,1,1,1,1,1,4,4,4,4,4}
# set.add(2)
# set.add(2) #Duplicates Not Allowed
# set.add(3)
# set.remove(5)
# set.add((1,2,3))  #Immutable Elements Allowed (Tupple)
# set.remove(3)
# set.clear()
# set.pop() # Randomly pops
# set.add([1,2,3])  #Mutable(hashable) Elements Not Allowed (List, Dict)          /* Important */

# set.union()  #Combine Two Sets (No Duplicates)
# set.intersection()    #Common Elements in Both Sets

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.union(set2))
# print(set1)
# print(set1.intersection(set2))
# print(set1)