# stack - LIFO (Last In First Out)

global my_stack
my_stack = []
def push(element) :
    my_stack.append(element)

def pop() :
    try :
        deleted = my_stack.pop()
    except IndexError :
        deleted = "Stack empty"
    return deleted

def show() :
    print(my_stack)

print("** q: stop")
print("1) push 2) pop 3) show")
print("Ex) push then element")
while True :
    statement = input()

    if statement == "q" :
        break
    elif statement == "push" :
        el = input("Enter the elememnt to push: ")
        push(el)
    elif statement == "pop" :
        print(pop())
    elif statement == "show" :
        show()