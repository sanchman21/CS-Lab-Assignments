#Problem 1
#Creating a mysavings variable, then assigning it a value and then printng that value.
mysavings = 550
print(mysavings)

#Problem 2
#Create a variable balance and assign it the value 1.1. Then print out the amount of money saved after 7 years. The variable name should be result.
balance = 1.1
#result
result = 300*1.1**7
print(result)

#Problem 3
#Create a stirng named others with the value "compound interest".
others="compound interest"
#Create a boolean named profitable with the value false.
profitable=False
#Print others and profitable.
print(others)
print(profitable)

#Problem 5
#Calculate the product of mysavings and balance. Then store the value in a variable named firstyearbalance.
firstyearbalance = mysavings*balance
#Print firstyearbalance
print(firstyearbalance)
#See the data type of firstyearbalance.
print(type(firstyearbalance))
#Calculate the sum of balance and balance and store the value in a new variable named as doublebalance.
doublebalance = balance + balance
#Print doublebalance.
print(doublebalance)

#Problem 6
#Fix the code given in the problem by using str() function wherever necessary.
#Then convert the variable pi to float and store its value in a new variable named as pifloat.
#Fix this printout : print("My account had $ to begin with" + mysavings+ ".Now I have $" + balance + ". Wow, this is Awesome!!")
#Below is the fixed printout:
print("My account had $" +str(mysavings)+ " to begin with. Now I have $" +str(balance)+ ". Wow, this is Awesome!!")
pi="3.1415926"
print(type(pi))
#Conversion to float type.
pifloat=float(pi)
#Printing type pf pifloat.
print(type(pifloat))
