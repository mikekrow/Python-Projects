#Created in Feb 2020 by Mike Krow


import csv, os, os.path, sys, time, socket, webbrowser, random, requests, pathlib

from datetime import datetime

from tkinter import *
from tkinter import messagebox



from tkinter import ttk
from tkinter.colorchooser import *



from os import path
from os import walk


buildName = "CHATZLITE 3.0" #the version name to be used on window titles


#intializing variables
user = []
IP, hostname, name, Chatroom,onlineUsers ="","","","",""
userfile,stock, chatroom,currentChatroom = "","","",""
textcolor = "#000000"


Dtxt,Rtxt = 0,0 #variables for deletable text and random color text//not used.
online = False

filenameLog = "CHATZROOMZ/cool.txt" #sets the default chatroom
dirPathUsers = os.path.dirname("USERS\\")#the path name for users folder





def saveUserData():
    global userfile, textcolor,user,name,root

    user = [] #resets user so we dont get double appending going on

            
    user.append ([IP,       #IP
                hostname, #Hostname aka computer name
                name,     #name of user
                chatroom, #name of chatroom
                textcolor,#Hex for text color
                Dtxt,    #whether deletable text is on or off 
                Rtxt,    #whether random text color is on or off
                online   #indicates whether or not online
               ])


    
    #opens up user file that holds their information and truncates it
    file = open(userfile, "w+",encoding='utf-8')
    file.close()

    #opens up user file and writes information from user variable
    with open(userfile, 'w',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(user)
        csvfile.close()



#function for pulling up color picker
def chooseColor():
        global textcolor,user,t

        try:
            file = open(userfile,encoding='utf-8')
            file.close()
            textcolor = askcolor(parent = t)
            textcolor = textcolor[1]
            saveUserData()
           
        except:
            
        
            textcolor = askcolor(parent = t)
            textcolor = textcolor[1]
        
       




def changeName():
    global t
    t = Toplevel(root)#creates toplevel for newuser class

    x = root.winfo_rootx()
    y = root.winfo_rooty()

    #sets the location of the new toplevel relative to the root window.
    geom = "+%d+%d" % (x+20,y-80)
    t.geometry(geom)
            
    newuser(t, width="10", height="10")

    t.grab_set() #makes it so this is the only window that can be used
    t.attributes('-topmost', 1)#moves window to uptmost top
    root.wait_window(t)

def about():
    webbrowser.open('https://github.com/mikekrow/CHATZLITE')


def onlineStatus():
    global userfile,online,user,root

    #sets online part of user informatin as True
    user[0][7] = True

    #this makes the onlineStatus repeat every 1 second
    whosOnline()
    root.after(1000, onlineStatus)
    

def onClosing():
    global userfile,online,user

    #sets online part of user informatin as False
    user[0][7] = False

    #runs function to save users data
    saveUserData()
    

    #destroys the root and kills program
    root.destroy()



    
def whosOnline():
    global onlineUsers,user,dirPathUsers

    #makes onlineUsers variable empty so we can add the new list onto it
    onlineUsers = ""
    
    #walks through root, directories and files of path
    for Root, Dirs, Files in os.walk(dirPathUsers):

        #looks at each file in USERS folder
        for file in Files:

            #creates a path for the csv file we are about to open
            csvFileName = "USERS\\"+file

            #opens csv file as read only
            with open(csvFileName,'rt',encoding='utf-8')as f:

                    #puts info from csv file into list so we can use it
                     data = list(csv.reader(f))

                     #variables to check from file
                     namez = data[0][2]
                     status = data[0][7]

                     #this is the chatroom on the file and not the chatroom
                     #we are currenlty connected to
                     myChatroom = data[0][3]
                     
    

                     #if online status equal true and user chatroom from csv file
                     #is the same as the users loaded data then add them on the same
                     #onlineUsers variable
                     if (str(status)=="True" and user[0][3]==myChatroom):

                            #adds new users to variable
                            onlineUsers = onlineUsers + namez+"\n"
                            
                     else:

                        #if not the variable stays the same
                        onlineUsers = onlineUsers
    
                         
#new user top for first time use and later to change user name
class newuser:
    def __init__(self, master,width,height):
        global user, userfile,hostname,IP,name,textcolor,online,chatroom,root
        
        self.master = master
        x = random.randint(1, 100)
        master.title("Name & Text Color")
        master.geometry("250x145")
        master.iconbitmap(r'Images\logo.ico')

        x = root.winfo_rootx()
        y = root.winfo_rooty()
       
        geom = "+%d+%d" % (x+20,y-80)
        master.geometry(geom)
        
        master.focus()


        #this is the default chatroom
        chatroom = "cool.txt"
        filenameLog = "CHATZROOMZ/"+chatroom

        try:#check to see if you can open user file name, if not means they are new
            file = open(userfile,encoding='utf-8')
            file.close()
            L1 = Label(self.master,text="Change your name &\n text color here!",font=("Courier", 10))
        except:
            root.withdraw()
            L1 = Label(self.master,text="WELCOME to CHATZ!",font=("Courier", 12))

        L1.pack()
        L1.config(font=("Courier", 12))
        L2 = Label(self.master,text="Please input your name")
        L2.pack()

        nm = Entry(self.master)
        nm.pack()
        nm.focus()
       


        b1 = Button(self.master,text="Choose Text Color",command=chooseColor)
        b1.pack()
        handler = lambda: onClose()
        b2 = Button(self.master,text = "<submit>",command=handler)
        b2.pack()

        
        

        def onClose():
            if nm.get()=="":
                messagebox.showinfo(buildName, "You need a name to start! ( ͡° ͜ʖ ͡°)")
            else:
                writetofile()
                

        def writetofile():
            global textcolor,user,name,root

            root.deiconify()
            #if text color is not choosen
            if textcolor =="":
                textcolor ="#000000"
            
            name = nm.get() #get user name from name entry

            if name=="":
                messagebox.showerror("Error", "Please enter a name.")
                return
            
            
            user = [] #resets user so we dont get double appending going on

            
            user.append ([IP,       #IP
                hostname, #Hostname aka computer name
                name,     #name of user
                chatroom, #name of chatroom
                textcolor,#Hex for text color
                Dtxt,    #whether deletable text is on or off 
                Rtxt,    #whether random text color is on or off
                online   #indicates whether or not online
               ])

            
            saveUserData()
            self.master.destroy()
           

        

            
       


def loadUser():
        global user, userfile,hostname,IP,name,online,filenameLog,textcolor,chatroom
        

    
        #gets hostname and IP of user
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)

    
     

        #creates the path for userfile
        userfile = pathlib.Path("USERS/"+IP+hostname+".csv")
    
        #sets user online 
        online = True 
    
    

        
        #check if user file already exsists
        if userfile.exists (): #if so it loads the info

           #loads user file into user as a list and closes after done
            with open(userfile,encoding="utf-8") as csvfile:
                  user = list(csv.reader(csvfile))
                  csvfile.close()
                  
          
            name = user[0][2]
            user[0][7] = True
            textcolor = user[0][4]
            chatroom = user[0][3]
          
            if  (chatroom.find(":") != -1):
                filenameLog=chatroom
            else:
                
                filenameLog = "CHATZROOMZ/"+chatroom
            saveUserData()
    
        else: #if not, it creates one
            
            print ("File not exist")
            global root,t
            
            t = Toplevel(root)#creates toplevel for newuser class
            x = root.winfo_rootx()
            y = root.winfo_rooty()
       
            geom = "+%d+%d" % (x+20,y-80)
            t.geometry(geom)
            
            newuser(t, width="10", height="10")

            t.grab_set() #makes it so this is the only window that can be used
            t.attributes('-topmost', 1)#moves window to uptmost top
            root.wait_window(t)









class main:
    def __init__(self, master):
        global onlineUsers,name,chatroom,currentChatroom

        self.master = master
        master.title(buildName)
        master.geometry("250x110")

        self.menubar = Menu(self.master)

        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.filemenu2 = Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label = "Change CHATZROOM", command = self.changeChat)
        self.filemenu.add_command(label = "Settings", command = changeName)
        self.filemenu.add_command(label = "About - Consider Donating!", command = about)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)
        
        self.master.config(menu = self.menubar)

        currentChatroom = chatroom
        self.currentRowCount = 0
        
        #creates a frame for user name entry and label
        self.frame1 = Frame(self.master)
        self.frame1.pack(expand=1,fill=X, side = "left")

        self.onlineLabel = Label(self.frame1, text = onlineUsers)
        self.onlineLabel.pack()

        #creates frame for online user display
        self.frame2 = Frame(self.master)
        self.frame2.pack(expand=1,fill=BOTH)


        #TextBox that will show conversation
        self.chatTextbox =Text(self.frame2,width=45,height = 1,wrap=WORD)
        self.chatTextbox.pack(fill=BOTH,expand=1)
        self.chatTextbox.config(font=("Arial", 9),state="normal")

        #entry to recieve user input
        self.userEntry = Entry(self.frame2, text="",width=45)
        self.userEntry.insert(0,"") 
        self.userEntry.pack(fill=BOTH,side=BOTTOM)
        self.userEntry.config(font=("Arial", 9))

        self.update()

        #binds enter to activate write log function
        self.master.bind('<Return>', self.writeLog)

        
        #this refocuses the text box when you resize the root window
        self.master.bind("<Configure>", self.onResize)
    
        

    def update(self):
        global filenameLog,onlineUsers,textcolor,name,user,chatroom,currentChatroom

        if currentChatroom != chatroom:
            currentChatroom = chatroom
            self.currentRowCount = 0
            self.chatTextbox.delete('1.0', END)
        
        #makes lg open to being added to
        self.chatTextbox.config(state="normal")

        
       #=============cause if there are no lines in the txt file it breaks...
        rowcnt = self.rowCount()
        
        if rowcnt==2:
            currentRowCount = 1
            file= open(filenameLog,"a+",encoding="utf-8")

       
        
            message = "======:firstline keep or it breaks....:====="
  
            file.write(message+'\n')
            file.close()
        #======================================
            
        rowcnt = self.rowCount()
        file=open(filenameLog,encoding="utf-8")
                
        lines=file.readlines()
        file.close()  

        
            
        

        
    
        
        x = 1
        while self.currentRowCount<rowcnt:

            try:
                end=lines[self.currentRowCount].find(":")
            except:
                end=1
            
            y = lines[self.currentRowCount]
            if y[0:end]==name:
                self.chatTextbox.tag_config("self",foreground=textcolor)
                self.chatTextbox.insert(END,lines[self.currentRowCount],"self")
                self.chatTextbox.see("end")
            else:
                self.chatTextbox.insert(END,lines[self.currentRowCount])
                self.chatTextbox.see("end")
            #self.chatTextbox.insert(END,lines[x])
                
                
            self.currentRowCount +=1
            

        
        self.onlineLabel.configure(text=onlineUsers)
        self.master.after(1000, self.update)
        

    def rowCount(self):
 
        global filenameLog

        
            
        
    
        #--opens log file and counts rows
        try:
            with open(filenameLog,encoding="utf-8") as file:
            
                for i, l in enumerate(file):
                    pass
                rowcnt = i
            #--closes file
            file.close()

        except:
            rowcnt=1


       

        return rowcnt+1
        
    def writeLog(self,event):
        global filenameLog, name,stock
        

        userInput = self.userEntry.get()
        if userInput.startswith(":") and userInput.endswith(":"):
            stock = userInput.replace(":", "")

            
            URL = 'https://api.coinmarketcap.com/v1/ticker/'+str(stock)+'/'
        
            response = requests.get(URL)

            if str(response) =="<Response [404]>":
                messagebox.showinfo("None found!","check web address!")
            else:
                btc = Tk()
                btc.geometry("110x40")
                x = root.winfo_rootx()
                y = root.winfo_rooty()
       
                geom = "+%d+%d" % (x+20,y-90)
                btc.geometry(geom)
                btcPrice(master=btc)
          
            self.userEntry.delete(0, END)
                

        else:
        
    
            file= open(filenameLog,"a+",encoding="utf-8")

       
        
            message = name+": "+userInput
  
            file.write(message+'\n')
            file.close()
    

        

            self.userEntry.delete(0, END)
            self.userEntry.focus_set()
            self.update()

    #changes the width and height based on whenever the window is changed
    def onResize(self,event):
        
        self.master.width = event.width   
        self.master.height = event.height 
        self.master.config(width=self.master.width, height=self.master.height)


    def changeChat(self):
        
        class chatSelection:
            def __init__(self, master):
                global topNewChat
                self.master = master
                master.title("SELECT CHATZ")
                master.geometry("250x110")
                master.iconbitmap(r'Images\logo.ico')

                x = root.winfo_rootx()
                y = root.winfo_rooty()
       
                geom = "+%d+%d" % (x+30,y-100)
                master.geometry(geom)

                
                dir_path = os.path.dirname("CHATZROOMZ\\")
                self.c= Canvas(self.master,width=50,height = 200)
                self.scroll_y = Scrollbar(self.master, orient="vertical", command=self.c.yview)
                #self.master.geometry("50x100")
                self.f = Frame(self.c,width=50,height=100)
                # group of widgets
                self.v = StringVar(self.f,"1")
                
                self.values = {}
    
                for Root, Dirs, Files in os.walk(dir_path):
        
                    for file in Files:
                        self.values[file] = file
                        
                for (self.text, self.value) in self.values.items():
           
                    Radiobutton(self.f, text = self.text, variable = self.v ,  
                        value = self.value).pack(anchor = 'w') 

                # put the frame in the canvas
                self.c.create_window(0,0, anchor='nw', window=self.f)
                # make sure everything is displayed before configuring the scrollregion
                self.c.update_idletasks()

                self.c.configure(width=50,scrollregion=self.c.bbox('all'), 
                 yscrollcommand=self.scroll_y.set)
                 
                self.c.pack(fill='both', expand=True, side='left')
                self.scroll_y.pack(fill='y', side='right')

                self.f2 = Frame(self.master)
                self.f2.pack()
                

                
                self.b1 = Button(self.f2,text="Move to",command=self.moveChatrooms, width = 10)
                self.b1.pack()
                self.b2 = Button(self.f2,text="New CHATZ", width = 10,command = self.newChatroom)
                self.b2.pack()

                self.b3 = Button(self.f2,text="Direct PATH", width = 10,command = self.directPath)
                self.b3.pack()
                self.master.protocol("WM_DELETE_WINDOW", self.onClose)
            
                
            def directPath(self):
                class directPathWindow:
                    def __init__(self, master):
                            self.master = master
                            master.title("Connect directly to file!")
                            master.iconbitmap(r'Images\logo.ico')
                            master.geometry("200x75")
                            x = top3.winfo_rootx()
                            y = top3.winfo_rooty()
       
                            geom = "+%d+%d" % (x+20,y-90)
                            master.geometry(geom)
                            
                            self.l = Label(self.master,text ="write exact path of txt file")
                            self.l.pack()

                            self.entryNewChat = Entry(self.master)
                            self.entryNewChat.pack()

                            self.b = Button(self.master, text="Connect to file",width = 10,command = self.connectFile)
                            self.b.pack()
                    def connectFile(self):
                        global user,chatroom,filenameLog

                        

                        if os.path.isfile(self.entryNewChat.get()):
                   
                            filenameLog = self.entryNewChat.get()
                      
                            if self.entryNewChat.get() =="1":
                                chatroom = "cool.txt"
                            else:
                
                                chatroom = self.entryNewChat.get()
                    
                            user[0][3]=self.entryNewChat.get()
                        
                            saveUserData()
                            self.master.destroy()
                            top3.destroy()

                            
                        else:
                             messagebox.showinfo(buildName,"File does not exist!")
                        
    
                self.topDirectPath=Toplevel()
                directPathWindow(master=self.topDirectPath)
               
            def newChatroom(self):
                
                class chatNameSelector:
                    global top3,filenameLog,topNewChat
                    def __init__(self, master):
                        self.master = master
                        master.title("Create New Chatroom!")
                        master.geometry("200x75")
                        master.iconbitmap(r'Images\logo.ico')
                        x = top3.winfo_rootx()
                        y = top3.winfo_rooty()
       
                        geom = "+%d+%d" % (x+20,y-90)
                        master.geometry(geom)

                        
                        self.l = Label(self.master,text ="write name for new chat room")
                        self.l.pack()
                        
                        self.entryNewChat = Entry(self.master)
                        self.entryNewChat.pack()

                        self.b = Button(self.master, text="Create New",width = 10,command = self.createFile)
                        self.b.pack()
                    def createFile(self):
                        global top3,filenameLog
                        if self.entryNewChat.get() =="":
                            messagebox.showinfo(buildName,"Input file name!")
                            
                            self.entryNewChat.delete(0, END)
                            self.entryNewChat.focus_set()
                        else:
                            newChatFileName = "CHATZROOMZ\\"+str(self.entryNewChat.get())+".txt"
                            
                            if path.exists(newChatFileName):
                                messagebox.showinfo(buildName,"Error! file name "+newChatFileName+" already exists!")
                                self.entryNewChat.delete(0, END)
                                self.entryNewChat.focus_set()
                                
                            else:
                                file = open(newChatFileName,'w+',encoding='utf-8')
                                file.close()
                                messagebox.showinfo(buildName,"file '"+newChatFileName+" created!")
                                filenameLog = newChatFileName
                                self.master.destroy()                                
                        
                            
                        
                        

                self.topNewChat=Toplevel()
                chatNameSelector(master=self.topNewChat)
              

                

            def moveChatrooms(self):
                global user,chatroom,filenameLog
                if self.v.get() =="1":
                    chatroom = "cool.txt"
                else:
                
                    chatroom = self.v.get()
                    
                user[0][3]=self.v.get()
                filenameLog = "CHATZROOMZ/"+chatroom
                saveUserData()
                top3.destroy()
                
            def onClose(self):
                global topDirectPath, topNewChat
                try:
                    self.topDirectPath.destroy()
                except:
                    None
                try:
                    self.topNewChat.destroy()
                except:
                    None
                self.master.destroy()
        
      
        top3 = Toplevel()
        chatSelection(master=top3)
        
class btcPrice():
    
    def __init__(self, master):
        global root,stock

        
        self.master = master
        master.title("BitCoin Price!")
        master.iconbitmap(r'Images\logo.ico')
        master.geometry("150x40")
        x = root.winfo_rootx()
        y = root.winfo_rooty()
       
        geom = "+%d+%d" % (x+20,y-90)
        master.geometry(geom)
        
        self.t = Text(self.master,height=2,width=20)
        self.t.pack()
        
  
        self.getPrice()

    def getPrice(self):
        global labelText,stock 
        global currentP, newP

        self.thisStock = stock
        self.t.delete('1.0', END)
        self.URL = 'https://api.coinmarketcap.com/v1/ticker/'+str(self.thisStock)+'/'
        
        self.response = requests.get(self.URL)
        

        self.response_json = self.response.json()

        # Convert the price to a floating point number
       
        self.t.insert(END,str(self.response_json[0]['name'])+" Price!\n")
        self.t.insert(END,str(float(self.response_json[0]['price_usd']))+"\n")
       
            
        self.master.after(3000, self.getPrice)
    
   
       
#check to see if starting cool file exsists     
try:
    f = open("CHATZROOMZ\\cool.txt")
    f.close()
    # Do something with the file
except IOError:
    file = open("CHATZROOMZ\\cool.txt", "w+",encoding='utf-8')
    file.close()



root = Tk()
root.geometry("250x110")
root.iconbitmap(r'Images\logo.ico')
loadUser()
onlineStatus()
chatz_gui = main(root)
root.protocol("WM_DELETE_WINDOW", onClosing)
root.mainloop()
