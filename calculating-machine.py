from tkinter import *

def yaz(x):
    s = len(login.get())
    login.insert(s,str(x))
    print(x)

calculus = 5
n1 = 0

def operations(x):
    global calculus
    calculus = x
    global n1
    n1 = float(login.get())
    print(calculus)
    print(n1)
    login.delete(0,END)

n2 = 0 
def calculate():
    global n2
    n2 = float(login.get())
    print(n2)
    global calculus
    result = 0
    if(calculus== 0):
         result = n1 + n2
    elif(calculus== 1): 
        result = n1 - n2
    elif(calculus== 2):
        result = n1 * n2
    elif(calculus==3):
        result = n1/n2
    login.delete(0,'end')
    login.insert(0,str(result))






window = Tk()
window.geometry("300x300+500+200")
window.configure(bg="#0830e0")
window.resizable(width="FALSE",height="FALSE")


login =Entry(font="Verdana 14 bold", width=15, justify=RIGHT)
login.place(x=20,y=20)

b = []

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",bg="#ff0a16",command=lambda x=i:yaz(x)))

counter = 0

for i in range(0,3):
    for j in range(0,3):
        b[counter].place(x=20+j*50,y=50+i*50)
        counter += 1 

operation = []

for i in range(0,4):
    operation.append(Button(font="Verdana 14 bold",width=2,bg="#046627",command=lambda x=i:operations(x)))

operation[0]['text'] = "+"
operation[1]['text'] = "-"
operation[2]['text'] = "*"
operation[3]['text'] = "/"


for i in range(0,4):
    operation[i].place(x=170,y=50+50*i)

zb = Button(text="0",font="Verdana 14 bold",bg="#046627",command=lambda x=0:yaz(x))
zb.place(x=20,y=200)

db = Button(text=".",font="Verdana 14 bold",bg="#046627",width=2,command=lambda x=".":yaz(x))
db.place(x=70,y=200)

eb =Button(text="=",fg="red",font="Verdana 14 bold",bg="#046627",command=calculate)
eb.place(x=120,y=200)



window.mainloop()