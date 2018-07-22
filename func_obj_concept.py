def say_hello():
	print "Hello !!"

say_hello()
check=say_hello
check()

print "Deleting the function say_hello()"
del say_hello
###Functions are the object that can be passed to another object
print "Calling the deleted function using the assigned word"
check()
