import webbrowser
import pyautogui
from time import sleep
import keyboard

def encontrar_e_click_simples(imagem):
    from PIL import ImageGrab
    from functools import partial

    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
    coord = pyautogui.locateCenterOnScreen(imagem)
    pyautogui.click(coord[0], coord[1], clicks=1, duration=1, button='left')

# Abre uma nova guia no site do jogo:
webbrowser.open('https://guitarflash.com/')
sleep(6)
# clicar no botão jogar:
pyautogui.click(2097, 392,duration=1)
sleep(5)
# Clicar no nivel e na musica:
encontrar_e_click_simples('nivel.PNG')
pyautogui.click(2093, 879, duration=2)
sleep(5)
# Rolar a para alinhar com as coordenadas:
pyautogui.scroll(-200)
sleep(10)
# Clicar na tecla space para começar a jogar:
pyautogui.press('space')
sleep(4.5)
# Reconhece se o disco está na coordenada necessária para pressionar a respectiva tecla:
while keyboard.is_pressed('space') == False:
    if pyautogui.pixelMatchesColor(2134, 823,(0, 152, 0)):
        pyautogui.press('a')
        sleep(0.095)
    if pyautogui.pixelMatchesColor(2225, 824,(255, 0, 0)):
        pyautogui.press('s')
        sleep(0.095)
    if pyautogui.pixelMatchesColor(2300, 820, (244, 244, 2)):
        pyautogui.press('j')
        sleep(0.095)
