"""name - 1436, 360
email - 1410, 406
bt - 1437, 438
"""
import pyautogui
from time import sleep

with open("files/alunos.txt", "r", encoding="utf-8") as file:
    for line in file:
        nome = line.split(",")[0]
        email = line.split(",")[1]
        pyautogui.click(1436, 360, duration=0.70)
        pyautogui.write(nome)
        pyautogui.click(1410, 406, duration=0.70)
        pyautogui.write(email)
        pyautogui.click(1437, 438, duration=0.4)
        pyautogui.screenshot(f"files/img/{nome}.png")
        sleep(1)
        