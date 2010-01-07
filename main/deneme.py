from Tkinter import*
import math
master=Tk()
master.geometry("256x180")
master.title("Azimut")
e1=Entry(master,justify=RIGHT, textvariable=float, width=10)
e1.grid(row=5,column=5, columnspan=5, rowspan=5, padx=15, pady=15)
e2=Entry(master,justify=RIGHT, textvariable=float, width=10)
e2.grid(row=5, column=10, columnspan=5, rowspan=5, padx=15, pady=15)
e3=Entry(master,justify=RIGHT, textvariable=float, width=10)
e3.grid(row=10, column=5, columnspan=5, rowspan=5, padx=15, pady=15)
e4=Entry(master,justify=RIGHT, textvariable=float, width=10)
e4.grid(row=10, column=10,columnspan=5, rowspan=5, padx=15, pady=15)

l1 = Label(master, text="Y1")
l1.grid(row=7, column=6)
l2 = Label(master, text="X1")
l2.grid(row=7, column=9)
l3 = Label(master, text="Y2")
l3.grid(row=12, column=6)
l4 = Label(master, text="X2")
l4.grid(row=12, column=9)

def azimut():
    y1=float(e1.get())
    x1=float(e2.get())
    y2=float(e3.get())
    x2=float(e4.get())
    
    a=(math.atan2(abs(y2-y1),abs(x2-x1)))*200/math.pi
    
    if (y2-y1)>0 and (x2-x1)>0:
        a=a
    elif (y2-y1)>0 and (x2-x1)<0:
        a=200 - a
    elif (y2-y1)<0 and (x2-x1)<0:
        a=200 + a
    elif (y2-y1)<0 and (x2-x1)>0:
        a=400 - a
    
    l5 = Label(master, text=round(a,5))
    l5.grid(row=15, column=10)


b=Button(master, height=3, width=10, text="Hesapla", command=azimut)
b.grid(row=15, column=7, padx=10, pady=10)
mainloop()
