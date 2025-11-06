import numpy as np
import pandas as pd

a=4
b=5

#  one dimensional array 

arr=[1,2,3,4,5]
np_arr=np.array(arr)
print(np_arr)

# multi dimensional array 
arr1=[1,2]
arr2=[3,4]
np_arr1=np.array([arr1,arr2])
print(np_arr1)

#  minimum dimensions
a1=[1,2,3,4,5,6,7,8]
np_arr2=np.array(a1,ndmin=3)
print(np_arr2)

# data types
a1=[4,5,6,7,8]
np_arr3=np.array(a1,ndmin=2,dtype=complex)
print(np_arr3)

# shapes and strides 
a2=[[1,2,3],[4,5,6]]
np_arr4=np.array(a2)
print("Array: ", np_arr4)
print("shape of the array: ",np_arr4.shape)
print("strides:", np_arr4.strides)
print(np_arr4.dtype)

# basic functions 

a3=np.zeros(3) # generates a array of zeros
a4=np.ones(4)  # generates a array of ones
a5=np.ones((4,3)) # generates multi dimenstional array 
print(a5)
print(a5.shape)
a6=np.ones((4,3), order='F') # Fortran-ordered array
print(a6)
print(a6.shape)

# np.arange(start,end,step)

print(np.arange(10))
print(np.arange(1,10))
print(np.arange(1,10,2))  

# evenly spaced values

print(np.linspace(1,10,endpoint=False))  # default num =50 
print(np.linspace(1,10, num=5,endpoint=True))
print(np.linspace(1,10, num=5,endpoint=False))






