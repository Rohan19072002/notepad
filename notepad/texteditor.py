from pydoc import text
from tkinter import font
from tkinter import *
import datetime
import os
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename
from tkinter.tix import ExFileSelectBox, NoteBook
import keyboard
impvarse=''
start_pos='1.0'
start_pos_replace="1.0"
endposition='1.0'
endpos='1.0'
zstrt='1.0'
zend='1.0'
count=0
fontzoomin=24
fontzoomout=24
fontzoomdefault=24
mainzfontin=[]
zfont=""
zoomcount=0
zoomcountout=0
impvar=''

def barupdate(mouse_pos):
    lines['text'] = 'Line: ' + mouse_pos.split('.')[0]
    chars['text'] = 'Charater: ' + mouse_pos.split('.')[1]

        
def getthelinendcharactr():
    global z
    z =TextArea.index('current')
    return z
def new():
    global file
    if TextArea.get(1.0,END)==0:
        root.title("Untitled - Notepad")
        file=None
        TextArea.delete(1.0,END)
    else:
        z=msg.askyesnocancel(title="Do You want to save?",message="Do You want to save?")
        if z=="yes":
            saveas()
        elif z=="no":
            root.title("Untitled - Notepad")
            file=None
            TextArea.delete(1.0,END)
        else:
            pass


def newwindow():
    os.startfile("texteditor.py")
def open1():
        global file
        file=askopenfilename(filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def save():
    global file
    file=asksaveasfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    f=open(file,"w")
    f.write(TextArea.get(1.0,END))
    f.close()
    root.title(os.path.basename(file)+"- Notepad")
    
def saveas():
    global file
    file=asksaveasfilename(initialfile="*txt", defaultextension=".txt",filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    f=open(file,"w")
    f.write(TextArea.get(1.0,END))
    f.close()
    root.title(os.path.basename(file)+"- Notepad")

    
def exit1():
    root.destroy()
def formatt():

    
    
   
    def font_changed(font):
        global zfont
        TextArea.config(font=font)
        zfont=font
        return zfont

    root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command', root.register(font_changed))
    root.tk.call('tk', 'fontchooser', 'show') 
    
def undo():
    keyboard.press_and_release('ctrl+z')
def cut():
    keyboard.press_and_release('ctrl+x')
def copy():
    keyboard.press_and_release('ctrl+c')
def paste():
    keyboard.press_and_release('ctrl+p')
def delete():
    keyboard.press_and_release('del')
def find():
    def findnext():
        global start_pos
        word=ent.get()
        if word:
                
                start_pos=TextArea.search(word,start_pos,nocase=1,stopindex=END)
                find=(f"0.{str(len(word))}")
                endposition=eval(f"{start_pos}+{find}")
                TextArea.tag_add("found",start_pos,endposition)
                TextArea.tag_config("found",foreground='red',background="blue")
                start_pos=endposition
                
                

                
        
    def cancel():
        newwin.destroy()
    global newwin
    newwin=Tk()
    newwin.geometry("400x110")
    newwin.maxsize(width=400,height=110)
    newwin.minsize(width=400,height=110)
    newwin.wm_iconbitmap("1.ico")
    newwin.title("Find")
    frame12=Frame(newwin)
    frame12.pack(anchor=SW)
    z=Label(frame12,text="Find What:",font="lucida 9")
    z.grid(row=0,column=1,padx=5,pady=5)
    findstr=StringVar()
    ent=Entry(frame12,textvariable=findstr,font="Helvetica 13")
    ent.grid(row=0,column=2,padx=15,pady=5)
    z=Button(frame12,text="Find Next",command=findnext)
    z.grid(row=0,column=3,padx=18,pady=5)
    k=Button(frame12,text="Cancel",command=cancel,padx=9)
    k.grid(row=1,column=3,padx=18,pady=5)

    newwin.mainloop()
def replace():
    def cancel():
        secwin.destroy()
    def findnext():
        global start_pos_replace
        global endpos
        global zstrt,zend
        wordd=entrry.get()
        if wordd:
                
                start_pos_replace=TextArea.search(wordd,start_pos_replace,nocase=1,stopindex=END)
                
                find=(f"0.{str(len(wordd))}")
                endpos=eval(f"{start_pos_replace}+{find}")
                
                TextArea.tag_add("found",start_pos_replace,endpos)
                TextArea.tag_config("found",foreground='red',background="blue")

                zstrt=start_pos_replace
                zend=endpos
                
                start_pos_replace=endpos
                return zstrt,zend
                
                
    def replace():
        global zstrt,zend
        worddd=entrry.get()
        wordddd=reent.get()
        if worddd and worddd:
            print(zstrt,zend)
            
            
            TextArea.tag_delete("found",zstrt,zend)
            TextArea.delete(zstrt,zend)
            TextArea.insert(zstrt,wordddd)
            # TextArea.insert(start_pos_replace,wordddd)
    def replaceall():
        TextArea.tag_remove('found', '1.0', END)
     
    # returns to widget currently in focus
        s = entrry.get()
        r = reent.get()
     
        if (s and r):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = TextArea.search(s, idx, nocase = 1,
                            stopindex = END)
            
                if not idx: break
             
            # last index sum of current index and
            # length of text
                lastidx = '% s+% dc' % (idx, len(s))
 
                TextArea.delete(idx, lastidx)
                TextArea.insert(idx, r)
 
                lastidx = '% s+% dc' % (idx, len(r))
             
            # overwrite 'Found' at idx
                TextArea.tag_add('found', idx, lastidx)
                idx = lastidx
 
        # mark located string as red
                TextArea.tag_config('found', foreground ='green', background = 'yellow')
    
    global secwin
    secwin=Tk()
    secwin.geometry("400x110")
    secwin.maxsize(width=400,height=110)
    secwin.minsize(width=400,height=110)
    secwin.wm_iconbitmap("1.ico")
    secwin.title("Find and Replace")
    frame12=Frame(secwin)
    frame12.pack(anchor=SW)
    z=Label(frame12,text="Find What:",font="lucida 9")
    z.grid(row=0,column=1,padx=5,pady=5)
    findstrr=StringVar()
    entrry=Entry(frame12,textvariable=findstrr,font="Helvetica 13")
    entrry.grid(row=0,column=2,padx=15,pady=5)
    zc=Button(frame12,text="Find Next",command=findnext)
    zc.grid(row=0,column=3,padx=18,pady=5)
    km=Button(frame12,text="Replace",command=replace,padx=9)
    km.grid(row=1,column=3,padx=18,pady=5)
    kc=Button(frame12,text="Cancel",command=cancel,padx=9)
    kc.grid(row=2,column=2,padx=18,pady=5)
    zr=Label(frame12,text="Find What:",font="lucida 9")
    zr.grid(row=1,column=1,padx=5,pady=5)
    replacestrr=StringVar()
    reent=Entry(frame12,textvariable=replacestrr,font="Helvetica 13")
    reent.grid(row=1,column=2,padx=15,pady=5)
    kmall=Button(frame12,text="ReplaceALL",command=replaceall,padx=9)
    kmall.grid(row=2,column=3,padx=18,pady=5)

    secwin.mainloop()

def selectall():
     keyboard.press_and_release('ctrl+a')
def td():
    z=datetime.datetime.now()
    TextArea.insert("1.0",z)
def zoomin():
    global zoomcount
    global fontzoomin
    global zfont
    global impvar
    global mainzfontin
    try:
        if zoomcount==0:
  
        
            zfont=zfont.split()
            zfontin=list(zfont)
            mainzfontin=zfontin
            zfontin[1]=eval(f'{zfontin[1]}+10')
            TextArea.config(font=zfontin)
            impvar=zfontin[1]
            zoomcount=zoomcount+1

        elif zoomcount>0:
            impvar=eval(f"{impvar}+10")
            mainzfontin[1]=impvar
            TextArea.config(font=mainzfontin)
    except:
        print("Here")
        
        fontzoomin+=10
        TextArea.config(font=f'helvetica {fontzoomin}')

        
        

    
def zoomout():
    global fontzoomout
    global zfont
    global zoomcountout
    global fontzoomin
    global impvarse
    global mainzfontin
    try:
        if zoomcountout==0:
  
        
            zfont=zfont.split()
            zfontin=list(zfont)
            mainzfontin=zfontin
            zfontin[1]=eval(f'{zfontin[1]}-10')
            TextArea.config(font=zfontin)
            impvarse=zfontin[1]
            zoomcountout=zoomcountout+1

        elif zoomcountout>0:
            impvarse=eval(f"{impvarse}-10")
            mainzfontin[1]=impvarse
            TextArea.config(font=mainzfontin)
    except:
        print("Here")
        
        fontzoomout-=10
        TextArea.config(font=f'helvetica {fontzoomout}')

def defaultzoom():
    global fontzoomdefault
    global zfont
    
    TextArea.config(font=f'helvetica {fontzoomdefault}')
def status():
    global lolframe
    global count
    count+=1
    if count%2==0:
        def barupdatesecond(mouse_pos):
                lines['text'] = 'Line: ' + mouse_pos.split('.')[0]
                chars['text'] = 'Charater: ' + mouse_pos.split('.')[1]
        lolframe=Frame(root)
        lolframe.pack(side=BOTTOM)
        lines = Label(lolframe, text='Lines: ', relief='sunken', border=1, )
        lines.grid(row=0,column=5)
        chars = Label(lolframe, text='Chars: ', relief='sunken', border=1, padx=200)
        chars.grid(row=0,column=7)
        TextArea.bind('<KeyRelease>', lambda e: barupdatesecond(TextArea.index('current')))
            

    else :
        
        lolframe.destroy()
        
def viewhelp():
    msg.showinfo(title="Help" ,message="This is a simple NotePad Developed by Rohan a copy of orignal Notepad")
def feed():
    zzxc=msg.askyesno(title="Feedback",message="Please provide your expericense of using of notepad")
def about():
    msg.showinfo(title="Help" ,message="This is a simple NotePad Developed by Rohan a copy of orignal Notepad")       
root=Tk()
root.geometry("900x700")
root.title("Untitled - Notepad")
root.wm_iconbitmap("1.ico")
lolframe=Frame(root)
lolframe.pack(side=BOTTOM)
lines = Label(lolframe, text='Lines: ', relief='sunken', border=1, )
lines.grid(row=0,column=5)
chars = Label(lolframe, text='Chars: ', relief='sunken', border=1, padx=200)
chars.grid(row=0,column=7)


# -----------------------------ADD Menu
rdi=IntVar()
rdi.set(1)

mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
editmenu=Menu(mainmenu,tearoff=0)
formatmenu=Menu(mainmenu,tearoff=0)
savmenu=Menu(filemenu,tearoff=0)
viewmenu=Menu(mainmenu,tearoff=0)
zoommenu=Menu(viewmenu,tearoff=0)

helpmenu=Menu(mainmenu,tearoff=0)
helpmenu.add_command(label="viewHelp",command=viewhelp)
helpmenu.add_command(label="Send FeedBack",command=feed)
helpmenu.add_separator()
helpmenu.add_command(label="About Notepas",command=about)

filemenu.add_command(label="New",command=new)
filemenu.add_command(label="New Window",command=newwindow)
filemenu.add_command(label="Open",command=open1)
filemenu.add_separator()
editmenu.add_command(label="Undo",command=undo)
editmenu.add_separator()
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)

editmenu.add_command(label="Delete",command=delete)
editmenu.add_separator()
editmenu.add_command(label="Find",command=find)
editmenu.add_command(label="Replace",command=replace)
editmenu.add_separator()
editmenu.add_command(label='Select All',command=selectall)
editmenu.add_command(label="Time Date",command=td)
savmenu.add_command(label="Save",command=save)
savmenu.add_command(label="Save As",command=saveas)
filemenu.add_cascade(label='Save',menu=savmenu)
filemenu.add_command(label="Exit",command=exit1)
formatmenu.add_command(label="Font",command=formatt)
zoommenu.add_command(label="Zoom In",command=zoomin)
zoommenu.add_command(label="Zoom Out",command=zoomout)
zoommenu.add_command(label="Restore Default Zoom",command=defaultzoom)
viewmenu.add_checkbutton(label="StatusBar",variable=rdi, command=status)

viewmenu.add_cascade(label="Zoom",menu=zoommenu)

mainmenu.add_cascade(label="File",menu=filemenu)
mainmenu.add_cascade(label="Edit",menu=editmenu)

mainmenu.add_cascade(label='Format',menu=formatmenu)
mainmenu.add_cascade(label="View",menu=viewmenu)
mainmenu.add_cascade(label="Help",menu=helpmenu)
root.config(menu=mainmenu)


#------------------------------------------------------------------------------------------



#Add TextArea
TextArea = Text(root, font="lucida 13",undo=TRUE)
TextArea.pack(expand=True,fill=BOTH)
TextArea.bind('<KeyRelease>', lambda e: barupdate(TextArea.index('current')))

file=None
z=Scrollbar(TextArea)
z.pack(side=RIGHT,fill=Y)
z.config(command=TextArea.yview)
TextArea.config(yscrollcommand=z.set)
file = None
root.mainloop()