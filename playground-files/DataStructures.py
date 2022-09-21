# DataStructures.py
# Just being used to help me understand list and dictionaries better.

a = [1,2,3]
print(a)

# List Slicing
b = [1,2,3,4,5]
c = b[:2] # This takes the first 2 elements.
print(c) 

d = b[0:6:2] # In this case we have [Start:End:Spacing] we can also leave Start and End blank if we're using 0th and last element in list.
print(d)

myList = list(range(100)) # Different way of initialising a list.
print(myList[::10])
print(myList[::-10]) # Just goes backwards in comparison to one above.

# List Modifications

## Append, Insert, Remove, Pop, Equiv vs. Copy.

a = [3,6,9]
a.append(12)
print(f"{a[0:3:1]} --> {a} with a.append(12)")

a.insert(3, 'hiya just added') # So position to insert, then content that you're adding.
print(a)


