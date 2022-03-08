from collections import deque

global qu
qu = deque()

def push(element) :
    qu.append(element)

def pop() :
    return qu.popleft()

def show() :
    qu.reverse()
    print(qu)


print("** q: stop")
print("1) push 2) pop")
print("Ex) push then element")
while True:
    statement = input()

    if statement == "q":
        break
    elif statement == "push":
        el = input("Enter the elememnt to push: ")
        push(el)
    elif statement == "pop":
        print(pop())

show()