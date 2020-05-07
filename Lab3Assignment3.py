import pandas as pd 
import os


#EXERCISE 1

fruits={'apples': [100,250,150,200],
'oranges': [50,60,70,80],
'grapes': [20,30,40,50],
'bananas': [5,10,15,20]
}
sales=pd.DataFrame(fruits)
print(sales)
sales=pd.DataFrame(fruits, index=['KL','KR','TN','WB'])
print(sales)
print(sales.loc['TN'])
print(type(fruits))
print(sales.mean())
dict2=sales.to_dict()
print(dict2)


#ASSIGNMENT 1

def convert(lst):
    finaldict = { lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return finaldict 

myList1 = ['apples', 100,150,200,250]
print(myList1) 

enter=[]
print("Enter the number of elements you want: ",end="")
n=int(input())
print("Enter the elements: ")
for i in range (0,n):
    a=input()
    enter.append(a)   
print(convert(enter))


#ASSIGNMENT 2

print(os.getcwd()) 
path="C:/Users/ADMIN/Desktop/19BCS095/"
os.chdir(path)
print(os.getcwd()) 

#Using for loop compression method.

with open("emp1.txt") as txtfile:
    dictionary = dict(line.strip().split(None, 1) for line in txtfile)
print(" This is the dictionary using for loop compression method: ")
print(dictionary)
print(dictionary.values()) 
print(dictionary.keys())
print(dictionary.items()) 

fhand=open("emp1.txt","r")
for line in fhand:
    words=line.strip().split()
    print(words)

#Without compression of for loop and by using file operators.

newDir = {} 
with open("Emp1.txt") as f:
    for line in f:
        (key, val) = line.strip().split(' ',1)
        newDir[int(key)] = val
print(" This is the dictionary without For Loop compression method")
print(newDir)