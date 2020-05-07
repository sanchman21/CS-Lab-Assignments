import array as myarray
import time
import matplotlib.pyplot as plt
import sys
print("Enter loop value : ",end="" )
input_value= input()
temp=myarray.array('i',[2,3,5,7,8,9])
array_size=sys.getsizeof(temp)
block_size = sys.getallocatedblocks()
total_time_array = []
arr_len = []
print ("initial Allocated List size: ", sys.getsizeof(arr_len))
print("Array Size and Block Size before the execution : " , array_size, block_size )
start_time=time.time()
for run_loop in range (0,int(input_value),1) :
    arr_len.append(len(temp))
    for k in range(0,10000) :
        t=0
    for j in range(1,5) :
        temp.append(run_loop+j)
    end_time=time.time() #captures starting time
    total_time= round((end_time-start_time),7)
    total_time_array.append(total_time) #captures total execution time
    run_loop += run_loop
array_size =sys.getsizeof(temp)
print("Total time=",total_time)
print(total_time_array)
print("Final list size: ", sys.getsizeof(arr_len))
print("Array Size and Block Size after the execution : ", array_size,block_size)
s=total_time_array #execution time
p=arr_len #array size
plt.plot(p,s) #plot the graph ( x axis = array size, y axis = execution time)
plt.show()
print(p,s)