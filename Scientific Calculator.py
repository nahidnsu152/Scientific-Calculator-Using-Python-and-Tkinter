#!/usr/bin/env python
# coding: utf-8

# In[22]:


from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background = "#3BC69B")
root.resizable(width=False, height =False)
root.geometry("472x541+0+0")

calc = Frame(root)
calc.grid()  

class Calc:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        
    def numberEnter(self,num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
            
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else: 
            self.total = float(txtDisplay.get())
            
            
    def display(self,value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
    
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
    
    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
    
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
        
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0
            
    def MathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
    
    def Squart(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def Cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def Cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def Tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def Tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)        

    def Sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def Sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def Log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
        
    def Exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def Expm(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def Lgmma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def Degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def Log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def Log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def Log1P(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)        
        
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
        
    def aSinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)
        
    def aCosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)
        
        
added_value = Calc()
 
txtDisplay = Entry (calc, font = ("arial",20,"bold"), bg="#23A199", bd=18, width=29, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i = 0
btn = []

for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6, height=2, font=("arial",20,"bold"), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
        i+=1
        
btnClear = Button(calc, text= chr(67), width=6, height=2, font = ("arial",20,"bold"), 
                  bd=4, bg="#23A199",command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)
btnAllClear = Button(calc, text= chr(67)+chr(69), width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199",command=added_value.All_Clear_Entry).grid(row=1, column=1, pady=1)
btnSq = Button(calc, text= "√", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Squart).grid(row=1, column=2, pady=1)

btnDiv = Button(calc, text= "/", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command = lambda: added_value.operation("divide")).grid(row=1, column=3, pady=1)
btnMul = Button(calc, text= "*", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command = lambda: added_value.operation("multi")).grid(row=2, column=3, pady=1)
btnSub = Button(calc, text= "-", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command = lambda: added_value.operation("sub")).grid(row=3, column=3, pady=1)
btnAdd = Button(calc, text= "+", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command = lambda: added_value.operation("add")).grid(row=4, column=3, pady=1)


btnPM = Button(calc, text= "+/-", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.MathsPM).grid(row=5, column=0, pady=1)
btnZero = Button(calc, text= "0", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command = lambda: added_value.numberEnter(0)).grid(row=5, column=1, pady=1)
btnDot = Button(calc, text= ".", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command = lambda: added_value.numberEnter(".")).grid(row=5, column=2, pady=1)
btnEq = Button(calc, text= "=", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

btnPi = Button(calc, text= "π", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.pi).grid(row=1, column=4, pady=1)
btnCos = Button(calc, text= "Cos", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Cos).grid(row=1, column=5, pady=1)
btnTan = Button(calc, text= "Tan", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Tan).grid(row=1, column=6, pady=1)
btnSin = Button(calc, text= "Sin", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Sin).grid(row=1, column=7, pady=1)


btn2Pi = Button(calc, text= "2π", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199",command=added_value.tau).grid(row=2, column=4, pady=1)
btnCosh = Button(calc, text= "Cosh", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.Cosh).grid(row=2, column=5, pady=1)
btnTanh = Button(calc, text= "Tanh", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.Tanh).grid(row=2, column=6, pady=1)
btnSinh = Button(calc, text= "Sinh", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.Sinh).grid(row=2, column=7, pady=1)

btnLog = Button(calc, text= "log", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Log).grid(row=3, column=4, pady=1)
btnExp = Button(calc, text= "Exp", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.Exp).grid(row=3, column=5, pady=1)
btnMod = Button(calc, text= "Mod", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command = lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)
btnE = Button(calc, text= "e", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.e).grid(row=3, column=7, pady=1)

btnLog2 = Button(calc, text= "log2", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Log2).grid(row=4, column=4, pady=1)
btnDeg = Button(calc, text= "deg", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.Degrees).grid(row=4, column=5, pady=1)
btnaCosh = Button(calc, text= "acosh", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.aCosh).grid(row=4, column=6, pady=1)
btnaSinh = Button(calc, text= "asinh", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, command=added_value.aSinh).grid(row=4, column=7, pady=1)


btnLog10 = Button(calc, text= "log10", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Log10).grid(row=5, column=4, pady=1)
btnLog1p = Button(calc, text= "Log1p", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Log1P).grid(row=5, column=5, pady=1)
btnaexpm1 = Button(calc, text= "expm1", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Expm).grid(row=5, column=6, pady=1)
btnLgamma = Button(calc, text= "lgamma", width=6, height=2, font = ("arial",20,"bold"), 
                     bd=4, bg="#23A199", command=added_value.Lgmma).grid(row=5, column=7, pady=1)

LabelDisplay = Label(calc,text="Scientific Calculator", font = ("arial",25,"bold"),justify=CENTER)
LabelDisplay.grid(row=0, column=4, columnspan=4)
def Exit():
    exit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit?")
    if exit > 0: 
        root.destroy()
        return   

def Standard():
    root.resizable(width = False, height = False)
    root.geometry("472x541+0+0")


def Scientific():
    root.resizable(width = False, height = False)
    root.geometry("936x541+0+0")

    
    
    
menubar = Menu(calc)

filemenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Standard Mode", command = Standard)
filemenu.add_command(label = "Scientific Mode", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = Exit)


editmenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_command(label = "Paste")

convertermenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Converter", menu = convertermenu)
convertermenu.add_command(label = "Length")
convertermenu.add_command(label = "Temparature")
convertermenu.add_command(label = "Time")
convertermenu.add_command(label = "Data")

root.config(menu = menubar)
root.mainloop()


# In[ ]:





# In[ ]:




