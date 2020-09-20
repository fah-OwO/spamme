import subprocess
import win32clipboard
import time
import win32api,win32con
import tkinter as tk
import os
root = tk.Tk()
__location__=os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def sc(data):
    root.clipboard_clear()
    root.clipboard_append(data)
    print (data)
def kbt(dat):
    win32api.keybd_event(dat, 0,0,0)
    time.sleep(.05)
    win32api.keybd_event(dat,0 ,win32con.KEYEVENTF_KEYUP ,0)

wait='<wait'

def spamme(w):
    time.sleep(0.5)
    for i in w.split('\n'):
        
        t=.015
        a=i.find(wait)
        if a>=0:
            x,y=a,i.find('>',a)
            if y>0:
                t=i[a+len(wait):y]
                i=i[:a]+i[y+1:]
                t=float(t)
        if not len(i)<1:
            try:
                sc(i)
            except :
                print('error');continue
            win32api.keybd_event(0x11, 0,0,0)
            win32api.keybd_event(0x56, 0,0,0)
            time.sleep(.15)
            win32api.keybd_event(0x56,0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(0x11,0 ,win32con.KEYEVENTF_KEYUP ,0)
            kbt(0x0D)
        time.sleep(t)
    
def tkwindow():
    def loadTXTfile():
        with open(os.path.join(__location__,'spammer.txt'),mode='a+', encoding='utf-16') as file:
            file.seek(0,0)
            w=file.read()
            file.close()
            text.delete(1.0,"end")
            text.insert(1.0, w)
    def setTXTfile():
        with open(os.path.join(__location__,'spammer.txt'),"w", encoding='utf-16') as file:
            file.write(text.get("1.0","end-1c"))
            file.close()
    def send():
        root.withdraw()     
        spamme(text.get("1.0","end-1c"))
        root.deiconify()
    
    root.configure(background='#482a10')
    root.title("spamme")
    root.attributes("-topmost", True)
    root.bind('<Escape>', lambda e: root.quit())
    text = tk.Text(root,height=12,width=30,font="Sans 24",padx=30,pady=30)
    text.grid(row=0,rowspan=12,column=1)
    loadTXTfile()
    send= tk.Button(text="Send",command=send,height=6,width=6,font="Sans 18")
    send.grid(row=0,rowspan=6,column=2)
    save= tk.Button(text="save to txt",command=setTXTfile,height=3,width=10,font="Sans 18")
    save.grid(row=6,rowspan=3,column=0)
    save= tk.Button(text="load from txt",command=loadTXTfile,height=3,width=10,font="Sans 18")
    save.grid(row=9,rowspan=3,column=0)
    root.mainloop()
if __name__ == "__main__":
    tkwindow()

# try place this on .txt file after running this
# ╔═══════
# ║
# ║
# ╠═════
# ║
# ║
# ║
