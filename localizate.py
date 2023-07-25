import pyautogui
import keyboard

posicao1 = None
posicao2 = None
contador = 0
def on_press_x(event):
    global posicao1, posicao2, contador

    contador += 1
    if contador == 1:
        posicao1 = pyautogui.position()
        print(f"A posição do primeiro clique é {posicao1}")
    elif contador == 2:
        posicao2 = pyautogui.position()
        print(f"A posição do segundo clique é {posicao2}")
        diferenca = (posicao2[0] - posicao1[0], posicao2[1] - posicao1[1])
        print(f"Diferença: {diferenca}")
        # Encerra o programax
        keyboard.unhook_all()

keyboard.on_press_key("x", on_press_x)

# Mantém o programa em execução para monitorar o pressionamento de teclas
keyboard.wait("esc")