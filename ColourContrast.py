import tkinter as tk 
import subprocess


#*******Command list**********
colorshm1bg = "red"
def change():
	print("in change")
	if checkVar1.get() == 1:
		for i in range(0,len(widget),1):
			widget[1].config(background = "blue")
	else:
		for i in range(0,len(widget), 1):
			widget[1].config(background = "red")



root = tk.Tk()
widget = []



#********variables*************
checkVar1 = tk.IntVar()
checkbox1 = tk.Checkbutton(root, var = checkVar1, text = "hello")
widget.append(checkbox1)
checkbox1.pack()


entry1 = tk.Entry(root, background = colorshm1bg)
entry1.pack()
widget.append(entry1)

label1 = tk.Label(root, text = "I am a label", background = "red")
label1.pack()
widget.append(label1)



root.mainloop()
