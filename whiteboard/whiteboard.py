#  Move Element To End
# -----------------------

# You're given an array of integers and an integer. 
# Write a function that moves all instances of that integer 
# in the array to the end of the array and returns the array.

# The function should perform this in-place 
# (i.e., it should mutate the input array) and doesn't 
# need to maintain the order of the other integers.

# Sample input:
# array = [4,1,4,4,4,4,2,3,4]
# to_move = 4

# Sample Output:
# [1,2,3,4,4,4,4,4,4] # 1, 2, and 3 could be in any order

# array = [4,1,4,4,4,4,2,3,4]
# to_move = 4
# # helper function
# def swap(x,y, array):
#     array[x], array[y] = array[y], array[x]
# # pointers = 0
# # right_pointer = len(array)-1
# def swappoints(array, to_move):
#     left = 0
#     right = len(array)-1
#     while left < right:
#         if array[right] == to_move:
#             right -= 1
#         elif array[left] == to_move:
#             swap(left,right,array)
#             left += 1
#         else:
#             left +=1
#     return array
# print(swappoints(array, to_move))
    


#     Two Sum Problem
# Create a function that given a list of numbers (that are sorted) 
# and a target number as a sum, return the two index numbers that when added equal the target number
# Example Input: [2,3,4,11,15], target = 6
# Example Output: [0,2]

def two_sum(arr, target):
    
    for i  in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
    return -1
print(two_sum([2,3,4,11,15], 15))


def two_sum2(arr, target):
    left = 0
    right = len(arr)-1
    while right > left:
        if arr[right] + arr[left] > target:
            right -= 1
        if arr[right] + arr[left] < target:
            left += 1
        if arr[left] + arr[right] == target:
            return left, right

print(two_sum2([2,3,4,11,15], 15))

        

