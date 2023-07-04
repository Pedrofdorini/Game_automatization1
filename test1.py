import pytesseract
from PIL import Image
import pyautogui
import webbrowser
import time

def capturar_imagem():
    # Obter as coordenadas do local de captura
    x = 542  # coordenada x do canto superior esquerdo
    y = 444  # coordenada y do canto superior esquerdo
    width = 110  # largura da área de captura
    height = 24  # altura da área de captura
        # Capturar a tela na área especificada
    imagem = pyautogui.screenshot(region=(x, y, width, height))

    # Salvar a imagem como arquivo
    imagem.save('imagem.png')

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
        minutos, tempo = tempo.split('m')
        segundos += int(minutos) * 60

    # Verificar se há segundos no tempo
    if 's' in tempo:
        segundos_str = tempo.replace('s', '')
        segundos += int(segundos_str)

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


def localizar_robo():
    while True:
        # Procurar a imagem na tela
        time.sleep(3)
        imagem = pyautogui.locateOnScreen("Robo.png")
        
        # Verificar se a imagem foi encontrada
        if imagem is not None:
            print("Imagem encontrada!")
            break
        
        # Clicar na coordenada (1865, 53)
        pyautogui.click(1865, 53)
        print("Clicando na tela...")
        imagem2=pyautogui.locateOnScreen("sim.png")
        if imagem2!=None:
          imagem_coord=pyautogui.center(imagem2)
          pyautogui.click(imagem_coord)
        print("Até aqui ta certo")
        

def abrir_steam_jogo(id_jogo):
    try:
        url = f"steam://rungameid/{id_jogo}"
        webbrowser.open(url)
        print("O jogo foi aberto com sucesso na Steam!")
    except Exception as e:
        print(f"Erro ao abrir o jogo: {e}")

def verificar_imagem(nome_arquivo):
    tentativas=0
    while True:
        # Procurar a imagem na tela
        first = pyautogui.locateOnScreen(nome_arquivo)
        tentativas=tentativas+1
        
        # Verificar se a imagem foi encontrada
        if first is not None:
            # Obter as coordenadas do centro da imagem
            coordenadas = pyautogui.center(first)
            pyautogui.click(coordenadas)
            print("Primeira etapa concluída")
            print (f"O número de tentativas para primeira parte foi {tentativas}")
            # Faça o que for necessário com as coordenadas encontradas
            
            # Sair do loop
            break
        
        # Aguardar um tempo antes de verificar novamente
        time.sleep(1)

# Exemplo de uso
id_jogo = 767560
abrir_steam_jogo(id_jogo)
nome_arquivo="Atualizar.png"
verificar_imagem(nome_arquivo)
localizar_robo()
print("robo localizado")
pyautogui.click(59,591)
time.sleep(2)
pyautogui.click(1718,1017)
time.sleep(2)
# Capturar a imagem
capturar_imagem()

# Carregar a imagem capturada
imagem = Image.open('imagem.png')
tempo = pytesseract.image_to_string(imagem)
aguardar_tempo(tempo)

