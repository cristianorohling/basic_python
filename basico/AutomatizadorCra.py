import pyautogui
import time

TempoEsperar = 3

#Failsafe
pyautogui.PAUSE = 0.3

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(TempoEsperar)

pyautogui.write('https://crapr.crabr.com.br/crapr/site/admin.php')    
pyautogui.press("enter")

time.sleep(TempoEsperar)

pyautogui.getWindowsWithTitle("CRA - Central de Remessa de Arquivos")[0].maximize()

#Clica em Entrar
pyautogui.click(x=1176, y=458)

time.sleep(TempoEsperar)

#Aciona o menu Relatorio
pyautogui.click(x=105, y=692)

#Aciona o botão "Relatorio"
pyautogui.click(x=118, y=713)
time.sleep(TempoEsperar)

#Clicar na Caixa de Seleção
pyautogui.click(x=721, y=320)
time.sleep(TempoEsperar)
pyautogui.write('Remessa')
time.sleep(TempoEsperar)
pyautogui.press("enter")

#Clicar na primeira data
pyautogui.click(x=634, y=369)
pyautogui.write('01082018')
pyautogui.press('tab')
#Selecionar data atual
pyautogui.click(x=889, y=645)

#Selecionar "Analítica Detalhada"
pyautogui.click(x=771, y=492)
time.sleep(TempoEsperar)
pyautogui.click(x=771, y=492)
time.sleep(TempoEsperar)
pyautogui.click(x=771, y=492)
time.sleep(TempoEsperar)

#Selecionar CSV
time.sleep(TempoEsperar)
pyautogui.click(x=767, y=550)