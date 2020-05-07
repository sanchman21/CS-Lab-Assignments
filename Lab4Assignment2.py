#PROGRAM 1

class Stack :
    def __init__( self ):
        self._theItems = list()
# Returns True if the stack is empty or False otherwise.
    def isEmpty( self ):
        return len( self ) == 0
# Returns the number of items in the stack.
    def __len__ ( self ):
        return len( self._theItems )
# Returns the top item on the stack without removing it.
    def peek( self ):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]
# Removes and returns the top item on the stack.
    def pop( self ):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()
# Push an item onto the top of the stack.
    def push( self, item ):
        self._theItems.append( item )

# Main program
myStack = Stack() 
userprompt=' '
value = int(input(userprompt))
while value >= 0 :
    myStack.push(value)
    value = int(input(userprompt))
while not myStack.isEmpty() :
    value = myStack.pop()
    print( value )

#PROGRAM 2

Lq = queue.LifoQueue(maxsize=6)

print(Lq.qsize())

Lq.put(9)
Lq.put(1)
Lq.put(2)
print("Full: ", Lq.full(), "Size: ", Lq.qsize())
# Data will be accessed in the reverse order of that of Queue
print(Lq.get(),Lq.get(),Lq.get())
print("Empty: ", Lq.empty()) 

#PROGRAM 3

DeQ = collections.deque(["Mon","Tue","Wed"])
print (DeQ)
# Append to the right
print("Adding to the right: ")
DeQ.append("Thu")
print (DeQ)
# append to the left
print("Adding to the left: ")
DeQ.appendleft("Sun")
print (DeQ)
# Remove from the left
print("Removing from the left: ")
DeQ.popleft()
print (DeQ)
# Reverse the dequeue
print("Reversing the deque: ")
DeQ.reverse()
print (DeQ)

queue = []
# Adding elements to the queue
queue.append('m')
queue.append('n')
queue.append('o')
print("Initial queue")
print(queue)
# Removing elements from the queue
print("\nElements dequeued from queue")

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)