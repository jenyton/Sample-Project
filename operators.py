##Checking the enumerate function
print "##Checking the enumerate function##"
word="abcde"
for item in enumerate(word):
	print item
for item in enumerate(word,10):
	print item

mylist=["apple","mango","pineapple"]

print list(enumerate(mylist))

##Checking the Zip function
print "##Checking the Zip function##"
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]
zipped=zip(name,roll_no,marks)

print "zipped value"
print zipped

print "Unzipped value"

n,r,m=zip(*zipped)
print n
print r
print m
