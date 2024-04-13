import pyautogui

#dar uma pausa de 2 segundos para cada comando
pyautogui.PAUSE = 2

#abrir o "programa"
pyautogui.press('win')
pyautogui.write('login.xlsx')
pyautogui.press('enter')

#preencher os dados
pyautogui.click(x=554, y=331)
pyautogui.write('Nome')
pyautogui.press('enter')
pyautogui.write('1234')

#clicar em logar
pyautogui.click(x=473, y=513)
