"""Yuyang Wang
CS152 sectionB
project 10 Final project
12/6/2022
serve as "module" which can be imported into other files 
Call this file like this:
python3 statistics2.py
"""


def sum(nums):
    """Calculates the sum"""
    #set the result to 0
    result = 0
    #loop over the nums list
    for i in nums:
        result += i
    return result


def mean(nums):
    """Calculates the mean"""
    result = sum(nums)/len(nums)
    return round(result,0)


def std(nums):
    """Calculates the standard deviation"""
    #set the std0 to 0
    std0 = 0
    #loop over the elements in the nums
    for i in nums:
        std0 += ((i-mean(nums))**2)/(len(nums)-1)
    std = std0 ** 0.5
    return std

n =[1,2,4,45,5]
print(mean(n))


