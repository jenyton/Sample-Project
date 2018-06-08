result=(lambda x,y:x+y)(5,4)
print result

def square(x): return x**2

res=square(4)
print res

sq_lambda = lambda x : x**2
print sq_lambda(5)

mynums = [1,2,3,4,5]

print list(map(lambda x : x**2,mynums))

print list(filter(lambda num : num%2==0,mynums))

