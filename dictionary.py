from tkinter import *
def dict():
 di={"Apple":"Fruit","Peacock":" Bird","Lion":" Animal","white":"Color"}
 a=ent.get()
 if a in di:
  res.config(text=di[a])
 else:
  res.config(text="not found")
root=Tk()
root.title("Dictionary")
root.geometry("500x400")
root.resizable(False,False)
root.config(bg="lightgrey")
lbl=Label(root, text= "DICTIONARY",fg= "black", font= ("Algerian 26 bold underline"))
lbl.place(x=150,y=20)
ent=Entry(root, font=("Arial 15"))
ent.place(x=150,y=90)
res=Label(root, text= " Meaning ",fg= "black", font= ("Arial 15 "))
res.place(x=150,y=150)
btn1=Button(root, text="SEARCH", fg="black", font=("Arial 15 "),command=dict)
btn1.place(x=150,y=200)
root.mainloop()