import random

# Exercise 1: Determine the min and max value===================
number1 = float(input('Please input number1:'))
number2 = float(input('Please input number2:'))
if number1 > number2:
    print("minimum number is:", number2,'and maximum number is:', number1)
elif number1< number2:
    print("minimum number is:", number1, 'and maximum number is:', number2)
elif number1 == number2:
    print('Two numbers are equal!')



# Exercise 2: Iterative statements/Loops===========================
interest1 = input('Please input 1 thing that you interested in(1/3):')
interest2 = input('Please input 1 thing that you interested in(2/3):')
interest3 = input('Please input 1 thing that you interested in(3/3):')
print([interest1, interest2, interest3])

interests = []
num_things = input('How many things you are interested in:')

for i in range(int(num_things)):
    interests.append(input('Thing you are interested in:'))
print(interests)


# Exercise 3: Iterative statements/Loops=========================
Liv = 'Liverpool'
Man = 'Manchester'
Edi = 'Edinburgh'
for i in range(1, 31):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0 and i % 5 != 0:
        print(Liv)
    elif i % 3 != 0 and i % 5 == 0:
        print(Man)
    else:
        print(Edi)


# Exercise 4: Create a nested dictionary by for loop===============
''' -------How to use enumerate()
                    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
                    >>> list(enumerate(seasons))
                    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
'''

department = ["Department1", "Department2", "Department3"]
cities = ["Hamburgh", "Barcelona", "London"]
countries = ["Germany", "Spain", "UK"]
dic = {}

for i, element in enumerate(department):
    dic[element] = {
        'city': cities[i],
        'country': countries[i]
    }
print(dic)


#Exercise 5: Simulate a coin toss=================================

head = 0
tail = 0
temp = -1
num_flip = -1
temp_num_flip = 0
mode = int(input('press 1 to enter equal probability mode, press 2 to enter modify probability:'))
if mode == 1:
    for i in range(100):
        result = random.randint(0, 1)
        if result == 1:
            print('head')
            head += 1
        else:
            print('tail')
            tail += 1
        if result != temp:
            num_flip += 1
            temp = result
            print('heads and tails have been flipped for ', num_flip, 'times so far.')

# Modify this code so that we have a biased coin; the user should be able to set the level of bias
if mode == 2:
    for i in range(1000):
        result = random.random()
        if result < 0.2:
            print('head')
            head += 1
            temp_num_flip = 1
        else:
            print('tail')
            tail += 1
            temp_num_flip = 0
        if temp_num_flip != temp:
            num_flip += 1
            temp = temp_num_flip
            print('heads and tails have been flipped for ', num_flip, 'times so far.')
else:
    print('Please enter the right number')

print('head is:',head,'tail is:',tail)
