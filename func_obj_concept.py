def say_hello():
	print "Hello !!"

say_hello()
check=say_hello
check()

print "Deleting the function say_hello()"
del say_hello
###Function can be used as an object and that can be passed to another object
print "Calling the deleted function using the assigned word"
check()
