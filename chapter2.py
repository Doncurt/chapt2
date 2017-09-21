# chapter 2 examples
item1, item2= input("Please enter 2 numbers")
plus= item1 + item2

print plus

for i in range (10):
    x= 3.9 *34
print x

for i in range(20):
    print i

print "this is a program that will print the entered percentage of interest youll earn in 10 years"

apr,principle=input("please inter an interest rate")

for year in range(10):
    principle = principle * (1+apr)

print principle
