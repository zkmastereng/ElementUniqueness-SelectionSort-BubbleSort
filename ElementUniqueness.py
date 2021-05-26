#Element Uniquness

def el_un(array,n):
   flag = False
   while flag is not True:
    for i in range(0,n-2):
        for j in range (i+1,n-1):
            if array[i]==array[j]:
                print("True")
                found = True
            
            
                 

def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)*n

def selection(array):

    for i in range (0,len(array)):
        min_index=i
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index=j
        array[i],array[min_index] = array[min_index],array[i]




print(fact(5))
array=[7,9,6,1,0,8,9,5,6,7]
array2=[0,8,7,9,6,1231,564,78,8,21,32,67,89,32,65,4]
selection(array2)
print(array2)

def bubblesort(array):
    for i in range(len(array),1):
        for j in range(1,len(array)):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                #array[j],array[j+1]=array[j+1],array[j]



array3=[4,8,9,7,1,0,2,-4,6,5,7,-11,5,6,3]
array4=[1,2,3,4,5,6]
bubblesort(array3)
print("bubble: "+str(array3))
el_un(array3,15)
bubblesort(array4)
el_un(array4,6)