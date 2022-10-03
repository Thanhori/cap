import pyautogui as pg
import time
import random
import io
import pyperclip
f=open("1.txt","w",encoding="utf-8")
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~!@#$%^&*()."

string = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(string, length)) 


for i in password:
  str = i
  f.write(i)
  f.write("")
  f.close
#nơi sản xuất mật khẩu

