

#Step 1: open file
file = open("Apple.txt","r")
#Step 2: read all data as a string.  Note that the newlines will show up
strData = file.read()
print(strData)
#Step 3: Convert to a list
strList = strData.split("\n")
print(strList)

#Step 4: Assume first element is the largest
largest = strList[0]
smallest = strList[0]
#Step 5: Loop through list comparing each element ot largest.  If largest is smaller than element, replace largest
for i in range(0,len(strList),1):
	largest = max(int(largest),int(strList[i]))
	smallest = min(int(smallest),int(strList[i]))
	
print(largest)
print(smallest)