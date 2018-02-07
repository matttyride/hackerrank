class Node:
    def __init__(self, index, head=None):
        self.index = index
        self.right = None
        self.left = None
        self.head = head

def create_b_tree():
    n = int(input().strip())
    # print(n)
    root = Node(1)
    head = root
    for c in range(n):
        a, b = int(input().split(' '))
        root.left = Node(a)
        root.right = Node(b)
        root.head =
    return

if __name__ == '__main__':
    swap_nodes()
