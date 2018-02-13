#similar to lists but are immutable, can mix object types
t = (1,2,3)
print "t = {x}".format(x=t)
print "len(t) = {x}".format(x=len(t))

#indexing and slicing same as strings and Lists
print ""
print "t.index(2) = {x}".format(x=t.index(2))
print "t.count(1) = {x}".format(x=t.count(1))

t = (1,1,2,"three")
print "t = {x}".format(x=t)
print "t.count(1) = {x}".format(x=t.count(1))
print ""

t = (1,2,3)
print "t = {x}".format(x=t)

#Use tuples if you know you don't want the values to change
