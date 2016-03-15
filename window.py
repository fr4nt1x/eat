import tkinter as tk
from ingredients import *
from main import *
import math
class Scroll(tk.Frame):
    def __init__(self, root,scrollrow,scrollcolumn,title=""):

        tk.Frame.__init__(self, root)
        self.Title = tk.Label(root, text=title)

        self.canvas = tk.Canvas(root, borderwidth=0, height=400,background="#ffffff")
        self.frame = tk.Frame(self.canvas,background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.grid(row=scrollrow+1,column=scrollcolumn, sticky='ns')
        self.canvas.grid(row=scrollrow+1,column=scrollcolumn+1)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")
        
        self.Title.grid(row=scrollrow,column=scrollcolumn)
        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        
class App:

    def __init__(self, master):

        self.nameL1 = tk.Label(master, text="MealName")
        self.day = getCurrentDay()
        
        self.nameL1.grid(row=3,column=1)
        self.name = tk.Entry(master)
        
        self.name.grid(row=3,column=2)
        self.name.delete(0, tk.END)
        
        #plus 2 because scrollbar and canvas 
        self.scaleFrames = []
        for i in range(0,len(IngredientList)):
            
            column = i%4
            row=math.floor(i/4.)
            
            self.scaleFrames.append(Scroll(master,2*row+1,2*column+1,[x for x in sorted(IngredientList)][i]).frame)  
        
        self.getKcalButton = tk.Button(
            master, text="Get Kcal", command=self.getKcal
            )
        
        self.currentDayVariable = tk.StringVar()
        self.currentDayVariable.set("Active Day: "+str(self.day.dateofconsum))
        self.currentDayL = tk.Label(master,textvariable=self.currentDayVariable)
        self.currentDayL.grid(row=1,column=0)
        
        self.getKcalButton.grid(row=2,column=0)
        self.kcalAll = tk.StringVar()
        self.getKcal()
        self.kcalShow = tk.Label(master, textvariable=self.kcalAll)
        self.kcalShow.grid(row=4,column=0)
        self.scales = []
        
        self.changeDay = tk.Button(
            master, text="Change Day", command=self.changeDay
            )
        
        self.changeDay.grid(row=4,column=4)
        
        self.apply = tk.Button(
            master, text="Apply", command=self.apply
            )
        self.apply.grid(row=3,column=4)
        
        i=0
        for key in sorted(IngredientList):
            for k in sorted(IngredientList[key]):
                f= self.scaleFrames[i]
                w= tk.Scale(f ,label=k+" "+str(IngredientList[key][k](1).GperOne), from_=0, to=5,resolution=0.1,length="100mm",orient=tk.HORIZONTAL,showvalue=1)
                self.scales.append((k,w))
            i+=1

        for k,v in self.scales:
            v.pack()
            
    def getKcal(self):
        self.kcalAll.set("Kcal: "+str(sum([x.kcal for x in self.day.meals])))
            
    def apply(self):
        kcal = 0
        for k,v in self.scales:
            scalevalue = v.get()
            v.set(0)
            if scalevalue > 0.0:
                ing = IngredientList[k](scalevalue)
                kcal += ing.getKcal()
        if kcal >0:
            addMeal(self.day,self.name.get(),kcal)
            self.name.delete(0, tk.END)
            self.getKcal()
            
    def changeDay(self):
        
        def SetDay():
            selection = listbox.curselection()
            if len(selection) ==1 :
                self.day= days[selection[0]][1]
                self.currentDayVariable.set("Active Day: "+str(self.day.dateofconsum))
                top.destroy()
        top = tk.Toplevel()
        top.title("Change Day")
        
        listbox = tk.Listbox(top)
        listbox.pack()
        
        days = [(x.dateofconsum,x) for x in session.query(Day).order_by(Day.dateofconsum.desc()).limit(10)]
        for key,value in days:
            listbox.insert(tk.END, key)
            
        msg = tk.Message(top, text="Change the Day")
        msg.pack()
        
        button = tk.Button(top, text="Cancel", command=top.destroy)        
        button.pack()
        button = tk.Button(top, text="Apply", command=SetDay)        
        button.pack()

      
         
root = tk.Tk()
root.title("Eatit")
app = App(root)


root.mainloop()
root.destroy() # optional; see description below
