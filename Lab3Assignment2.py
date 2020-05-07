#EXERCISE 1

import numpy as np
"""list1 = [25.20, 919.32, 900, 4526.65, 53, 235]
print("List :",list1)
converted_array = np.array(list1)
print("One-dimensional NumPy array: ", converted_array)

#EXERCISE 2

x = np.array([1,2,3], dtype=np.float64)
print("Size of the array: ", x.size)
print("Length of one array element in bytes: ", x.itemsize)
print("Total bytes consumed by the elements of the array: ",
x.nbytes)

#EXERCISE 3

print("Enter twelve integer values")
for i in range(int(input())
x=np.arange(10, 21).reshape(3,3)
print(x)

#EXERCISE 4

array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [0, 40]
print("Array2: ",array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))

#EXERCISE 5

x = np.array([[0, 10.5, 20.3,45.2,60.4,30.2], [20.5, 30.6,
40.9,50,2,56.9]])
print("first array: ")
print(x)
print("Values bigger than 20 =", x[x>20])
print("Their indices are ", np.nonzero(x > 20))

#EXERCISE 6

x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(type(x))
print(x.shape)
print(x.dtype)

#EXERCISE 7

a = np.array([[0, 1, 3], [5, 7, 9]])
b = np.array([[0, 2, 4], [6, 8, 10]])
c = np.concatenate((a, b), 1)
print(c) 

#EXERCISE 8

x = np.arange(16).reshape((4, 4))
print("Original array:",x)
print("After splitting horizontally:")
print(np.hsplit(x, [2, 6]))"""

#EXERCISE 9

x= np.arange(12).reshape(3, 4)
print("Original array elements:")
print(x)
print("Above array in small chuncks:")
for a in np.nditer(x, flags=['external_loop'], order='F'):
    
    print(a)

#EXERCISE 10

"""a1=np.array([1,2,3,4])
a2=np.array(['Red','Green','White','Orange'])
a3=np.array([12.20,15,20,40])
result= np.core.records.fromarrays([a1, a2, a3],names='a,b,c')
print(result[0])
print(result[1])
print(result[2])

#EXERCISE 11

x = np.array([10, 10, 20, 30, 30], float)
print(x)
print("Put 0 and 40 in first and fifth position of the above array")
y = np.array([0, 40, 60], float)
x.put([0, 4], y)
print("Array x, after putting two values:")
print(x)"""