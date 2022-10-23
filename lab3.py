import itertools
import math
# Exercise 1: Concatenate lists--------------

lista = [23,689,56,89,143,897]
listb = [56.8,89,898,45,897,569]
listc = [57,1,2,3,5,2,11]

print(lista + listb + listc)
print(sum([lista,listb,listc],[]))
concat_list = itertools.chain(lista,listb,listc)
concat_list = list(concat_list)
print(concat_list)



# Exercise 2: Flatten a nested list of integers and calculate statistical measures

a = [[4, 8, 6], [3, 2, 8], [2, 3, 3, 8]]
listA = sum(a,[])
print(listA)
print(' maximum in a is:',max(listA),'\n',
      'minimum in a is:',min(listA),'\n',
      'mean in a is:',sum(listA)/len(listA))
listA.sort()
print(listA)


#Exercise 3: Access elements in tuple
month1 = (('net earning', 125633.11),('cash flow', 7406.23))
month2 = (('net earning', 123711.12),('cash flow', 8000.458))
month3 = (('net earning', 32487.23),('cash flow', 5000.458))
total_net_earning = month1[0][1] + month2[0][1] + month3[0][1]
cashflow = month1[1][1] + month2[1][1] + month3[1][1]
print('total net earning is:',total_net_earning, '\n',
      'cash flow is:',cashflow)



#Exercise 4---------------------

list_a = list(range(1,100,10))
print(list_a)
list_b = list(range(300,500,30))
print(list_b)
listoflists = []  #empty list
listoflists.extend([list_a,list_b])
print(listoflists)


#Exercise 5------------------
i = 0.05    #interest rate
n = 5       #number of payments
t = 0
annuity = []
list_C = [1000,2300,750]
PV1 = round(list_C[0] * ((1-pow(1+i,-n))/i) * (1+i),3)
PV2 = round(list_C[1] * ((1-pow(1+i,-n))/i) * (1+i),3)
PV3 = round(list_C[2] * ((1-pow(1+i,-n))/i) * (1+i),3)
annuity.extend([PV1,PV2,PV3])
print('annuity:',annuity,'\n',
      'maximum value:',max(annuity),'\n',
      'minimum value:',min(annuity),'\n',
      'Present value of an Annuity for person1, person2, person3 is:',
      annuity[0],',',annuity[1],',','and',annuity[2],', respectively.')

'''---USE LOOP---
for t in range(len(list_C)):
      annuity.append(round(list_C[t] * ((1-pow(1+i,-n))/i) * (1+i),3))
'''