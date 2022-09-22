# Comprehensions is something that I've struggled with since it's not available in quite a few other languages.
# This file I will work on that.
def genList(x):
    return list(range(x+1))

# List Comprehensions

# Simple function
a = genList(10)
a2 = [2* item for item in a]
print(a2)


