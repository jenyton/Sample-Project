def hello(name="Jose"):
	print('The hello() has been executed')
	
	def greet():
		return "greet() inside hello()"
	def welcome():
		return "welcome() inside hello()"
	
	print "I am going to return a function"
	
	if name == "Jose" :
		return greet
	else :
		return welcome


a=hello()
##Calling a function inside a function by assigning the function to a variable
print "Function assignment"
print a
print a()
b=hello
print b
b()

def hi():
	return "Hi !!!"

def other(some_def_func):
	print "Other code runs here"
	print(some_def_func())


print ("\n\nCalling a function by passing another function as argument")
other(hi)

