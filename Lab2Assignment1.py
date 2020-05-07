#PROBLEM 1

s='BEAUTIFUL PALACE'
print(s[4:9])
print(s[:5]+s[5:])#It will print the whole string.
print(s[8:11:1])
FIRST_SIX_CHARACTERS=s[:6]
print(FIRST_SIX_CHARACTERS)
third_to_fifth_chars=s[2:5]
print(third_to_fifth_chars)


#PROBLEM 2

t='LEARN PYTHON'
slice_object1=slice(-1,-5,-1)
slice_object2=slice(1,6,-1)#This won't get printed.
slice_object3=slice(1,9,1)
print(t[slice_object1] ,t[slice_object2] ,t[slice_object3])


#PROBLEM 3

r='LEARNING IS FUN'
reversestring=r[::-1]
print(reversestring)
s1=r[2:8:2]
print(s1)
s2=r[8:1:-1]
print(s2)
s1=r[-4:-2]
s2=r[8:1:-2]
print(s1)
print(s2)
a='PYTHON'
a1=a[100:]#This won't get printed.
print(a1)
a2=a[2:50]#This will get printed till the index number 5.
print(a2)


#PROBLEM 4

str='PYTHON BOOK'
slice_str=slice(3)
print(str[slice_str])
slice_str=slice(1,6,2)
print(str[slice_str])


#PROBLEM 5

list1=['P','Y','T','H','O','N']
tuple1=('P','Y','T','H','O','N')
slice_object=slice(3)
print(list1[slice_object])
slice_object=slice(1,5,2)
print(tuple1[slice_object])
slice_object=slice(-1,-4,-1)
print(list1[slice_object])
slice_object=slice(-1,-6,-1)
print(tuple1[slice_object])
list1[0]='T'
print(list1[0])
tuple1[0]='T'#It will show error as tuple is immutable.
print(tuple1[0])