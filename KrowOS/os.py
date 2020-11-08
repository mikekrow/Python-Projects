from tkinter import *

def calculate(equation):
    equation = equation.replace("x", "*")
    print(equation)
    #equation = equation.replace("*", "X")

    try:
        char = str(eval(equation))
        
    except:
        char = f"Unexpected error: {sys.exc_info()[0]}"
    return char



    return

class main:
    def __init__(self,master):
      
        
        self.master = master
        master.geometry("200x120")  

      
        self.frame = Frame(self.master)
        self.frame.pack(expand=1,fill=BOTH)


        #TextBox that will show conversation
        self.txt =Text(self.frame,width=45,height = 1,wrap=WORD)
        self.txt.pack(fill=BOTH,expand=1)
        self.txt.config(font=("Arial", 9),state="normal", background = "black", foreground = "white", insertbackground='white')
        self.txt.insert(END,"text")
        self.txt.configure(state = "disabled")

        #entry to recieve user input
        self.cmndLine = Entry(self.frame, text="",width=45, background = "black", foreground = "white", insertbackground='white')
        self.cmndLine.insert(0,"") 
        self.cmndLine.pack(fill=BOTH,side=BOTTOM)
        self.cmndLine.config(font=("Arial", 9))
        
        
        self.master.bind('<Return>',self.mainOS)

        #this refocuses the text box when you resize the root window
       # self.master.bind("<Configure>", self.onResize)
 
    def mainOS(self,event):
        cmnd = str(self.cmndLine.get()).lower()
        

        if cmnd.startswith("$$"):
             self.cmndLine.delete(0,END)
             cal = cmnd[2:len(cmnd)]
             cmnd = calculate(cal)
             self.txt.configure(state = "normal")
             self.txt.insert(END,f"\n{cal} = {cmnd}")
             self.txt.see(END)
             self.txt.configure(state = "disabled")
             
       

    def onResize(self,event):
     
        self.master.width = event.width   #>>>854
        self.master.height = event.height #>>>404
        self.master.config(width=self.master.width, height=self.master.height)
        




root = Tk()
#root.geometry("200x100")

mainInterface = main(root)
root.mainloop()
