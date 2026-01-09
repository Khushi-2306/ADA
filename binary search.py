arr=list(map(int,input("enter sorted elements:").split()))
key=int(input("enter element to search:"))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        print("element found at position ",mid+1)
        break
    elif arr[mid]<key:
        low=mid+1
    else:
        high=mid-1
else:
    print("element not found")