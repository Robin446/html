from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
import os

root = Tk()
root.title("HTML")
root.geometry("650x650")

open1 =ImageTk.PhotoImage(Image.open("open.png"))
save1 =ImageTk.PhotoImage(Image.open("save.png"))
exit1 =(Image.open("play.jpeg"))
rs= exit1.resize((20,20), Image.ANTIALIAS)
play1= ImageTk.PhotoImage(rs)

label_file = Label(root,text="File Name")
label_file.place(relx=0.28,rely=0.03,anchor=CENTER)

inp = Entry(root)
inp.place(relx=0.46,rely=0.031,anchor=CENTER)

txt= Text(root,height =35,width=80)
txt.place(relx=0.5,rely=0.55,anchor=CENTER)

name = ""
def openfile():
    global name
    txt.delete(1.0,END)
    inp.delete(0,END)
    txt_file = filedialog.askopenfilename(title="open text file", filetyper=(("Text Files","*.html")))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    inp.insert(end,formated_name)
    text_file = open(name,'r')
    paragraph=ttxt_file.read()
    txt.insert(end, paragraph)
    txt_file.close()

def save():
    inp1231 = inp.get()
    file = open(inp1231+".html","w")
    data = txt.get("1.0",END)
    print(data)
    file.write(data)
    inp.delete(0,END)
    txt.delete(1.0,END)
    messagebox.showinfo("Update","Success")
    
def closewin():
    global name
    #webbrowser.open_new("file://" + file_path)
    webbrowser.open(name)
    
    
btn_FBI_OPENUP =Button(root,image=open1,command=openfile)
btn_FBI_OPENUP.place(relx=0.05,rely=0.03,anchor=CENTER)

save=Button(root,image=save1,command=save)
save.place(relx=0.11,rely=0.03,anchor=CENTER)

exit32 = Button(root,image=play1,command=closewin)
exit32.place(relx=0.17,rely=0.03,anchor=CENTER)

root.mainloop()