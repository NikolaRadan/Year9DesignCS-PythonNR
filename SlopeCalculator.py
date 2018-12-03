import os

print("Slope Calculator:")

os.system("say welcome to my slope Calculator")
#input
x1 = input("input x1: ")
x1 = int(x1)

y1 = input("input y1: ")
y1 = int(y1)

x2 = input("input x2: ")
x2 = int(x2)

y2 = input("input y2: ")
y2 = int(y2)

#process
rise = x2 - x1
run = y2 - y1

fSlope = rise/run

#output
print("Your slope is m = "+str(rise)+"/"+str(run))
print("Your slope as a decimal is "+str(fSlope))
os.system("say your slope as a decimal is "+str(fSlope))
print(rise)
print(run)




