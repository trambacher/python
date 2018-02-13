#python 2, does classic division, 3/2 = 1
from __future__ import division
#causes division to be similar to python 3

print "Division"
print "usually classic, imported module to make true"
print "3/2 =", 3/2
print "without module, to get true"
print "float(3)/2 =", float(3)/2

print "\nPower"
print "2**3 =", 2**3
print "4**5 =", 4**5
print "4**0.5 =", 4**0.5

print "\nVars"
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print "Taxes:", my_taxes

print .1+.2-.3
#does not result in 0
