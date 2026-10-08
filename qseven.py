list1 = [10,20,30,40,50,60]
list2 = [30,40,50,60,7,80,90]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
only_list1 = set1 - set2
only_list2 = set2 - set1


print("Common elements:",common)
print("Elements only in list1:",only_list1)
print("Elements only in list2:",only_list2)
