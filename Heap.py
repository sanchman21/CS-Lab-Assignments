import heapq as h
list1 = []
first = input("Enter first element:\n")
h.heappush(list1, first)
second = input("Enter second element:\n")
h.heappush(list1, second)
third = input("Enter third element:\n")
h.heappush(list1, third)

print("Items in the heap:\n")
for i in list1:
	print(i)
print("The smallest item in the heap:\n")
print(list1[0])
smallest = h.heappop(list1)
print("Pop the smallest item in the heap \n")
print(smallest)

print("New heap:\n")
for j in list1:
	print(j)