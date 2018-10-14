def bub_Sorter(arr):
    
    if(len(arr)==1):
        return arr
    
    
    swap=True
    while swap:
        swap=False
        temp=None
        for i in range(0,len(arr)):
            if(temp==None):
                temp=arr[i]
            elif(temp>arr[i]):
                arr[i-1],arr[i]=arr[i],arr[i-1]
                swap=True
                temp=arr[i]
            else:
                temp=arr[i]
    return arr


s=[7,2,5,1,4,3,2,1]
print bub_Sorter(s)
s.sort()
print s