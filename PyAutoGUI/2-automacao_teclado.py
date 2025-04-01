import pyautogui
import time

# pyautogui.write("Ola mundo!")
pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("calculadora", interval=0.10)
pyautogui.press("enter")

# Minimiza janela
pyautogui.moveTo(1780, 16, duration=0.7)
time.sleep(1)
pyautogui.click()

# Fecha janela
# pyautogui.keyDown('alt')
# pyautogui.press('f4')

# Tecla de atalho
# pyautogui.hotkey("ctrl", "shift", "esc")

pyautogui.keyDown("winleft")
pyautogui.press(["left"])
time.sleep(2)
pyautogui.keyDown("winleft")
pyautogui.press(["right"])