
#tkinker is a module (tool box) that holds code
#that you can use 
import tkinter as tk

#root variable that holds the information
#about the main window. That is the indow
#With the close, min, max buttons in the top left

root = tk.Tk()

ent = tk.Entry(root)
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 0, column = 1)

label = tk.Label(root, text = "...")
label.grid(row = 1, column = 0, columnspan = 2)


#This is an EVENT PROGRAM this means
#a function is called when we "do something"
root.mainloop()