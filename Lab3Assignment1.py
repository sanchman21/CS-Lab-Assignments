#EXERCISE 1

a_list=[52,53,26,53,73,63,24,73,63,88,88]
def firstsecond_element(given_list):
    a=given_list
    a.sort(reverse=True)#reverse=true is writte so that list is sorted in descending order
    print(a)
    first=a[0]
    second=None 
    for element in a_list:
        if element != first:
            second=element
            return first,second
f,s=firstsecond_element(a_list)
print(f,s)

#EXERCISE 2

firstmatrix=[[1,2,3],[5,3,6],[3,7,5]]
secondmatrix=[[4,3,6],[5,3,6],[8,2,6]]
thirdmatrix=[[2,6],[4,8]]
def sumofdiagonal(matrixitems):
    sum=0
    for i in range(len(matrixitems)):
        sum += matrixitems[i][i]
    return sum
print("Sum of diagonal of first matrix =",sumofdiagonal(firstmatrix))
print("Sum of diagonal of second matrix =",sumofdiagonal(secondmatrix))
print("Sum of diagonal of third matrix =",sumofdiagonal(thirdmatrix))

#EXERCISE 3

list_items=["INDIA",500,"USA",6745,"ENGLAND",45.26]
str_items=[]
num_items=[]
for item in (list_items):
    if isinstance(item,int) or isinstance(item,float):
        num_items.append(item)
        print(num_items)
    elif isinstance(item,str):
        str_items.append(item)
        print(str_items)
print(str_items)
print(num_items)
str_asc_items=str_items.sort(key=str.lower)
print(str_asc_items)
str_des_items=str_items.sort(key=str.lower,reverse=True)
print(str_des_items)
num_asc_items=num_items.sort()
print(num_asc_items)
num_des_items=num_items.sort(reverse=True)
print(num_des_items)

#EXERCISE 4

my_list = ['p','r','o','b','l','e','m']
print('p' in my_list)
print('o' not in my_list)
for fruit in ('APPLE','MANGO','BANANA'):
    print("I LOVE",fruit )

#EXERCISE 5

my_tuple=('mouse',[3,6,5],(5,9,2,'keyboard'))
print(type(my_tuple[1]))
my_tuple[1][2]='monitor'
print(my_tuple)  
del my_tuple