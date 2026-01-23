from itertools import combinations
weights=[1,3,6,5]
values=[4,2,3,5]
capacity=10
n=len(weights)

best_values=0
best_subset=None
print ("subset\tTotal Weight\tTotal Value")
print("_"* 45)


for r in range (n+1):
    for subset in combinations (range (n), r):
       total_weight=sum(weights[i] for i in subset) 
       total_value=sum(values[i] for i in subset)

       subset_display="{" + " , ".join(str(i+1)for i in subset)+"}"

       if total_weight<=capacity:
           print(f"{subset_display:<15}{total_weight:<}${total_value}")
           if total_value > best_values:
               best_values=total_value
               best_subset=subset
           else:
               print(f"{subset_display:<15}{total_weight:<15}not feasible")


print("\n optimal solution:")
print("items selected:",{i+1 for i in best_subset})
print("maximum values:$",best_values)