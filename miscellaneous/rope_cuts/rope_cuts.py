#!/usr/bin/env python

"""
Let's say that you have a bunch of ropes of various lengths, and you want all of them to be the same length.
You have to find the shortest one, and cut all of the ropes to be that length.
Given an int array of rope lengths, return a new array of how much each rope should be cut.
Example:
> ropeCuts([2,2,5,1,6])
> [1,1,4,0,5]
"""

def ropeCuts(arr):
    arr_min = min(arr)
    cut_arr = []
    for i in arr:
        cut_arr.append(i-arr_min)
    return cut_arr

if __name__ == '__main__':
#    arr = [2,2,5,1,6]
    arr = list(input('Integers separated by spaces: ').split())
    arr = [int(i) for i in arr]
    print('original', arr)
    print('cut', ropeCuts(arr))
