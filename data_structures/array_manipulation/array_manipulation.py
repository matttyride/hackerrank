#!/usr/bin/env python

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = [0] * (n+1)
    # print(arr)
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        arr[a-1] += k
        if ((b) <= len(arr)): arr[b] -= k;
    max_ = 0
    temp = 0
    for i in arr:
        temp = temp + i
        if (max_ < temp): max_ = temp;
    print(max_)
