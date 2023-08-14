import pytesseract
from PIL import Image
import pyautogui
import webbrowser
import time
import re
import os


def contagem_regressiva(tempo1, tempo2):

    print(f"Tempo 1: {tempo1} segundos")
    print(f"Tempo 2: {tempo2} segundos")

    while tempo1 > 0 and tempo2 > 0:
        print(f"Tempo 1: {tempo1} segundos | Tempo 2: {tempo2} segundos")
        time.sleep(1)
        tempo1 -= 1
        tempo2 -= 1

    if tempo1 == 0:
        print("Tempo 1 chegou a zero!")
        pass# Coloque aqui o código que você deseja executar quando o tempo1 chegar a zero

    if tempo2 == 0:
        print("Tempo 2 chegou a zero!")
        pass# Coloque aqui o código que você deseja executar quando o tempo2 chegar a zero
def localizar_clicar_imagem_especifica(nome_arquivo):

    while True:
        imagem = pyautogui.locateOnScreen(nome_arquivo)
        if imagem is not None:
            coordenadas = pyautogui.center(imagem)
            pyautogui.click(coordenadas)
            print(f"A imagem {nome_arquivo} foi encontrada e clicada nas coordenadas {coordenadas}")
        else:
            break
def capturar_imagem(nome_arquivo,x,y,width,height):

    imagem = pyautogui.screenshot(region=(x, y, width, height))

    # Salvar a imagem como arquivo
    imagem.save(nome_arquivo)
    return nome_arquivo
def converter_tempo(tempo):

    # Filtrar apenas os caracteres válidos usando uma expressão regular
    tempo_filtrado = re.sub(r'[^\dsmh]', '', tempo)

    segundos = 0

    # Verificar se há dias no tempo
    if 'd' in tempo_filtrado:
        dias, tempo_filtrado = tempo_filtrado.split('d')
        segundos += int(dias) * 24 * 60 * 60

    # Verificar se há horas no tempo
    if 'h' in tempo_filtrado:
        horas, tempo_filtrado = tempo_filtrado.split('h')
        segundos += int(horas) * 60 * 60

    # Verificar se há minutos no tempo
    if 'm' in tempo_filtrado:
        try:
            minutos, tempo_filtrado = tempo_filtrado.split('m')
            segundos += int(minutos) * 60
        except ValueError:
            pass

    # Verificar se há segundos no tempo
    if 's' in tempo_filtrado:
        segundos_str = tempo_filtrado.replace('s', '')
        try:
            segundos += int(segundos_str)
        except ValueError:
            pass

    return segundos
def aguardar_tempo(tempo):

    # Converte o tempo fornecido em segundos
    segundos = converter_tempo(tempo)

    # Loop que aguarda até que o temporizador seja concluído
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos")
        time.sleep(1)  # Aguarda 1 segundo
        segundos -= 1

    print("Temporizador concluído!")
def abrir_steam_jogo(id_jogo):
    try:
        url = f"steam://rungameid/{id_jogo}"
        webbrowser.open(url)
        print("O jogo foi aberto com sucesso na Steam!")
    except Exception as e:
        print(f"Erro ao abrir o jogo: {e}")

def verificar_e_clicar_imagem(nome_arquivo):
    imagem = pyautogui.locateOnScreen(nome_arquivo,confidence=0.8)
    if imagem is not None:
        # Obter as coordenadas do centro da imagem
        coordenadas = pyautogui.center(imagem)
        
        # Clicar no centro da imagem
        pyautogui.click(coordenadas)
        
        print(f"A imagem {nome_arquivo} foi encontrada e clicada nas coordenadas {coordenadas}")
        
        # Verificar se é a imagem "Robo.png" e sair do loop
        if nome_arquivo == "Robo.png":
            return True
    
    return False

def localizar_clicar():
    imagens = ["Atualizar.png", "sim.png", "x_preto.png", "X.png","XVermelho.png"]
    while True:
        # Procurar a imagem "Robo.png" na tela
        imagem_robo = pyautogui.locateOnScreen("Robo.png")
        
        # Verificar se a imagem "Robo.png" foi encontrada
        if imagem_robo is not None:
            print("Imagem 'Robo.png' encontrada!")
            break
        
        # Verificar e clicar nas outras imagens de forma aleatória
        for nome_arquivo in imagens:
            if verificar_e_clicar_imagem(nome_arquivo):
                break
        
        # Clicar na coordenada (1865, 53)
    
    print("Até aqui está correto")
# Diretório onde estão as imagens
while True:
# Exemplo de uso
 id_jogo = 767560
 abrir_steam_jogo(id_jogo)
#vai entrar ir para tela incial
 localizar_clicar()
 print("até aqui veio")

#os fragmentos
 pyautogui.click(59, 591)
 time.sleep(3)
 pyautogui.click(1718, 1017)
 time.sleep(5)

#verificar se já é possível botar os fragmentos

# Capturar a imagem

 
 Obter_encontrada= pyautogui.locateOnScreen("Obter.png",confidence=0.8)
 if Obter_encontrada:
     for _ in range(2):
       pyautogui.click(551, 533)
       time.sleep(1)
       pyautogui.click(591, 834)
       time.sleep(1)
       pyautogui.click(1002,539)
       time.sleep(1)
       pyautogui.click(1026, 819)
       time.sleep(1)
       pyautogui.click(1495, 528)
       time.sleep(3)
 imagem2=capturar_imagem("imagem2.png", 532, 437, 120, 38)
 imagem2 = Image.open("imagem2.png")


# Carregar a imagem capturada
 imagem2_texto = pytesseract.image_to_string(imagem2)
 print(imagem2_texto)
 tempo2=converter_tempo(imagem2_texto)
 pyautogui.hotkey("alt","f4")
 contagem_regressiva(tempo2, tempo2)


#volta para tela inicial
