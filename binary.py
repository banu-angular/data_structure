def binary(arr,target):
    left=0
    right=len(arr) -1
    while left<=right:
        mid= (left+right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid -1
    return -1
arr=[1,2,3,4,5]
target=2
result=binary(arr,target)
if result!=-1:
    print("I found data in ",result)
else:
    print("I cannot find the data")
