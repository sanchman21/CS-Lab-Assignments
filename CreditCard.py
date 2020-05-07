class CreditCard():
    def __init__(self,Customer_Name,Bank_Name,Bank_Balance,CreditCard_Number):
        self.Customer_Name=Customer_Name
        self.Bank_Name=Bank_Name
        self.Bank_Balance=Bank_Balance
        self.CreditCard_Number=CreditCard_Number
        self.c=None
    def charge(self,c):
        self.Bank_Balance=self.Bank_Balance + c
name= input("Customer Name:\n")
bankname= input("Bank Name:\n")
Bankbalance= int(input("Enter the Bank Balance:\n"))
CardNumber=int(input("Enter the credit Card no:\n"))
a=CreditCard(name,bankname,Bankbalance,CardNumber)
c=int(input("Enter the amount to be Charged:\n"))
a.charge(c)
print("Now the Balance is:",a.Bankbalance)