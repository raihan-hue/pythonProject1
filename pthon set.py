thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set3)
print(set2)
print(set1)

set1 = {"abc", 34, True, 40, "male"}

print(set1)

thisset = {"apple", "banana", "cherry"}

for y in thisset:
    print(y)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("aple" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
thisset.add("blue")
thisset.remove("cherry")
thisset.discard("banana")
thisset.pop()

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)