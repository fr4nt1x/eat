import tkinter as tk
from ingredients import *
from main import *
import math


class Scroll(tk.Frame):
    def __init__(self, root,scrollrow,scrollcolumn,title="",font=("Helvetica", 12)):

        tk.Frame.__init__(self, root)
        self.Title = tk.Label(root, text=title,font=font)

        self.canvas = tk.Canvas(root, borderwidth=0, height=400,background="#ffffff")
        self.frame = tk.Frame(self.canvas,background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.grid(row=scrollrow+1,column=scrollcolumn, sticky='nsw')
        self.canvas.grid(row=scrollrow+1,column=scrollcolumn+1)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")
        
        self.Title.grid(row=scrollrow,column=scrollcolumn,columnspan=2,sticky="w")
        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        
class App:

    def __init__(self, master):
        self.FontSize = 14
        self.nameL1 = tk.Label(master, text="Meal Name:",font=("Helvetica", self.FontSize))
        self.currentWeight = tk.Label(master, text="Meal Name:",font=("Helvetica", self.FontSize))
        self.day = getCurrentDay()
        

        self.name = tk.Entry(master)
        

        self.name.delete(0, tk.END)
        
        #plus 2 because scrollbar and canvas 
        self.scaleFrames = []
        self.maxRows = 2
        self.maxColumns = 8
        for i in range(0,len(IngredientList)):
            
            column = i%4

            row=math.floor(i/4.)
            self.maxRows = 2*(row+1)
            self.scaleFrames.append(Scroll(master,2*row+1,2*column,[x for x in sorted(IngredientList)][i]).frame)  
        
        self.updateDayDataBtn = tk.Button(
            master, text="Get Kcal & Weight", command=self.updateData,font=("Helvetica", self.FontSize)
            )
        
        self.currentDayVariable = tk.StringVar()
        self.currentDayVariable.set("Active Day: "+str(self.day.dateofconsum))
        self.currentDayL = tk.Label(master,textvariable=self.currentDayVariable,font=("Helvetica", self.FontSize))

        self.weight = tk.StringVar()
        self.weightShow = tk.Label(master, textvariable=self.weight,font=("Helvetica", self.FontSize))

        self.kcalAll = tk.StringVar()
        self.kcalShow = tk.Label(master, textvariable=self.kcalAll,font=("Helvetica", self.FontSize))

        self.updateData()


        self.scales = []
        
        self.changeDay = tk.Button(
            master, text="Change Day", command=self.changeDay,font=("Helvetica", self.FontSize)
            )
        self.changeWeightBtn = tk.Button(
            master, text="Change Weight", command=self.changeWeight,font=("Helvetica", self.FontSize)
            )
        self.Quit = tk.Button(
            master, text="Quit", command=master.quit,font=("Helvetica", self.FontSize+5),fg="red"
            )

        
        self.apply = tk.Button(
            master, text="Apply", command=self.apply,font=("Helvetica", self.FontSize)
            )
        
        self.callGrid()
        i=0
        for key in sorted(IngredientList):
            for k in sorted(IngredientList[key]):
                f= self.scaleFrames[i]
                w= tk.Scale(f ,label=k+" "+str(IngredientList[key][k](1).GperOne)+" ("+str(IngredientList[key][k](1).kcalPerOne)+")", from_=0, to=5,resolution=0.1,length="100mm",orient=tk.HORIZONTAL,showvalue=1)
                self.scales.append((key,k,w))

            i+=1

        for _,_,v in self.scales:
            v.pack()
            
    def updateData(self):
        self.getKcal()
        self.getWeight()
        
    def getKcal(self):
        self.kcalAll.set("Kcal: "+str(sum([x.kcal for x in self.day.meals])))
        
    def getWeight(self):
        self.weight.set("Weight: "+str(self.day.weight))
        
    def callGrid(self):
        self.currentDayL.grid(row=self.maxRows+1,column=0,columnspan=2,sticky="w")
        self.kcalShow.grid(row=self.maxRows+1,column=2,columnspan=2,sticky="w")
        self.weightShow.grid(row=self.maxRows+1,column=2,columnspan=2,sticky="e")
        self.nameL1.grid(row=self.maxRows+1,column=6,columnspan= 2,sticky="w")
        self.name.grid(row=self.maxRows+1,column=6,columnspan= 2,sticky="e")

        
        self.apply.grid(row=self.maxRows+2,column=4,columnspan= 2,sticky="e")
        self.changeDay.grid(row=self.maxRows+2,column=0,columnspan=2,sticky="w")
        self.updateDayDataBtn.grid(row=self.maxRows+2,column=2,columnspan= 2,sticky="w")
        self.changeWeightBtn.grid(row=self.maxRows+2,column=2,columnspan= 2,sticky="e")
        self.Quit.grid(row=self.maxRows+2,column=6,columnspan= 2,sticky="e")

        
    def apply(self):
        kcal = 0
        for key,k,v in self.scales:
            scalevalue = v.get()
            v.set(0)
            if scalevalue > 0.0:
                ing = IngredientList[key][k](scalevalue)
                print(ing.name)
                kcal += ing.getKcal()
        if kcal >0:
            addMeal(self.day,self.name.get(),kcal)
            self.name.delete(0, tk.END)
            self.getKcal()

    def changeWeight(self):
        top = tk.Toplevel()
        top.title("Add Weight")
        weight = tk.Entry(top)
        weight.pack(anchor="e")
        def SetWeight():
            weightuser = weight.get()
            try:
                # Try to make it a float
                weightuser = float(weightuser)
                self.day.weight = weightuser
                session.commit()
                top.destroy()
            except ValueError:
                # Print this if the input cannot be made a float
                print ("Bad input")
                
        msg = tk.Message(top, text="Enter Weight:")
        msg.pack()
        
        button = tk.Button(top, text="Cancel", command=top.destroy)        
        button.pack()
        button = tk.Button(top, text="Apply", command=SetWeight)        
        button.pack()
        



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
        
        days = [(x.dateofconsum,x) for x in session.query(Day).order_by(Day.dateofconsum.desc()).limit(12)]
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
#root.attributes("-fullscreen", True)
app = App(root)

root.mainloop()
root.destroy() # optional; see description below
