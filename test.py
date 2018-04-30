func = lambda x: ",".join("'"+str(i)+"'" for i in x)
a=['apple','mango']
b=fun(a+('banana','grapes').split(","))
print b
