# Does a collection contain a specific element : lets say a list, we have the `in` to allow us check if an item
# is in a list
# Algorithms Concerns With The Best / Average / Worst Times to find an element
# 1. Best case: When the first element is the one we are looking for O(log n)
# 2. Avarage case: In a random list we must check 1/2 of the list, if not found we must check each remaining one O(log n)
# 3. Worse case: You have to check each one O(log n)
# *** Can we do better => Yes => Only if we add structure to the collection


# collection = [1,5,6,8,9,0,12,31,34,65,86,97,118]

# if 31 in collection:
#     print('I found 31 in list')

# if 400 not in collection:
#     collection.append(400)
#     print('I didnt find 400 in list')

# print(collection)

# Binary Array Search Algorithm
# Consider a phone book, with names and numbers for a country
# If you want to find a name, the phone book lists names alphabetically so thats pretty easy
# But what do you do if you want to find a number?
# You have to start from the beginning and go through to the end
# We can assume thats what the in operator in python does, it starts at the beginning and goes all the way till it finds a match
# **** The trick here from our dictionary example is it's easy to search for things when they are ordered
# So the first thing we need to do before we search is to order
# OBSERVATION: Searching through a phone book with 400 pages is not twice as hard as searching on with 200 pages
# You just divide the 400 into 2 and you have reduced the problem by half
# This is the fundamental basis for the Binary Array Aearch algorithm
# If you keep cutting the problem into half it's size you are making tremendous progress
# Compared to walking through an list one by one
# So if we have a 1000 elements in the list and you need to search each one at a time
# You may only need to do 10 searches because 2^10 = 1000
# NB: We are ASSUMING list is sorted

def bs_contains(myList, searchItem):
    length = len(myList)
    lowestPoint = 0
    highestPoint = length - 1

    while lowestPoint <= highestPoint:
        midpoint = (lowestPoint + highestPoint)/2
        if searchItem == myList[midpoint]:
            return midpoint
        elif searchItem < myList[midpoint]:
            highestPoint = midpoint - 1
        else:
            lowestPoint = midpoint + 1
    return -(lowestPoint + 1)

def insertInPlace(ordered, target):
    idx = bs_contains(ordered, target)
    if idx < 0:
        ordered.insert(-(idx + 1), target)