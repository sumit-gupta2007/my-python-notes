#import numpy as np
#arr_2d=np.array([(1,2,3),
                # [4,5,6]])
#print(arr_2d.shape)
import numpy as np
#arr=np.array([(10,20,30),[40,50,60]])
#print(arr.size)
#import numpy as np
#arr_1d=np.array([1,2,3])
#arr_2d=np.array([[1,2,3],[4,5,6]])
#arr_3d=np.array([[[1,2],[3,4],[5,6],[7,8]]])
#print(arr_1d.ndim)
#print(arr_2d.ndim)
#print(arr_3d.ndim)
#import numpy as np
#arr=np.array([10,20,30.5,40])
#print(arr.dtype)
#import numpy as np
#arr=np.array([1.2,2.3,4.5])
#print(arr.dtype)
#int_arr=arr.astype(int)
#print(int_arr)
#print(int_arr.dtype)
arr=np.array([10,20,30])
#print(arr+5)
#print(arr*6)
#print(arr**2)
#aggregation function in c
#arr=np.array([10,20,30,40,50])
#print(np.sum(arr))
#print(np.mean(arr))
#print(np.min(arr))
#print(np.max(arr))
#print(np.std(arr))
#print(np.var(arr))
""""""
#array[Index] #1d array
#array[row,column] #2
#""""""
#import numpy as np
#arr=np.array([10,20,30,40,50])
#print(arr[0])
#print(arr[1])
#print(arr[-1])
#""""""""
#slicing
#array[start:stop:step]
#arr[start:end],start to end-1
#negative step,-1 reversed
#"""'"""
#import numpy as np
#arr=np.array([10,20,30,40,50,60,70])
#print(arr[1:5])
#print(arr[:4])
#print(arr[::2])
#print(arr[::-1])
# slicing indexing
#import numpy as np
#arr=np.array([10,20,30,40,50,60])
#print(arr[[0,2,4]])
#boolean masking conditions filtring
#import numpy as np
#arr=np.array([10,20,30,40,50,60])
#print([arr>25])
#reshape(rows,columns)specify the  new shape
#if dimension match
#import numpy as np
#arr=np.array([1,2,3,4,5,6])
#reshaped_arr=arr.reshape(2,3)
#print(reshaped_arr)
#.ravel()-> view
#.flatten()-> copy
#import numpy as np
#arr_2d=np.array([[1,2,3],[4,5,6]])
#print(arr_2d.ravel())
#print(arr_2d.flatten())
#ADVANCED IN NUMPY
#np.insert(array,index,value,asix=none)
#array-original array
#index-
#Value-
#axis-
#axis = 0, row-Wise
#1 column wise
#import numpy as np
#arr=np.array([10,20,30,40,50,60])
#print(arr)
#new_arr=np.insert(arr,2,100)
#print(new_arr)
#import numpy as np
#arr_2d=np.array([[1,2],[3,4]])
#print(arr_2d)

#insert a new row at index 1
#new_arr_2d=np.insert(arr_2d,1,[5,6],axis=1)
#print(new_arr_2d)
#import numpy as np
#arr=np.array([10,20,30])
#new_arr=np.append(arr,[40,50,60])
#print(new_arr)
#np.concatenate(array1,array2),axis=0
#axis 0 >vertical stacking
#axis 1 > horizontal stacking    

#import numpy as np

#arr1=np.array([1,2,3])
#arr2=np.array([4,5,6])
#new_arr=np.concatenate((arr1,arr2))
#print(new_arr)
#np.delete(array,index,axis=none)
#flattern array
import numpy as np
#arr=np.array([10,20,30,40,50,60])
#new_arr=np.delete(arr,0)
#print(new_arr)
#import numpy as np
#arr_2d=np.array([[1,2,3],[4,5,6]])
#new_arr_2d=np.delete(arr_2d,0,axis=0)
#print(new_arr_2d)
#stacking
#vertically
#horizontally

#vstack()row 
#hstack() column Wise

#import numpy as np
#arr1=np.array([1,2,3])
#arr2=np.array([4,5,6])

#print(np.vstack((arr1,arr2)))
#print(np.hstack(((arr1,arr2))))
#np.split()
#equal
#np.hsplit()
#np.vsplite()

#import numpy as np
#arr=np.array([10,20,30,40,50,60])

#print(np.split(arr,2))  
import numpy as np

#prices=np.array([100,200,300])//broadcasting method
#discount=10#scalar single value

#final_prices=prices-(prices*discount/100)
#print(final_prices)

#import numpy as np
#arr=np.array([100,200,300])#single value broadcasting
#result=arr*2
#print(result)
#import numpy as np
#matrix=np.array([[1,2,3],[4,5,6]])#2*3 matrix matching dimension
#vector=np.array([10,20,30])# 1d aarray
#result=matrix+vector
#print(result)
#import numpy as np
#arr1=np.array([[1,2,3],[4,5,6]]) #incomplete shape
#arr2=np.array([1,2])
#result=arr1+arr2
#print(result)

#import numpy as np # vectoriation  addition
#arr1=np.array([1,2,3])
#arr2=np.array ([4,5,6])
#result=arr1+arr2
#print(result)

#import numpy as np// vectoriation multiplied  
#arr=np.array([10,20,30])
#multiplied=arr*3

#print(multiplied)

#import numpy as np# handling missing value

#arr=np.array([1,2,np.nan,4,np.nan,6])
#print(np.isnan(arr))
  
  #not equal
#print(np.nan==np.nan)

#np.nan_to_num(array,nan=value) default=0

#import numpy as np #replaces
#arr=np.array([1,2,np.nan,4,np.nan,6])
#cleared_arr=np.nan_to_num(arr,nan=100)
#print(cleared_arr)

#np.isinf()10*1000s
#1/0


#import numpy as np// bollean value return

#arr=np.array([1,2,np.inf,4,-np.inf,6])
#print(np.isinf(arr))

#import numpy as np

#arr=np.array([1,2,np.inf,4,-np.inf,6])
#print(np.isinf(arr))

#cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=-1000)

#print(cleaned_arr)

#import pandas as pd
##read data frame csv into a data frame
#df=pd.read_csv("sencoding=")
#print(df)

cities=["delhi","pune","noida","chennai", "mumbai"]
heroes=[ "thor","ironman","captain  america","shaktiman"]


def print_len(list):
    print(len(list))

    print_len(cities)
    print_len(heroes)



