#1. WAP to remove a given item from the set.
s = {1, 2, 3, 4, 5}
item_to_remove = 3
s.remove(item_to_remove)
print("After removal:", s)

#2. WAP to create an intersection of sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print("Intersection:", intersection)

#3. WAP to create an union of sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print("Union:", union)

#4. WAP to find the maximum and minimum value in set.
num_set = {10, 2, 35, 7, 18}
print("Maximum:", max(num_set))
print("Minimum:", min(num_set))
