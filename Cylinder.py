import tkinter as tk 
import math

#The definition is a function, which is a small collection of code
#How Python tells what code is associated with the definition is it 
#looks for tabs. Everything that is tabbed in is in the function

def submit():
	print("Submit Pressed")
	r = float (entr.get())
	h = float (entr.get())

	v = math.pi*r*r*h
	v = round (v,3)

	output.config(state="normal")
	output.insert(tk.INSERT,v)
	output.config(state="disabled")


#Your program starts at the first non-indented section
root =tk.Tk()
root.title("Volume of a Cylinder")
print("this program calculates the volume of")
print("a cylinder given radius and height")

labr = tk.Label(root, text="radius")
labr.pack()

#widget 
entr = tk.Entry(root)
entr.pack()
#end of widget
#Always pack() to finish constructing widget

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.pack()


root.mainloop()


#process





#output

print("END PROGRAM")