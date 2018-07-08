##Global variable
name="Global name"

def outer_func():

	### Enclosing function variable
	name="I am variable of out func"

	def inside_func():
		### Local  Variable
		name = "I am variable of inside func"
		print name

	inside_func()

outer_func()

