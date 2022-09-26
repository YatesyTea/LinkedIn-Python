my_list = [n for n in range (1,11)] # Create list within ranges granted.
my_list = [n*n for n in range (1,11)] # Adding a change before adding into list.
my_list = [n*n for n in range (1,11) if n%2==0] # Adding a control statement to restrict additions.
print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

names = ['Sam', 'Ben', 'Dan', 'Hammod', 'Dylan', 'Farah']
roles = ['Top', 'Jgl', 'Mid', 'Bot', 'Sup', 'Sub']

my_dict = {name:role for name, role in zip(names, roles) if roles != 'Sub'}
print(my_dict)

nums = [1,1,1,1,1,2,2,2,2,2,2,5,5,5,4,4,4,4,4,7,7,7,7,8,8,8,9,9,9,9,4,4,4,4]
my_set = {x for x in nums}
print(my_set)

# Look at generators and generator expressions at a different time.
