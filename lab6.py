import math


# Exercise 1: Computing the factorial ===============================
def iterative_factorial(n):
    i = 1
    if not isinstance(n, int):
        print('The number must be positive integer!')
        quit()
    elif n <= 0:
        print('The number must be positive integer!')
        quit()
    while n > 0:
        i *= n
        n -= 1
    return i


try:
    n = int(input("Please provide a positive integer: "))
except ValueError:
    print("Incorrect type")
except ZeroDivisionError:
    print("Can't divide by 0")
finally:
    print(iterative_factorial(n))


# Exercise 2: Recursive function to compute product of odd items in a list===
def odd_compute(ls=[]):
    n = 1
    i = 0
    if len(ls):
        while i < len(ls):
            n *= ls[i]
            i = i + 2
        return n
    else:
        print('List is empty!')


ls = [3, 5, 1, 2, 6, 3]
print(odd_compute(ls))


# Exercise 3: Detect vowels in phrases=====================================
def isvowel(sentences):
    vo = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    a = []
    for i in range(len(sentences)):
        if sentences[i] in vo:
            a.append(sentences[i])
    if not a:
        print('no vowel in these sentences')
        quit()
    return a


print(isvowel("Tom the rAt"))
print(isvowel("HeLlO wOrLd!"))
print(isvowel("gfdy"))


# Exercise 4: Write a Function to calculating the Future Value of an Ordinary Annuity=
def calculation(data):
    result = []
    for m in range(len(data)):
        c = data[m][0]
        i = data[m][1]/100
        n = data[m][2]
        fv = round(c * ((math.pow((1 + i), n)-1)/i), 3)
        result.append(fv)
    return result


data = [[2000, 5, 7],
        [3500, 5.5, 6],
        [5500, 6.5, 8]]
print(calculation(data))


# Exercise 5 (a): Find error in data stored in a nested-dictionary===========
xyzcompany_dict1 = {'fiscal_quarter1': {"Month": ["Jan", "Feb", "Mar"],
                                        "Income": [9900, 9346, 9000],
                                        "Saving": (7231.67, 3675, 2347)},

                    'fiscal_quarter2': {"Month": ["Apr", "May", "Jun"],
                                        "Income": [13400, 9789, 8690],
                                        "Saving": (9679.32, 786.56, 4359)},

                    'fiscal_quarter3': {"Month": ["Jul", "Aug", "Sep"],
                                        "Income": [13202.878, 8792.89, 8110.87],
                                        "Saving": (9679.32, 786.56, 4359)}}

xyzcompany_dict2 = {'fiscal_quarter1': {"Month": ["Jan", "Feb", "Mar"],
                                        "Income": [9900, 9346, 9000],
                                        "Saving": (7231.67, 3675, 2347)},

                    'fiscal_quarter2': {"Month": ["Apr", "May", "Jun"],
                                        "Income": [13400, 9789, 8690],
                                        "Saving": (9679.32, 786.56, 4359)},

                    'fiscal_quarter3': {"Month": ["Jul", "Aug", "Sep"],
                                        "Income": [13202.878, 8792.89, 8110.87],
                                        "Saving_q3": (9679.32, 786.56, 4359)}}


def comparsion(xyzcompany_dict1, xyzcompany_dict2):
    for count, value in enumerate(xyzcompany_dict1):
        for key in xyzcompany_dict1[value].keys():   # inter keys loop
            if xyzcompany_dict1[value].keys() != xyzcompany_dict2[value].keys():
                print('two internal keys below are different: ', xyzcompany_dict1[value].keys(), xyzcompany_dict2[value].keys())
                quit()
    print('Two dictionaries have the same keys.')


comparsion(xyzcompany_dict1, xyzcompany_dict2)


















