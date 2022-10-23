import datetime

# Exercise 1: String Operations===================
x = "python interpreter and the extensive standard library are freely available " \
    "in source or binary form for all major platforms from the Python Web site, https://www.python.org/"

print(x.capitalize())
temp_x = '.'
print(x + temp_x)


# Exercise 2: Print following pattern by using string repeat operation===

y = '*hello* '
print(y)
print(y * 2)
print(y * 3)
print(y * 4)
print(y * 5)
print(y * 6)


# Exercise 3: Escape Characters in String================
x = "Your line spacing options aren\'t limited to the ones in the Line and Paragraph Spacing menu. \nTo adjust spacing with more precision, select Line Spacing Options from the menu to access the Paragraph dialog box.\nYou\'ll then have a few additional options you can use to customize spacing."
print(x)

# Exercise 4: String Formatting=========================
print('Hey! {0:s}, your account has been credited £ {1:9.3f}'.format("John", 5786.72478))


# Exercise 5: Datetime Formatting=======================
current_date = datetime.datetime.now()
print(current_date)

date_str = str(current_date)
print(type(date_str))

date_format = datetime.datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S.%f')
print(date_format)


# Exercise 6: User Input – input( )==================
'''
name = input('Please input your name:')
city = input('Please input your city:')
country = input('Please input your country:')
print('Nice to meet you',name,'from',city,',',country)
'''


# Exercise 7: Set operations========================

sentence1 = "Simple is better than complex ."
sentence2 = "Complex is better than complicated ."

sen1_set = set(sentence1.split(' '))
sen2_set = set(sentence2.split(' '))
print(sen1_set)
print(sen2_set)
print('The union between two sentences is:',sen1_set.union(sen2_set))
print('The intersection between two sentences is:',sen1_set.intersection(sen2_set))
print('The difference between two sentences is:',sen1_set.difference(sen2_set))

print(sen1_set.isdisjoint(sen2_set))
print(sen1_set.issubset(sen2_set))
print(sen1_set.issuperset(sen2_set))


# Exercise 8: Dictionary==========================
Company = {
  "Department1": {
    "name": "Data Governance",
    "Revenue": 20011.78
  },
  "Department2": {
    "name": "Electricity Pricing",
    "Revenue": 55451.901
  },
  "Department3": {
    "name": "Gas Pricing",
    "Revenue": 62728.99
  },
    "Department4": {
    "name": "Smart Meter",
    "Revenue": 41728.99
  }
}

print(Company.keys())
print('Keys of Department1 is', Company['Department1'].keys())
print('Keys of Department4 is', Company['Department4'].keys())
print(Company['Department2'])
print(Company['Department3'])
print('Name of Department2 is:', Company['Department2']['name'])
print('Revenue of Department4 is:', Company['Department4']['Revenue'])