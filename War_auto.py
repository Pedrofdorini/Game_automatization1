import pytesseract
from PIL import Image
import pyautogui
import webbrowser
import time
import numpy as np

def verificar_imagem_aprimorar(imagem):
    for i in range(3):
    # procurar imagem aprimorar na tela
       imagem_aprimorar= pyautogui.locateOnScreen("Aprimorar.png",grayscale=True, confidence=0.8)
       if imagem_aprimorar is not None:
          return True
       else:
          time.sleep(2)
    print("A imagem 'Aprimorar.png' não foi encontrada após 3 tentativas.")
    return False
        
def verificar_imagem_na_tela(imagens, tempo_limite=10):
    tentativas = tempo_limite // 2  # Realizar tentativas a cada 2 segundos
    coordenadas_imagens = {}
    for _ in range(tentativas):
        # Procurar as imagens na tela
        for imagem in imagens:
            imagens_encontradas = list(pyautogui.locateAllOnScreen(imagem, grayscale=True, confidence=0.8))
            if imagens_encontradas:
                if imagem not in coordenadas_imagens:
                    coordenadas_imagens[imagem] = []
                coordenadas_imagens[imagem].extend(imagens_encontradas)
        if coordenadas_imagens:
            time.sleep(2)  # Aguardar 2 segundos antes de tentar novamente
        else:
            break
    return coordenadas_imagens

def imagens_sao_iguais(imagem1, imagem2):
    # Carregar as duas imagens usando a PIL
    img1 = Image.open(imagem1)
    img2 = Image.open(imagem2)

    # Converter as imagens para arrays numpy
    array1 = np.array(img1)
    array2 = np.array(img2)

    # Comparar os arrays numpy pixel a pixel
    if np.array_equal(array1, array2):
        return True
    else:
        return False

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
    segundos = 0

    # Verificar se há dias no tempo
    if 'd' in tempo:
        dias, tempo = tempo.split('d')
        segundos += int(dias) * 24 * 60 * 60

    # Verificar se há horas no tempo
    if 'h' in tempo:
        horas, tempo = tempo.split('h')
        segundos += int(horas) * 60 * 60

    # Verificar se há minutos no tempo
    if 'm' in tempo:
        try:
            minutos, tempo = tempo.split('m')
            segundos += int(minutos) * 60
        except ValueError:
            pass

    # Verificar se há segundos no tempo
    if 's' in tempo:
        segundos_str = tempo.replace('s', '')
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
    imagem = pyautogui.locateOnScreen(nome_arquivo)
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

# Exemplo de uso
id_jogo = 767560
abrir_steam_jogo(id_jogo)
#vai entrar ir para tela incial
localizar_clicar()
print("até aqui veio")
imagem="Aprimorar.png"

if verificar_imagem_aprimorar(imagem):
    time.sleep(2)
    pyautogui.click(1615,569)
else:
    pass

imagem1 = capturar_imagem("imagem1.png", 908, 163, 99, 32)
imagem1 = Image.open("imagem1.png")
tempo1 = pytesseract.image_to_string(imagem1)

#os fragmentos
time.sleep(3)
pyautogui.click(59, 591)
time.sleep(3)
pyautogui.click(1718, 1017)
time.sleep(5)

#verificar se já é possível botar os fragmentos

# Capturar a imagem

imagens_procurar = ["Obter.png", "Repetir_Khepri.png"]
tempo_limite = 10
coordenadas_imagens = verificar_imagem_na_tela(imagens_procurar, tempo_limite)
for imagem, coordenadas_encontradas in coordenadas_imagens.items():
    if coordenadas_encontradas:
        print(f"A imagem {imagem} foi encontrada com sucesso!")
        for coordenadas in coordenadas_encontradas:
            centro_imagem = pyautogui.center(coordenadas)
            time.sleep(2)
            pyautogui.click(centro_imagem)
            print(f"Clicou no meio da imagem {imagem} nas coordenadas {centro_imagem}")
    else:
        print(f"A imagem {imagem} não foi encontrada na tela.")

  

imagem2=capturar_imagem("imagem2.png", 542, 444, 110, 24)
imagem2 = Image.open("imagem2.png")


# Carregar a imagem capturada
imagem2_texto = pytesseract.image_to_string(imagem2)
tempo2 = converter_tempo(imagem2_texto)


pyautogui.hotkey("alt", "f4")

#volta para tela inicial
