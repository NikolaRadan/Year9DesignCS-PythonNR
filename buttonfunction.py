import tkinter as tk

def onclick():
	print("Button clicked")


root = tk.Tk()
root.title("GUI Button")


#First step Create Element
btn1 = tk.Button(root, text="Button 1", command=onclick)
btn2 = tk.Button(root, text="Button 2")


#Last Step: Put on window
btn1.pack()
btn2.pack()

root.mainloop()