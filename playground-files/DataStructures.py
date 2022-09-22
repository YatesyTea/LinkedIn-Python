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

# Sets
setA = {'a','b','c'}
print(setA)

# List to Set to List
a = ['a','a','b','c','c','c']
print(a)
a = list(set(a))
print(a) # Do keep in mind that Sets do not preserve order, so these can end up in random order.
# You can also not access set my position as sets are unordered, you instead access by element.

setA.add('d') # Like insert/append but doesn't add anywhere specific.
print(setA)

# Checking whether something is present in set.
print('a' in setA)
# Returns as a boolean value.
print('z' in setA)



