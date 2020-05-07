import math
import sys 

#PROGRAM 1

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

def insert(root, item): # Insert function definition
    temp = Node(item)
    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
    return root

def display(newlist): # Insert function definition
    while (newlist!= None) :        
        print(newlist.data, end = " ")
        newlist = newlist.next # next is a pointer

def arrayToList(arr, n): # Array to list conversion function definition
    newlist = None
    for i in range(0, n, 1):
        newlist = insert(newlist, list[i])
        print(sys.getsizeof(newlist)) # display new node size in bytes
    return newlist

# main program
if __name__=='__main__':
    list = [100, 2.5, "xyz", 40, 56.6]
    n = len(list)
    newlist = arrayToList(list, n)
    print("Linked list size in bytes : ", sys.getsizeof(newlist), "\nList Array size in bytes ", sys.getsizeof(list))
    display(newlist)    

#PROGRAM 2

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

def get_area(self):
    return self.length * self.breadth

r = Rectangle(160, 120)
print("\nArea of Rectangle: %s sq units" % (get_area(r)))