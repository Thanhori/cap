import pyautogui as pg
import random
import io
import pyperclip


txt = io.open("1.txt", mode="r", encoding="utf-8")


for i in txt:
  str = i
  pyperclip.copy(str)
  pg.hotkey("ctrl", "v")
  pg.press('Enter')