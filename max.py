n=int(input("enter number of elements:"))
arr=list(map(int ,input("enter elements").split()))
max_element=arr[0]
for i in range (1,n):
    if arr[i] >max_element:
        max_element=arr[i]
print("maximum element :",max_element)