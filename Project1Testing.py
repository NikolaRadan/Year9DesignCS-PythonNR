
#tkinker is a module (tool box) that holds code
#that you can use 
import tkinter as tk

#root variable that holds the information
#about the main window. That is the indow
#With the close, min, max buttons in the top left

def change(*args):
	print("running change")
	#Step 1: Grab value
	opt = var.get()
#These are multiple if statments so that tou can access
#Certain data bases aout stocks
	
	
	for i in range(0,len(OPTIONS),1):
		if (opt == OPTIONS[i]):
			print(OPTIONS_PRICE[i])


	'''
	if (opt == OPTIONS[0]):
		print("price: 31")
	elif(opt == OPTIONS[1]):
		print("price: 32")
	elif(opt == OPTIONS[2]):
		print("price: 33")
	elif(opt == OPTIONS[3]):
		print("price: 34")
	elif(opt == OPTIONS[4]):
		print("price: 35")
	elif(opt == OPTIONS[5]):
		print("Price 36")
	elif(opt == OPTIONS[6]):
		print("price: 37")
	elif(opt == OPTIONS[7]):
		print("price: 38")
	elif(opt == OPTIONS[8]):
		print("price: 39")
	elif(opt == OPTIONS[9]):
		print("price: 40")
	elif(opt == OPTIONS[10]):
		print("Price 41")
	elif(opt == OPTIONS[11]):
		print("price: 42")
	elif(opt == OPTIONS[12]):
		print("price: 43")
	elif(opt == OPTIONS[13]):
		print("price: 44")
	elif(opt == OPTIONS[14]):
		print("price: 45")
	elif(opt == OPTIONS[15]):
		print("Price 46")
	elif(opt == OPTIONS[16]):
		print("price: 47")
	elif(opt == OPTIONS[17]):
		print("price: 48")
	elif(opt == OPTIONS[18]):
		print("price: 49")
	elif(opt == OPTIONS[19]):
		print("price: 50")
	elif(opt == OPTIONS[20]):
		print("Price 51")
	elif(opt == OPTIONS[21]):
		print("price: 52")
	elif(opt == OPTIONS[22]):
		print("price: 53")
	elif(opt == OPTIONS[23]):
		print("price: 54")
	elif(opt == OPTIONS[24]):
		print("price: 55")
	elif(opt == OPTIONS[25]):
		print("Price 56")
	elif(opt == OPTIONS[26]):
		print("price: 57")
	elif(opt == OPTIONS[27]):
		print("price: 58")
	elif(opt == OPTIONS[28]):
		print("price: 59")
	elif(opt == OPTIONS[29]):
		print("price: 60")
	elif(opt == OPTIONS[30]):
		print("Price 61")
	#'''

#if (opt == OPTIONS_STOCKNAME[0]):
		#print("DO THIS")
	
	#elif(opt == OPTIONS_STOCKNAME[1]):
		#print("DO THAT")
	#elif(opt == OPTIONS_STOCKNAME[2]):
		#print("This Do")
	#elif(opt == OPTIONS_STOCKNAME[3]):
		#print("That Do")
	#elif(opt == OPTIONS_STOCKNAME[4]):
		#print("oof")




root = tk.Tk()


#List of strings 
#My list is called options there are 4 elements with index 0 to 3
#print(OPTIONS[2])
#First drop down menu
OPTIONS= [
	"American express Co",
	"Apple Co",
	"Boeing Co",
	"Caterpillar Inc",
	"Cisco Inc",
	"Cheveron Corp",
	"DowDuPont inc",
	"Exxon Mobil Corp"
	"Goldman Saches Inc",
	"Home Depot Inc",
	"International Business Machines Corp",
	"Intel Corp",
	"Johnson & Johnson",
	"Coca-Cola",
	"JPMorgan Chase",
	"McDonalds Corp",
	"3M Co",
	"Merck & Co",
	"Microsoft Corp",
	"Nike Inc",
	"Pfizer Inc",
	"Procter & Gamble Co",
	"Travelers Companies Inc",
	"Travelers Companies Inc",
	"UnitedHealth Group Inc",
	"United Technologies Corp",
	"Verizon Communications Inc",
	"Visa Inc",
	"Walgreens Boots Alliance Inc",
	"Walmart Inc",
	"Walt Disney Co",
]
OPTIONS_PRICE = [31,32,33,34,35]
#Trying to link with second menu
#CHANGE NAME TO LINK
OPTIONS_STOCKNAME = [
	"Price",
	"Dividend",
	"52 week high",
	"52 week low",
	"Market cap",

]
#Do not .pack after evr command but rather .grid 
#so you can place the commands in order
var = tk.StringVar(root)
var.set(OPTIONS[0])
#var.trace("w",change)

lab1 = tk.Label(root, text = "Stock")
lab1.grid(row = 0, column = 0)
dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8],OPTIONS[9],OPTIONS[10],OPTIONS[11],OPTIONS[12],OPTIONS[13],OPTIONS[14],OPTIONS[15],OPTIONS[16],OPTIONS[17],OPTIONS[18],OPTIONS[19],OPTIONS[20],OPTIONS[21],OPTIONS[22],OPTIONS[23],OPTIONS[24],OPTIONS[25],OPTIONS[26],OPTIONS[27],OPTIONS[28])
dropDownMenu.grid(row = 1, column = 0, padx = 50, pady = 50)

dropDownMenuB = tk.OptionMenu(root,var, OPTIONS_STOCKNAME[0],OPTIONS_STOCKNAME[1],OPTIONS_STOCKNAME[2],OPTIONS_STOCKNAME[3],OPTIONS_STOCKNAME[4])
dropDownMenuB.grid(row = 1, column = 1)
#Submit button
btn = tk.Button(root, text = "Submit", command = change)
btn.grid(row = 2, column = 0)




root.mainloop()






