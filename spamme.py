import subprocess
import win32clipboard
import time
import win32api,win32con
import os
__location__=os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f1=open(os.path.join(__location__,'spammer.txt'),mode='a', encoding='utf-16')
f1.close()
def sc(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data,win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    print (data)
def kbt(dat):
    win32api.keybd_event(dat, 0,0,0)
    time.sleep(.05)
    win32api.keybd_event(dat,0 ,win32con.KEYEVENTF_KEYUP ,0)

def spamme():
    while True:
        subprocess.call(['C:\\Windows\\Notepad.exe',os.path.join(__location__,'spammer.txt')])

        time.sleep(0.5)
        f2=open(os.path.join(__location__,'spammer.txt'),mode='r', encoding='utf-16')
        w=f2.read()
        if w=='':
            break
        frth=0
        for i in w.split('\n'):
            if('exit' in i):
                print('exit')
                return
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
            if frth%4==3:
                time.sleep(1)       # EDIT
                if frth%8==7:
                    time.sleep(12)  # time.sleep
            else:
                time.sleep(0.15)    # up on your purpose
            frth+=1
        f2.close()
if __name__ == "__main__":
    spamme()
# try this
# ╔═══════
# ║
# ║
# ╠═════
# ║
# ║
# ║
