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
print a
print a()

