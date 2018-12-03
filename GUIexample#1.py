import tkinter as tk



root = tk.Tk()

#***************WIDGET1*************
#Three steps:
#1. Construct the object
#2. Configure it
#3. Pack the object(or use Graphing)
titleLabel = tk.Label(root, text = "Wow you actually did something with your life", font=("Comic Sans MS", 16))
titleLabel.grid(row = 0, column = 0, columnspan = 2)





#*******WIDGET2*******
output = tk.Text(root, height = 10, width = 50)
output.config(state ="disable")
output.grid(row=1,column=0, columnspan=2)





#**********WIDGET3********
word1Label=tk.Label(root, text="Word 1")
word1Label.grid(row=2, column=0)

word2Label=tk.Label(root, text="Word 2")
word2Label.grid(row=3, column=0)


word3Label=tk.Label(root, text="Word 3")
word3Label.grid(row=4, column=0)




#******WIDGET4*********
ent1=tk.Entry(root)
ent1.grid(row=2, column=1)

ent1=tk.Entry(root)
ent1.grid(row=3, column=1)

ent1=tk.Entry(root)
ent1.grid(row=4, column=1)



btnGo=tk.Button(root, text="submit")
btnGo.grid(row = 5, column=1)

#The mainloop command is creating and running the page
#Without this you cannot have a page displayed
root.mainloop()