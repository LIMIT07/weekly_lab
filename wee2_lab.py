import math

#Exercise1------

x1 = 'Python was created by Guido van Rossum a Dutch programmer.'
x2 = 'First version of Python 0.9.0 was developed in Centrum Wiskunde & Informatica (CWI) in the Netherlands in 1991.'
x3 = 'Python 3.0, was released on 3 December 2008.'

print(type(x1))
print(type(x2))
print(type(x3))
A = type(x1)==type(x2)==type(x3)==str
print(A)
print(x1,x2,x3)


#Exercise2(a)------
'''
FV is the future value of an ordinary annuity
C is the cash flow per period, C = 2000
i is the interest rate, i = 5%
n is the number of payments, n = 7
'''
C = 2000
i = 0.05
n = 7
FV = C * ((pow(1+i,n)-1)/i)  #pow(x,i) = x**i
print('FV=',FV)


#Exercise2(b)------
'''
PV is the present value of an annuity due
C is the cash flow per period
i is the interest rate
n is the number of payments
'''
C = 1000
i = 0.05
n = 5
PV = C * ((1-pow(1+i,-n))/i) * (i+1)
print('PV=',PV)

#Exercise3-------
# This code is incorrect - you need to fix it so that it provides the desired output!
divide_by = 2
subtract_by = 3

var = 1
var1 = var - subtract_by
print("Subtracting your value of var by ""+subtract_by+"" will give ", var1)

var2 = var1 / divide_by
print("Dividing var1 by ",divide_by," will give ",var2)

var3 = input("Please provide a real number between 0 and 1: ")
print("The ceiling of", var3, "is ",math.ceil(float(var3)))

var4 = 2
var5 = 3

print("Multiplying", var4, "by", var5, "will give", var4*int(var5))
print("Multiplying", var4, "by", var5, "will give", int(var4)*int(var5))
print("Multiplying", var4, "by", var5, "will give", float(var4)*float(var5))