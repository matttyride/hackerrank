n = int(input())
arr = []
for _ in range(n):
    arr.append(str(input()))
    q = int(input())
    q_arr = []
    for _ in range(q):
        q_arr.append(str(input()))
        for query in q_arr:
            print(arr.count(query))
