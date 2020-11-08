from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import csv
import os
import sys
import time
import socket
from datetime import datetime
import webbrowser
from tkinter import ttk
from tkinter.colorchooser import *
import random
import requests

class HyperlinkManager:

    def __init__(self, text):

        self.text = text

        self.text.tag_config("hyper", foreground="#6c4b3c", underline=1)

        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)

        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
 
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return

def click1():
   
    webbrowser.open(website, new=0, autoraise=True)


    


hostname = socket.gethostname()
#hostname = "test"
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)   

def clearLog():
    global filename_log
    global updated_row_count
    global loaded_row_count
    
    open(filename_log, 'w',encoding="utf-8").close()
    fl = open(filename_log, 'w',encoding="utf-8")
    fl.write("---DELETED---\n")
    fl.close()

        
    #--clears row count file and empties it
    open(filename_row,"w",encoding="utf-8").close
    fr= open(filename_row,"w",encoding="utf-8")
    fr.write(str(1))
    fr.close()

    updated_row_count=1
    loaded_row_count=1



    
    
def rowCount():
 
    global filename_log

    row_data=[]

    
    #--opens log file and counts rows
    with open(filename_log,encoding="utf-8") as f:
        for i, l in enumerate(f):
            pass
        row_count = i


   #--closes file
    f.close()

    return row_count+1

def intialize():
    global filename_log

    #makes lg open to being added to
    lg.config(state="normal")

    
    f=open(filename_log,encoding="utf-8")
    lines=f.readlines()

    rowcnt = rowCount()

    x = 1
    while x<rowcnt:
        
        website=lines[x]
            
        webLoc = website.find("www.")
        
        if webLoc==-1:
            webLoc=website.find("https:")
            webLen = len(website)
            website = website[webLoc:webLen]
      
            
        if "www." in website or "https:" in website:
                
                hyperlink = HyperlinkManager(lg)
                lg.insert(END,lines[x],hyperlink.add(click1))
        
                
        else:
                if randomColor==1:
                    
                    color =randomColorMode()
                    #print(color)
                
                    lg.tag_config(color,foreground=color)

               
                
                    lg.insert(END,lines[x],color)
                else:

                    end=lines[x].find(":")
                    y = lines[x]
                    if y[0:end]==user_name.get():
                       lg.tag_config("self",foreground=textColor)
                       lg.insert(END,lines[x],"self")

                    else:
                         lg.insert(END,lines[x])
                
                
        x =x+1
    lg.see("end")
    user_entry.focus_set()
    
def update():
    global loaded_row_count
    global updated_row_count
    global filename_log
    global hostname
    global website
    global frozenText
    global textColor
    global crypto_count
    global fm
        
    lg.config(state="normal")
    #print("this is entry lenght " + str(len(user_entry.get())))
    #print("Loaded row count "+str(loaded_row_count))
    #print("Updated row count "+str(updated_row_count))
    
    
    
    updated_row_count = rowCount()
    if loaded_row_count<updated_row_count:
        
        print("================SCREEN MOVED========= at "+"this is updated "+str(updated_row_count)+"this is loaded "+str(loaded_row_count))
        f=open(filename_log,encoding="utf-8")
        lines=f.readlines()
        
        while updated_row_count>loaded_row_count:
            
            website=lines[loaded_row_count]
            filename = lines[loaded_row_count]
           
            
            
            webLoc = website.find("www.")
            if webLoc==-1:
                webLoc=website.find("https:")
                webLen = len(website)
                website = website[webLoc:webLen]
            
            if "P:" in filename:
                print(filename)
                website = website[website.find("P:"):len(website)]
           
                

            
            
            if "www." in website or "https:" in website:
                  hyperlink = HyperlinkManager(lg)
                  lg.insert(END,lines[loaded_row_count],hyperlink.add(click1))
               
                  user_entry.focus_set()
            elif "P:" in filename:
                
                 hyperlink = HyperlinkManager(lg)
                 lg.insert(END,lines[loaded_row_count],hyperlink.add(click1))
               
                 user_entry.focus_set()
            else:
                 if randomColor==1:
                    
                    color =randomColorMode()
                    #print(color)
                
                    lg.tag_config(color,foreground=color)

               
                
                    lg.insert(END,lines[loaded_row_count],color)
                 else:

                    end=lines[loaded_row_count].find(":")
                    y = lines[loaded_row_count]
                    if y[0:end]==user_name.get():
                        lg.tag_config("self",foreground=textColor)
                        lg.insert(END,lines[loaded_row_count],"self")

                    else:
                        lg.insert(END,lines[loaded_row_count])
                
                
        
            lg.see("end")
            loaded_row_count+=1
            user_entry.focus_set()
            user_entry.icursor(len(user_entry.get()))
            
        f.close()
        root.deiconify()
        root.lift()
        
   
        markOnline()
            
        fcs = root.focus_get()
        print(fcs)
        if fcs == ".!frame2.!entry":
            user_entry.focus_set()
            user_entry.icursor(len(user_entry.get()))

        else:
            lg.see("end")
    else:
        None
        #print("focus is:",root.focus_get())
            
        


    #checks to see if frozenstate of text is on
   
    if frozenText==1:
        
        lg.config(state="disable",fg='gray') #bg='snow2'
       
    else:
       
        lg.config(state="normal",fg='black')

    
        
  

    
    

    if crypto_count==10:
        
         r = get_latest_bitcoin_price()
         r = "BitCoin Price: $" + str(r)

         menubar.entryconfigure(4, label=r)
         crypto_count = 0
            #print(str(crypto_count)+" BTC Updated!")

    else:
         crypto_count=crypto_count+1
       # print(crypto_count)

    root.after(1000, update)

def shortCuts():
    global updated_row_count
    global msg
    global filename_kao

    kaomoji_data = []
    
    with open(filename_kao, newline='',encoding="utf-8") as csvfile:
          kaomoji_data = list(csv.reader(csvfile))
    csvfile.close()
          
   
    for k in kaomoji_data:

        if k[0] in str(msg):
       
        #if k[0]==str(msg):
          #  msg = k[1]
            msg = msg.replace(k[0],k[1])
            print(msg)
    if "IP" in str(msg):
        msg = msg.replace("IP",IPAddr)
        
    if "btc" in str(msg):
        r = get_latest_bitcoin_price()
        r = "BitCoin Price: $" + str(r)
        msg = msg.replace("btc",r)
        print(msg)
        
def get_latest_bitcoin_price():
    BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])
   

def writeLog(event):
    global filename_log
    global lg
    global updated_row_count
    global msg

    msg = user_entry.get()
    shortCuts()
    
    f= open(filename_log,"a+",encoding="utf-8")

    import time
    ts = time.gmtime()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    msgg = user_name.get()+": "+msg
    
    
  
    f.write(msgg+'\n')
    f.close()
    
   
    
    
    if user_entry.get()=="zxc":
       clearLog()
    
        
        
    else:
       #updated_row_count+=1
       None
    #rowCount()
    update()
    user_entry.delete(0, END)
    user_entry.focus_set()

def writeLogButton():
    global filename_log
    global lg
    global updated_row_count
    global msg

    msg = user_entry.get()
    shortCuts()
    
    f= open(filename_log,"a+",encoding="utf-8")

    import time
    ts = time.gmtime()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    #print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
    #print(xx)
    
    #msgg = '\n'+user_name.get()+": "+timestamp+"\\"+msg
    msgg = user_name.get()+": "+msg
    
    
    #f.write(timestamp+" "+msgg+'\n')
    f.write(msgg+'\n')
    #lg.insert(END, msgg)
    #lg.insert(END,'\n')
    f.close()
    
   
    
    
    if user_entry.get()=="zxc":
       clearLog()
    
        
        
    else:
       #updated_row_count+=1
       None
    #rowCount()
    update()
    user_entry.delete(0, END)
    user_entry.focus_set()

    
def findUserName():
    global hostname
    global filename_user
    global textColor

    x = ''

    user_data = []
         
    
    with open(filename_user,encoding="utf-8") as csvfile:
          user_data = list(csv.reader(csvfile))
    csvfile.close()

    
    #=== the code below eliminates teh empty lists [] created by opening the
    #=== the list read from the CSV file
    user_data = [i for i in user_data if i != []]
    #checks to see if sure exsits
    for u in user_data:
        print(u[0])
        print(u)
    
        if u[0]==hostname:
                x = u[1]
                textColor=u[4]
            
       

    #if it doesnt it asks to create one
    if x =='':
       x = createUser()
       user_name.delete(0, END)
       #user_name.insert(0,x)
     
    return x
        
    

def createUser():
    global hostname
    global filename_user
    global chat
    
    uname = simpledialog.askstring("Create New User","Input your Username.")
    
    if uname is None:
        messagebox.showwarning("No User Added","no name entered")
    else:
        with open(filename_user,encoding="utf-8") as csvfile:
              user_data = list(csv.reader(csvfile))
              csvfile.close()
         #=== the code below eliminates teh empty lists [] created by opening the
        #=== the list read from the CSV file
        user_data = [i for i in user_data if i != []]
        x = 0
        found = False
        
        for u in user_data:
            if u[0]==hostname:
                user_data[x][1]=uname
                
                found = True
            x+=1
           
        if found is not True:
            #sets up pc name, user name, online status, and deleteable text
           user_data.append([hostname,uname,1,0,"#00000",chat])
        else:
            user_name.delete(0, END)
            user_name.insert(0,uname)
            
            
            
            
        with open(filename_user, 'w',encoding='utf-8',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(user_data)
        csvfile.close()
     
        return uname
    




def userOnline():
    global hostname
    global filename_user
    
   
    x = 0

    user_data = []
    
    with open(filename_user,encoding="utf-8") as csvfile:
          user_data = list(csv.reader(csvfile))
    csvfile.close()
    
    for u in user_data:
        if u[0]==hostname:

            user_data[x][2]=1
            ts = time.gmtime()
            timestamp = time.strftime("%H:%M:%S %m/%d/%Y", ts)

            nm = user_name.get()

            phrase= ["hell", "マイクの最後のとりで","yahwe's funhouse"]
            p = random.randint(0, len(phrase)-1)
           
            print(p)
            phrase = phrase[p]
    
            f= open(filename_log,"a+",encoding="utf-8")
            f.write(f"***{nm} came from {phrase} to join the chat!*** \n{timestamp} \n")
            f.close()

            
        x+=1

    with open(filename_user, 'w',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(user_data)
    csvfile.close()
def markOnline():
    global hostname
    global filename_user
    global userstring

   
    user_data = []



    with open(filename_user,encoding="utf-8") as csvfile:
         user_data = list(csv.reader(csvfile))
    csvfile.close()
   
    x = 0
    userstring='Online\n'
   

    for u in user_data:
       
        if int(u[2])==1 and u[0]!=hostname:
          
            
           
        


            userstring = userstring+u[1]+"\n"
    online_label.configure(text=userstring)
   


def loadFrozenTextState():
    global hostname
    global filename_user
    global frozenText

    ft=0
    x = 0

    user_data = []
    
    with open(filename_user,encoding="utf-8") as csvfile:
          user_data = list(csv.reader(csvfile))
    csvfile.close()

     #=== the code below eliminates teh empty lists [] created by opening the
    #=== the list read from the CSV file
    user_data = [i for i in user_data if i != []]
    
    for u in user_data:
        if u[0]==hostname:

            ft=u[3] #grabs frozen text state from csv file
         
        x+=1

    #if ft==1:
     #   print(f"this is in update {frozenText}")
     #   lg.config(state="disabled")
   # else:
    #    lg.config(state="normal")
    
    return int(ft)

def changeFrozenTextState():
    global hostname
    global filename_user
    global frozenText

    if frozenText==1:
        frozenText=0
    else:
        frozenText=1


    
    
   
    x = 0

    user_data = []

     #=== the code below eliminates teh empty lists [] created by opening the
    #=== the list read from the CSV file
    user_data = [i for i in user_data if i != []]
    
    with open(filename_user,encoding="utf-8") as csvfile:
          user_data = list(csv.reader(csvfile))
    csvfile.close()
    
    for u in user_data:
        if u[0]==hostname:

            u[3]=frozenText
            
        x+=1

    with open(filename_user, 'w',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(user_data)
    csvfile.close()
    


    

   

def on_closing():
    global hostname
    global filename_user
    
    ts = time.gmtime()
    timestamp = time.strftime("%H:%M:%S %m/%d/%Y", ts)

    nm = user_name.get()

    phrase= ["bye bye", "さよなら","あばよ","au revoir","じゃあね","ジャガイモがいいね"]
    p = random.randint(0, len(phrase)-1)
    print(p)
    phrase = phrase[p]
    
    f= open(filename_log,"a+",encoding="utf-8")
    f.write(f"***{nm} said {phrase} to the chat!***\n {timestamp} \n")
    f.close()
    
   

    

    
    x = 0
    user_data = []
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    with open(filename_user,encoding="utf-8") as csvfile:
            user_data = list(csv.reader(csvfile))
    for u in user_data:
            
            #print(hostname+"-----------")
            #print(u[0])
        if u[0]==hostname:
                #print(user_data[x][2])
            user_data[x][2]=0
        x+=1
       # print(user_data)
    with open(filename_user, 'w',encoding='utf-8',newline='') as csvFile:
         writer = csv.writer(csvFile)
         writer.writerows(user_data)
    root.destroy()


def focusview(event):
    lg.yview(END)



   
def forceUser():
    global hostname
    hostname = "TestUSER"
    userOnline()



def changeChatRoom():
    global chat
    chat= "Chatroom"
    lg.config(state="normal",fg='black')
    lg.delete(1.0,END)
def randomColorMode():
    import random
    
    letters = ''
    for j in range(6):
        letters = letters+random.choice('0123456789ABCDEF')

    color = "#"+''.join(letters)
    return color

def randomColorOn():

    global randomColor

    if randomColor == 0:
        
        randomColor=1

        color = randomColorMode()
        user_name_label.config(bg=color)
        online_label.config(bg=color)
        enterb.config(bg=color)
        f1.config(bg=color)
        user_name.config(fg=randomColorMode(),bg=randomColorMode())
    else:
     
        randomColor =0
        user_name.config(fg='black',bg="white")
        color='SystemButtonFace'
        user_name_label.config(bg=color)
        online_label.config(bg=color)
        enterb.config(bg=color)
        f1.config(bg=color)

        

def clearText():
    lg.config(state="normal",fg='black')
    lg.delete(1.0,END)

def changeTextColor():
    global textColor
    color = askcolor()
    print(color[1])
    textColor = color[1]

    x = 0

    user_data = []

     #=== the code below eliminates teh empty lists [] created by opening the
    #=== the list read from the CSV file
    user_data = [i for i in user_data if i != []]
    
    with open(filename_user,encoding="utf-8") as csvfile:
          user_data = list(csv.reader(csvfile))
    csvfile.close()
    
    for u in user_data:
        if u[0]==hostname:

            u[4]=textColor
            
        x+=1

    with open(filename_user, 'w',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(user_data)
    csvfile.close()
    lg.tag_config("self",foreground=textColor)
    
def on_resize(event):
     
        root.width = event.width   #>>>854
        root.height = event.height #>>>404
        root.config(width=root.width, height=root.height)
        #lg.see("end")


        




#--load up info--

chat = "log"
filename_log= f"LOG/{chat}.txt"
filename_row= "LOG/row count.txt"
filename_kao= "Misc/kaomoji.csv"
filename_user= "Misc/user.csv"
fm = ""



randomColor=0
textColor = "#00000"

crypto_count = 0
loaded_row_count = rowCount()


print("this is loaded row count " + str(loaded_row_count))
updated_row_count = 0
website=""
msg =''
rtTitle="Chatz 3.17 - 日本語, fix focus/rowcount issue!"

frozenText=loadFrozenTextState()
print(frozenText)

#checks pc name and creates user info if not already there.




#creates root window
root = Tk()
root.title(rtTitle)
root.iconbitmap(r'Images\logo.ico')

root.geometry("400x150")












#creates a frame for user name entry and label
f1 = Frame(root)
f1.pack(expand=1,fill=Y,side=RIGHT)

#creates a frame for log and user entry
f2 = Frame(root)
f2.pack(expand=1,fill=BOTH,side=LEFT)





#list boxes to show texts sent
lg =Text(f2,width=45,height = 1,wrap=WORD)
lg.pack(fill=BOTH,expand=1)

lg.config(font=("Arial", 9),state="normal")


#adds the long entry for people to type in
user_entry = Entry(f2, text="",width=45)
user_entry.insert(0,"")
user_entry.pack(fill=BOTH,side=BOTTOM)
user_entry.config(font=("Arial", 9))






#creates entry and label for user name
user_name_label = Label(f1,text="UserName")
user_name_label.pack()
user_name = Entry(f1, text="",width=10)
user_name.insert(0,findUserName())
user_name.pack()

#adds online to frame

online_label = Label(f1,text="Online")
online_label.pack()


#creates send button
enterb =Button(f1,text='--Send--',command=writeLogButton)
enterb.pack(side=BOTTOM,fill=X)


#creates menu bar
menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)

filemenu.add_command(label = "Change User Name", command = createUser)
filemenu.add_command(label = "Change Text Color", command = changeTextColor)
filemenu.add_separator()


filemenu.add_command(label = "Deleteable Text On/Off", command = changeFrozenTextState)

filemenu.add_command(label = "Clear Text On Screen", command = clearText)


menubar.add_cascade(label = "File", menu = filemenu)






filemenu2 = Menu(menubar, tearoff = 0)

#filemenu2.add_command(label="Force User Address", command = forceUser)
filemenu2.add_command(label="Change Chat Room", command = changeChatRoom)


menubar.add_cascade(label = "Experimental", menu = filemenu2)


filemenu3 = Menu(menubar, tearoff = 0)

filemenu3.add_command(label="Random Text Color", command = randomColorOn)

menubar.add_cascade(label = "FUN!!", menu = filemenu3)

root.config(menu = menubar)

filemenu4 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "BC", menu = filemenu4)

root.config(menu = menubar)



#binds enter button to function "writeLog"
root.bind('<Return>', writeLog)





#this refocuses the text box when you resize the root window
root.bind("<Configure>", on_resize)





    
#loads user name

       

# call first time
intialize()
update()


# call first time after 100 ms


userOnline()













root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
