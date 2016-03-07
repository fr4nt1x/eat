import tkinter as tk
from ingredients import *
from main import *

class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.grid(row=4,column=1, sticky='ns')
        self.canvas.grid(row=4,column=2)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        
class App:

    def __init__(self, master):

        self.nameL1 = tk.Label(master, text="MealName")
        
        self.nameL1.grid(row=0,column=0)
        self.name = tk.Entry(master)
        
        self.name.grid(row=0,column=1)
        self.name.delete(0, tk.END)
        
        self.scaleFrame = tk.Frame(master)
        
        ex =  Example(master)
        ex.grid(row=3,column=2)
        self.scaleFrame2 = ex.frame#tk.Frame(master)
        

        self.scaleFrame.grid(row=0,column=2)
        #self.scaleFrame2.grid(row=0,column=3)
        self.getKcal = tk.Button(
            master, text="GetKcalToday", command=self.getKcalToday
            )
        
        self.getKcal.grid(row=1,column=0)
        self.scales = []
        self.apply = tk.Button(
            master, text="Apply", command=self.apply
            )
        self.apply.grid(row=1,column=3)
        i = 0
        for key in sorted(IngredientList):
            w= tk.Scale(self.scaleFrame ,label=key, from_=0, to=5,resolution=0.1,length="100mm",orient=tk.HORIZONTAL,showvalue=1)
            i=i+1
            f= self.scaleFrame
            if i > len(IngredientList)/2:
                f= self.scaleFrame2
            w= tk.Scale(f ,label=key, from_=0, to=5,resolution=0.1,length="100mm",orient=tk.HORIZONTAL,showvalue=1)
            self.scales.append((key,w))    
        for k,v in self.scales:
            v.pack()
            
    def getKcalToday(self):
        day = getCurrentDay()
        print(sum([x.kcal for x in day.meals]))
            
    def apply(self):
        kcal = 0
        for k,v in self.scales:
            scalevalue = v.get()
            v.set(0)
            if scalevalue > 0.0:
                ing = IngredientList[k](scalevalue)
                kcal += ing.getKcal()
        if kcal >0:
            addMeal(getCurrentDay(),self.name.get(),kcal)
            self.name.delete(0, tk.END)
            
root = tk.Tk()

app = App(root)


root.mainloop()
root.destroy() # optional; see description below
