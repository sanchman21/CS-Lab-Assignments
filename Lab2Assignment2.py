#PROBLEM 1

import operator
a=7
b=6
print("addition =",end=" ")
print(operator.add(a,b))
print("subtraction =",end=" ")
print(operator.sub(a,b))
print("multiplication =",end=" ")
print(operator.mul(a,b))


#PROBLEM 2

a=26
b=6

print("true division =",end=" ")
print(operator.truediv(a,b))
print("floor division =",end=" ")
print(operator.floordiv(a,b))
print("exponentiation =",end=" ")
print(operator.pow(a,b))
print("modulus =",end=" ")
print(operator.mod(a,b))


#PROBLEM 3

a=33
b=23
if(operator.lt(a,b)):
    print("33 is less than 23")
else : print("33 is greater than 23")   
if(operator.le(a,b)):
    if(operator.lt(a,b)):
        print("33 is less than 23")
    else : print("33 is equal to 23")    
else : print("33 is greater than 23")  
a=33
b=33 
if(operator.eq(a,b)):
    print("33 is equal to 33")
else : print("33 is not equal to 33")     


#PROBLEM 4

a=535
b=364
if(operator.gt(a,b)):
    print("535 is greater than 364")
else : print("535 is less than 364")    
if(operator.ge(a,b)):    
    if(operator.eq(a,b)):
        print("535 is equal to 364")
    else : print("535 is greater than 364")    
else : print("535 is less than 364")    
a=535
b=535
if(operator.ne(a,b)):
    print("535 is not equal to 364")
else : print("535 is equal to 364")    