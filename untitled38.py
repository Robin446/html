from tkinter import *

root = Tk()
root.title("base")
root.geometry("600x300")

lab = Label(root,text="Enter the number: ")
lab.pack()
inp = Entry(root)
inp.pack()
lab2 = Label(root)
lab2.pack()

def getnum():
    inp1 = inp.get()
    url= "https://api.whatsapp.com/send/?phone=91"+inp1+"&text=Namasteji"
    lab2["text"] = url
    print(inp1)
    
btn = Button(root,text="Click Me", command=getnum)
btn.pack()

root.mainloop()