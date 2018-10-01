#A Loop Demo is a structure that allows us to run 
#a section of code a number of times. It is great for
#when we need to repeat a process. It is also great when
#we need to run trhough apattern

#To brand catagries of a loop
#Conditional Loop: This loops if something is true
#Counted loop: This loops a set number of times

print("0")
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")


print("****************")
#the general structure if a counted loopis
# Count: this is the variable we use to track 
#the number of times a loop runs
#Check: This is the boolean (true or false) satement we evaluate 
# to decide is to keep going
# Change: This is the change in the count that happens after
#each loop.each

#we use i in range loop
for i in range(0, 6 ,1):
	print(i)
#how would the above loop run
#would we recah line 27
#i = 0, 0 < 6, True RUN LOOP
#i = 1, 1 < 6, True RUN LOOP
#i = 2, 2 < 6, True RUN LOOP
#i = 3, 3 < 6, True RUN LOOP
#i = 4, 4 < 6, True RUN LOOP
#i = 5, 5 < 6, True RUN LOOP
#i = 6, 6 < 6, False EXIT LOOP AND MOVE ON

print("*******************")
print("wite a loop that will print out 7 to 104 inclusive")
for i in range(7, 105, 1):
	print(i)
print("*******")
print("write a loop that will print out even numbers from -22 to 134 inclusive")
for i in range(-22, 135, 2):
	print(i)

print("*********************")
print("We can count backwards as well. Python3 will assume the check is based on")
print("relative value of the count and check")
for i in range(3, 0, -1):
	print(i)

print("**********")
print("all numbers from 101 to 0 inclusive")
for i in range(101, -1, -1):
	#anything that is tabbed is the loop code block
	print(i)


s = "Fish food"
for i in range(0, 9, 1):
	print(i)

#Can you print s ount in reverse?
for i in range(len(s) -1,-1,-1):
	print(s[i])