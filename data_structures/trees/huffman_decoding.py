"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    #Enter Your Code Here
    s_decode = ''
    head = root
    for i in s:
        x = int(i)
        if x == 1:
            head = head.right
        elif x == 0:
            head = head.left
        if head.right == None and head.left == None:
            s_decode += head.data
            head = root
    print(s_decode)
