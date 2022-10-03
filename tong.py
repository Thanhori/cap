from subprocess import call
from tkinter import *
import time
import pyautogui
#--------- def ---------#
def click():
	time.sleep(2)
	for a in range(1000000):
		call(["python", "test.py"])
		call(["python", "s.py"])
#--------- Button ---------#
root = Tk()
root.geometry("700x350")
root.title("Check Pass")
root.iconbitmap(r'p1.ico')
root.config(background='#1a1616')
bg = PhotoImage(file="2.png")
#label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
b1 = Button(root,text='Check Pass')
b1.place(x=15,y=300)
b1.config(font=('Comic Sans MS Italic',12,'bold'))
b1.config(command=click)
b1.config(bg='#32323d')
b1.config(fg='#a19999')
b2 = Button(root,text='Auto Click')
b2.place(x=155,y=300)
b2.config(font=('Comic Sans MS Italic',12,'bold'))
b2.config(command=click)
b2.config(bg='#32323d')
b2.config(fg='#a19999')
root.resizable(False, False)

root.mainloop()
#--------- Button ---------#

