items=[]
n=int(input("enter number of items:"))
for i in range(n):
    value=int(input("enter the value:"))
    weight=int(input("enter the weight:"))
    items.append((value,weight))
capacity=int(input("enter knapsack capacity:"))
items.sort(key=lambda x:x[0]/x[1],reverse=True)

total_value=0
for value,weight in items:
    if capacity>=weight:
        capacity-=weight
        total_value+=value
    else:
        total_value+=value*(capacity/weight)
        break
    print("maxium value:",total_value)
