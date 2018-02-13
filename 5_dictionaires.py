#Values of dictionary can be any object
my_dict = {'k1':123, 'k2':3.5, 'k3':'string'}
print "my_dict= {x}".format(x=my_dict)
print "my_dict['k3'] = {x}".format(x=my_dict['k3'])
#can use objects of dictionary
print "my_dict['k3'].upper() = {x}".format(x=my_dict['k3'].upper())

#update value of dictionary
my_dict['k1'] = my_dict['k1'] - 120
print "my_dict['k1'] = my_dict['k1'] - 120 => {x}".format(x=my_dict)
print ""

#python has self math, using <op>=, k=k+1 => k+=1

d = {}
print "d = {x}".format(x=d)
d['animal'] = 'Dog'
print "d['animal'] = 'Dog' => {x}".format(x=d)
print ""
#nesting dictionaires
nested = {'k1': {'nestkey': {'subnestkey':'value'}}}
print "nested = {x}".format(x=nested)
print "nested['k1'] = {x}".format(x=nested['k1'])
print "nested['k1']['nestkey']['subnestkey'] = {x}".format(x=nested['k1']['nestkey']['subnestkey'])
print "nested['k1']['nestkey']['subnestkey'].upper() = {x}".format(x=nested['k1']['nestkey']['subnestkey'].upper())

print "\nMethods"
d = {'k1':1, 'k2':2, 'k3':3}
print "d = {x}".format(x=d)

#Order is not garaunteed, use ordereddict to retain order, covered later
print "d.keys() = {x}".format(x=d.keys())
print "d.values() = {x}".format(x=d.values())
print "d.items() = {x}".format(x=d.items())     #list of tuples
