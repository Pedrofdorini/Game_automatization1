import pyautogui
import keyboard

def print_mouse_position():
    contagem=1
    posicao = pyautogui.position()
    print(f"A posição do mouse no momento {contagem} {posicao}")
    contagem+=1

# Inicia a função para monitorar a tecla "x" e imprimir a posição do mouse
keyboard.add_hotkey("x", print_mouse_position)

# Mantém o programa em execução para monitorar o pressionamento de teclas
keyboard.wait("esc")
