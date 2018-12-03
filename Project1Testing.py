
#tkinker is a module (tool box) that holds code
#that you can use 
import tkinter as tk

#root variable that holds the information
#about the main window. That is the indow
#With the close, min, max buttons in the top left

def change(*args):
	print("running change")
	#Step 1: Grab value
	opt = var1.get()
	#These are multiple if statments so that tou can access
	#Certain data bases aout stocks

	
	for i in range(0,len(OPTIONS),1):
		if (opt == OPTIONS[i]):
			price = OPTIONS_PRICE[i]
			Dividend = OPTIONS_DIVIDEND[i]
			print(OPTIONS_PRICE[i])

	#NEXT STEP: based on the second option menu you will have decide what to do?
	#This is where you use some if statements. 
	print(var2.get())
	#Make an if statement for every var2 option and simply print out some text. 
	#Price if statment
	if var2.get() == "Price":
		textbox.config(state = "normal")
		textbox.insert(tk.END,var1.get()+" Price: "+str(price)+"\n")

		textbox.config(state = "disabled")

	#Divident If statment
	if var2.get() == "Dividend":
		textbox.config(state = "normal")
		textbox.insert(tk.END,var1.get()+" Dividend: "+str(Dividend)+"\n")

		textbox.config(state = "disabled")


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
OPTIONS_PRICE = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
#Trying to link with second menu
#CHANGE NAME TO LINK

OPTIONS_STOCKNAME = [
	"Price",
	"Dividend",
	"52 week high",
	"52 week low",
	"Market cap",
                                                      
]

OPTIONS_DIVIDEND = [70,71,72,73,74,75,76,77,78,79,80]







#Do not .pack after evr command but rather .grid 
#so you can place the commands in order
var1 = tk.StringVar(root)
var1.set(OPTIONS[0])

var2 = tk.StringVar(root)
var2.set(OPTIONS_STOCKNAME[0])

#var.trace("w",change)

lab1 = tk.Label(root, text = "Stock", font = "Kefa", background = "Royalblue1")
lab1.grid(row = 0, column = 0)
dropDownMenu = tk.OptionMenu(root,var1, OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8],OPTIONS[9],OPTIONS[10],OPTIONS[11],OPTIONS[12],OPTIONS[13],OPTIONS[14],OPTIONS[15],OPTIONS[16],OPTIONS[17],OPTIONS[18],OPTIONS[19],OPTIONS[20],OPTIONS[21],OPTIONS[22],OPTIONS[23],OPTIONS[24],OPTIONS[25],OPTIONS[26],OPTIONS[27],OPTIONS[28])
dropDownMenu.config(width = 40)
dropDownMenu.grid(row = 1, column = 0, padx = 30, pady = 30, )

lab2 = tk.Label(root, text = "Characteristic", font = "Kefa", background = "Royalblue1")
lab2.grid(row = 0, column = 1)


dropDownMenuB = tk.OptionMenu(root,var2, OPTIONS_STOCKNAME[0],OPTIONS_STOCKNAME[1],OPTIONS_STOCKNAME[2],OPTIONS_STOCKNAME[3],OPTIONS_STOCKNAME[4])
dropDownMenuB.config(width = 20)
dropDownMenuB.grid(row = 1, column = 1)


#Submit button
btn = tk.Button(root, text = "Select", command = change, font = "Kefa", foreground = "black", background = "honeydew4")
btn.grid(row = 2, column = 0, columnspan = 2,sticky = "NESW")



#textboxBOI
textbox = tk.Text(root, height = 10, width = 50, foreground = "grey")
textbox.grid(row = 3, column = 0, columnspan = 2)

#entire backround colour
root.config(background = "honeydew4")

#Chamge to night mode
#btn2 = tk.Button(root, text = "Night Mode", command = change, font = "Kefa", foreground = "black", background = "honeydew4", command= onclick1)
#btn2.grid(row = 4, column = 0, columnspan = 2)
#def onclick1():
	#print("hello")
	#root.config(background = "black")

root.mainloop()






