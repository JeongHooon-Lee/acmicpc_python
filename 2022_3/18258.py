import sys
from collections import deque

queue = deque([])

for i in range(int(input())):
    s = sys.stdin.readline().split()
    
    if s[0] == "push":
        queue.append(s[1])
    elif s[0] == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif s[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print("-1")
    elif s[0] == "size":
        print(len(queue))
    elif s[0] == "empty":
        if queue:
            print("0")
        else:
            print("1")
    elif s[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
