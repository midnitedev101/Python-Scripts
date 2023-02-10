# Binary Search

# Used for: Lists in sorted order such as alphabetical or numeric, does not work on unsorted list

def binary_search(list, item):  # function takes in 2 arguments: list where the item is to be searched for; and the item
    low = 0 # represents the index for the first element in the list (to keep track of which part of the list searched in)
    high = len(list) - 1    # represents the index for the last element in the list (to keep track of which part of the list searched in)

    while low <= high:  # loop condition as true while
        mid = (low + high) // 2  # divide the current length of the list by half to narrow down search (store it as mid index); use // operator instead of / to return integer rather than float
        # print(mid)
        guess = list[mid]   # mid index is used to represent the value in the list (as the current guess)
        if guess == item:   # if the guess is the same as the item in argument, then return the mid index
            
            return mid  # returns the index of the guess
        if guess > item:    # if the guess is higher than the item in the argument, disregard the items after the position of the guess value and guess value itself
            
            high = mid - 1  # set the current max index of the list as mid - 1 since the guess was too high (should be lesser than the current guess)
        else:    # if the guess is lower than the item in the argument, disregard the items before the position of the guess value and guess value itself
            
            low = mid + 1   # set the current min index of the list as mid + 1 since the guess was too low (should be greater than the current guess)
    return None # the item does not exist

list_one = [1,3,5,7,9]

print(binary_search(list_one, 3))   # returns 1 since 3 can be found on list[1]
print(binary_search(list_one, -1))  # returns None since -1 is not on the list

# Exercises:
# 1) Suppose you have a sorted list of 128 name, and you're searching through it with binary search. What's the max number of steps it would take?
# Given that: log (2) 128 = x ~ 2 ^ x = 128, 2 ^ 7 = 128
# Therefore max number of steps for a sorted list of 128 names is 7 (x = 7; x + 1 = 8)

# 2) Suppose you double the size of the list. What's the max number of steps now? 
# With 128 * 2 = 256
# Given that: log (2) 256 = x ~ 2 ^ x = 256, 2 ^ 8 = 256
# Therefore max number of steps for a sorted list of 256 names is 8 (x = 8; x + 1 = 9)

# 3) How about the max number of steps it would take for binary search to look for 8 elements?
# Given that: log (2) 8 = x ~ 2 ^ x = 8, 2 ^ 3 = 8
# Therefore max number of steps for a sorted list of 8 elements is 3 (x = 3; x + 1 = 4)

# 4) How about the max number of steps it would take for binary search to look for 1024 elements?
# Given that: log (2) 1024 = x ~ 2 ^ x = 1024, 2 ^ 10 = 1024
# Therefore max number of steps for a sorted list of 1024 elements is 11 (x = 10; x + 1 = 11)

# 5) How about the max number of steps it would take for binary search to look for 16 elements?
# Given that: log (2) 16 = x ~ 2 ^ x = 16, 2 ^ 4 = 16
# Therefore max number of steps for a sorted list of 16 elements is 5 (x = 4; x + 1 = 5)

# Additional Sources:
# 1) Why max number of steps add 1 when doing binary search?
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/running-time-of-binary-search