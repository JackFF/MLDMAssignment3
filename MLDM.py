from tkinter import *

root = Tk()
root.title("Machine Learning & Data Mining")
root.geometry("450x335")

def printName():
    print("Stupid ass bitch I aint fucking with you")

def exitApplication():
    root.destroy()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

topLabel = Label(topFrame, text="This is an application that uses the C4.5 algorithm in Python. \nPlease select one of the following options:", font=(30))

topLabel.pack()

b1 = Button(bottomFrame, text="Use the owls.csv\ndata", width="15", height="15", font=(30))
b1.config(command=printName)

b2 = Button(bottomFrame, text="Upload your own\ndata files", width="15", height="15", font=(30))
b2.config()

b3 = Button(bottomFrame, text="Exit the application", width="15", height="15", font=(30))
b3.config(command=exitApplication)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

root.mainloop()
