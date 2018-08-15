from collections import deque
queue = deque(["Ram", "chandhu", "haari", "kesav"])
print(queue)
queue.append("nani")
print(queue)
queue.append("vicky")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)

'''output:
deque(['Ram', 'chandhu', 'haari', 'kesav'])
deque(['Ram', 'chandhu', 'haari', 'kesav', 'nani'])
deque(['Ram', 'chandhu', 'haari', 'kesav', 'nani', 'vicky'])
Ram
chandhu
deque(['haari', 'kesav', 'nani', 'vicky'])

'''