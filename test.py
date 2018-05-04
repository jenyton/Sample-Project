func = lambda x: ",".join("'"+str(i)+"'" for i in x)
a=['apple','mango']
b=func(a+("banana,grapes").split(","))
#b=("banana,grapes").split(",")
#b=func(a)
print b
