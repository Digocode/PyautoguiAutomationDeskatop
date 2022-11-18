import pyautogui
import time
from tkinter import *

janela = Tk()
janela.title("Primocast")
janela.geometry("80x80")



def primocast():
    pyautogui.moveTo(1752,11, duration= 0.5)
    pyautogui.click()
    pyautogui.doubleClick(48,391, duration=0.5)
    time.sleep(1)
    pyautogui.doubleClick(595,41, duration=0.5)
    time.sleep(1)
    pyautogui.write("youtube.com")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(823,143)
    pyautogui.write("primo cast")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(763,382)


botao = Button(janela, text='executar', command=primocast)
botao.pack()
janela.mainloop()
janela.quit
