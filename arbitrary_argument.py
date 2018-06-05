##built in sum function (takes argument inside tuples)
print "Calling built in sum function without any argument"
print sum(())
print "Calling built in sum function with argument inside tuple"
print sum((10,20))

### *args

def myfunc(*args):
  print args
  print sum(args)

print "Calling myfunc using 4 arguments"
myfunc(10,20,30,40)
print "Calling myfun using 2 arguments"
myfunc(10,60)

### **kwargs

def newfunc(**kwargs):
   print kwargs


print "Calling kwargs function"
newfunc(name="David",age=23)

### combination of args and kwargs

def func1(*args,**kwargs):
   print args
   print kwargs
   print ("I would like {} {}".format(args[0],kwargs['food']))

print "Calling combination of args and kwargs function"
func1(10,20,30,fruit='apple',food='eggs',animal='dog')
