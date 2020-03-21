# 3 way partitioning or Dutch National Flag Algorithm

def DutchNationalFlagAlgorithm(arr):
    low = mid = 0
    high = len(arr)-1
    while(mid<=high):
        if(arr[mid]==0):
            if(arr[mid] != arr[low]):
                arr[mid],arr[low]=arr[low],arr[mid]
            low += 1
            mid += 1
        elif(arr[mid]==1):
            mid += 1
        else:
            if(arr[mid] != arr[high]):
                arr[mid],arr[high]=arr[high],arr[mid]
            high -= 1
    
arr = [1,0,0,2,1,2,0,2,1,2,0,2,1,1,0,0,2]
DutchNationalFlagAlgorithm(arr)
print(arr)