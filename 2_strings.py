#use 's' or "s"

#from __future__ import print_function
#makes print a function
#print("Hello World")

s = "Hello World"
print s
print "Legth =", len(s)

print "\nIndexing"
print "s[0]=", s[0]
print "s[-1]=", s[-1]       #Last letter

print "\nSlicing"
print "s[1:]=", s[1:]
print "s[:3]=", s[:3]       #from start up to index 3
print "s[:]=", s[:]         #grab all
print "s[:-1]=", s[:-1]     #grab all but last
print "\n"

# String[start:end:step]
print "s[::2]=", s[::2]     #every other word
print "s[::-1]=", s[::-1]   #reverse string

#Strings are immutable, can't change elements
print "\n"
print s*10                #print string s 10 times

print "\n"
print s.upper()             #Capitalizes String
print s.lower()             #Lowercases string
print s.split('e')          #splits where first character occurrs
