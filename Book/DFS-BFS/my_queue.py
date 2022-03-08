# queue - FIFO (First In First Out)

global my_queue
my_queue = []

def push(element):
    my_queue.insert(0, element) # new element becomes the first element in the queue

def pop() :
    try :
        deleted = my_queue.pop()
    except IndexError :
        deleted = "Empty Queue"
    return deleted
    
def show() :
    print(my_queue)

print("** q: stop")
print("1) push 2) pop 3) show")
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
    elif statement == "show":
        show()
