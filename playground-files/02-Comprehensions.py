# Comprehensions is something that I've struggled with since it's not available in quite a few other languages.
# This file I will work on that.
def genList(x):
    return list(range(x+1))

# List Comprehensions

# Simple Operations on Lists
print('######### Simple Operations ########## \n\n\n')
a = genList(10)
a2 = [2* item for item in a]
print(f'Converting from {a} --> {a2} \n\n\n')

b = genList(100)
print('[item for item in list if item % 10 == 0] \n Does this:')
b2 = [item for item in b if item % 10 == 0]
print(f'Converting from list of 0 to 100 --> {b2} using modulo and if statement.')

# Calling Functions
print('#### List Comprehensions With Functions ####')
# Strings are treated as lists in Python in most cases.
myString = "My name is Jimbob. I have no control over my baking skills. They fluctuate"

def cleanWord(word):
    return word.replace(',','').lower() # This replaces every instance of a , with empty string, and then sets it to lowercase.
print(myString)
print('Goes to')
cleaned = [cleanWord(word) for word in myString.split() if len (cleanWord(word)) < 4]
print(cleaned)
print("The generic form is [function for element in list if statement]")

# Nested List Comprehensions
separatedSentence = [sentence for sentence in myString.split(',')]
cleaned = [cleanWord(word) for word in myString.split()]
# Both of these above can be nested together into a one liner SO PYTHONIC!
fullyDone = [[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')]
print(fullyDone)

# Nested Loops
print([(x,y) for x in range(5) for y in range(5)])

''' This is equivalent to:

for x in range(5):
    for y in range(5):
        print(x,y)

So we're starting from the leaf of the structure and walking down the branch to the trunk.
'''

classrooms = [
    [
        {'name' : 'kid1', 'age' : 12, 'role': 'student'},
        {'name' : 'kid2', 'age' : 12, 'role': 'student'},
        {'name' : 'teacher', 'age' : 40, 'role': 'teacher'}],
    [
        {'name' : 'kid3', 'age' : 12, 'role': 'student'},
        {'name' : 'kid4', 'age' : 12, 'role': 'student'}
    ]    
]

print([person['name'] for classroom in classrooms for person in classroom if person['role'] == 'student'])

dateIdeas = [
        {'name':'Pottery Spinning Class', 'type': 'Learning', 'times': ['morning', 'afternoon'], 'price':5},
        {'name':'Swimming', 'type': 'active', 'times':['morning','afternoon'], 'price':1}
        ]

print(f"Date Idea Names: {[date['name'] for date in dateIdeas]}")

print(f"Names: {[date['name'] for date in dateIdeas]} Price: {[date['price'] for date in dateIdeas]}")

