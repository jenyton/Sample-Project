def check_even(num):
   return num%2 == 0

mynums = [1,2,3,4,5]

for item in filter(check_even,mynums):
   print item

print "Printing the result of filter function inside a list"
print list(filter(check_even,mynums))


