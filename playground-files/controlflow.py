# One Liner If Statements

n = 5
fizzBuzz = 'FizzBuzz' if n % 3 == 0 and n % 5 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n
print(fizzBuzz)

# print(['FizzBuzz' if n % 3 == 0 and n % 5 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n for n in range(1,101)])

# While Loops using interesting things

from datetime import datetime

wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    pass
print(f'Waited enough time, seconds is now {datetime.now().second}')

# Using break
wait_until = datetime.now().second + 2
while True:
    if datetime.now().second == wait_until:
        print(f'Waited enough time, seconds is now {datetime.now().second}')
        break
print(' break only gets you out of the current while loop, if nested it does not get you out of the next layer.')

# Using continue
print('Continue is used as a pass however is usually done with an if statement.')
