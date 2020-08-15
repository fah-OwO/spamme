import subprocess
import win32clipboard
import time
import win32api,win32con
import codecs



f1=open('C:\\Users\\msi\\Desktop\\spammer.txt','a')
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
        subprocess.call(['C:\\Windows\\Notepad.exe','C:\\Users\\msi\\Desktop\\spammer.txt'])
        time.sleep(0.5)
        f2=codecs.open('C:\\Users\\msi\\Desktop\\spammer.txt', 'r', 'utf8')# f2=open('C:\\Users\\msi\\Desktop\\spammer.txt','r')
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
                # time.sleep(3)
                if frth%8==7:
                    time.sleep(12)# here you can change your time sleep your slef
            else:
                time.sleep(0.33)
            frth+=1
        f2.close()
if __name__ == "__main__":
    spamme()
# try place this on .txt file after running this
# ╔═══════
# ║
# ║
# ╠═════
# ║
# ║
# ║
