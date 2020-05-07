#Problem 1

a=21
housenumber=100
print(a,housenumber)
#Created two variables a and housenumber and then assigned them some values. The values were then printed.

myhousenumber=housenumber#Assigning the value of housenumber to myhousenumber
b=a#Assigning the value of a to b
print(myhousenumber,b)#Printing myhousenumber and b
print(type(myhousenumber),b)#Printing the type of myhousenumber and b

ourhouse=int(housenumber)#Assigning the value of housenumber to ourhouse
c=int(b)#Assigning the value of b to c
print(ourhouse,c)#Printing the value of ourhouse and c
print(type(ourhouse),type(c))#Printing the type of ourhouse and c


#Problem 2

a=4324+32#integer addition
b=543-22#integer subtraction
c=(42*43)+65#integer multiplication then addition
d=b/a#integer division(will give float value)
e=c//b#integer division(will give int value)
f=c-b#integer subtraction
print(a,b,c,d,e,f)#printing the values


#Problem 3

m=0b11#this will convert the binary value of 11 to decimal
print(m)
n=0o20#this will convert the octal value of 20 to decimal
print(n)
p=0xF#this will convert the hexadecimal value of F to decimal
print(p)
numbersize=10**100#Taking a very large number
newnumbersize=numbersize*numbersize#Taking another large number, the multiplication of numbersize with numbersize
print(numbersize,newnumbersize)#printing numbersize and newnumbersize


#Problem 4

a=5.342-2.76
b=564.64
c=2.143e4
print(a,b,c)


#Problem 5

hey = "Hi"
print(hey)
print("how are you")
reply = input() #here, user will give input
print(reply)

#string operations
str1 ="hi "+"hello" #string concatenation
str2 ="WOW "*3 #string repetition
str3 = "Nice"[0] #indexing
str4 = "Nice"[-1] #from end
str5 = "Very Nice"[1:6] #slicing
str6 = len("good") #string length

print(str1 + "\n",str2 + "\n",str3 + "\n",str4 + "\n",str5 + "\n",str6)