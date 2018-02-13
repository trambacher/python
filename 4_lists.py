#Strings are a type of sequence
#Lists are most generic version of sequences
my_list = [1,2,3]
print my_list

#Can have different object types
my_list = ["String", 23, 1.2, 'o']
print my_list
print "len(my_list) = {x}".format(x=len(my_list))

print "\nIndexing"
my_list = ["one", "two", "three", 4, 5]
print "my_list[0] = {x}".format(x=my_list[0])

print "\nSlicing"
print "my_list[1:] = {x}".format(x=my_list[1:])
print "my_list[:3] = {x}".format(x=my_list[:3])

print "\nConcatentation"
#doesn't change my_list
print "my_list + ['new item'] = {x}".format(x=my_list + ['new item'])
my_list = my_list + ["permanent add"]
print "my_list = my_list + ['permanent add']: {x}".format(x=my_list)

#list can be any length of any types
print "\nMethods"
l = [1,2,3]
print "l = {x}".format(x=l)
l.append('append me!')
print "l.append('append me!') = {x}".format(x=l)
print "l.pop() = {x}\n=> l = {y}".format(x=l.pop(), y=l)
print ""
print "l.pop(0) = {x}\n=> l = {y}".format(x=l.pop(0), y=l)
new_list = ['a','e','x','b','c']
print "\nnew_list = {x}".format(x=new_list)
new_list.reverse()
print "new_list.reverse() => {x}".format(x=new_list)
new_list.sort()
print "new_list.sort() => {x}".format(x=new_list)

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1, l_2, l_3]
print "\nmatrix = {x}".format(x=matrix)
print "matrix[0] = {x}".format(x=matrix[0])
print "matrix[2][0] = {x}".format(x=matrix[2][0])

print ""
first_col = [row[0] for row in matrix]
print "first_col = [row[0] for row in matrix] = {x}".format(x=first_col)
