s = "String"
print "Place my variable here: %s" %(s)

#floating point, minDigits.precision
#minDigits will add white space if not enough characters
#precision will pad with 0's to get to desire precision
print "Floating point number: %1.3f" %(13.145)

#%s uses str()
print "Convert to string %s" %(123)
#%r uses repr()
print "Convert to string %r" %(123)

print "First: %s, Second: %s, Third: %s" %('hi!', "two", 3)

#better to use .format, order doesn't matter then, and easier to use same variable
print "\nFirst: %s, Second: %s" %(2,2)
print "First: {x}, Second: {x}".format(x="inserted")
print "First: {x}, Second: {y}, Third: {x}".format(x="inserted", y = "two!")
