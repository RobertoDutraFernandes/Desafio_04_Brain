import pytesseract
import cv2
import numpy as np

# Definir o caminho do executável Tesseract trabalho
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/ADM/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
# Definir o caminho do executável Tesseract casa
# pytesseract.pytesseract.tesseract_cmd = r"C:/Users/Pichau/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"


# Carregar a imagem trabalho
#cnh = cv2.imread("C:/Users/ADM/Downloads/desafio_04_brain-20240628T105720Z-001/desafio_04_brain/cnh_boa.jpg")
# carregar a imagem casa
cnh = cv2.imread("./modelo_cnh1.jpg")

# Separar a imagem em faixas horizontais
height, width = cnh.shape[:2]
start1 = 0
end1 = height // 30
start2 = end1
end2 = 2 * end1
start3 = end2
end3 = 3 * end1
start4 = end3
end4 = 4 * end1
start5 = end4
end5 = 5 * end1
start6 = end5
end6 = 6 * end1
start7 = end6
end7 = 7 * end1
start8 = end7
end8 = 8 * end1
start9 = end8
end9 = 9 * end1
start10 = end9
end10 = 10 * end1
start11 = end10
end11 = 11 * end1
start12 = end11
end12 = 12 * end1
start13 = end12
end13 = 13 * end1
start14 = end13
end14 = 14 * end1
start14_5 = (14 * end1) - 10
start15 = end14
end15 = 15 * end1
start16 = end15
end16 = 16 * end1
start17 = end16
end17 = 17 * end1
start18 = end17
end18 = 18 * end1
start19 = end18
end19 = 19 * end1
start20 = end19
end20 = 20 * end1
start21 = end20
end21 = 21 * end1
start22 = end21
end22 = 22 * end1
start23 = end22
end23 = 23 * end1
start24 = end23
end24 = 24 * end1
start25 = end24
end25 = 25 * end1
start26 = end25
end26 = 26 * end1
start27 = end26
end27 = 27 * end1
start28 = end27
end28 = 28 * end1
start29 = end28
end29 = 29 * end1
start30 = end29
end30 = 30 * end1


# Separar a imagem em faixas verticais
height, width = cnh.shape[:2]
vstart1 = 0
vend1 = width // 20
vstart2 = vend1
vend2 = 2 * vend1
vstart3 = vend2
vend3 = 3 * vend1
vstart4 = vend3
vend4 = 4 * vend1
vstart5 = vend4
vend5 = 5 * vend1
vstart6 = vend5
vend6 = 6 * vend1
vstart7 = vend6
vend7 = 7 * vend1
vstart8 = vend7
vend8 = 8 * vend1
vstart9 = vend8
vend9 = 9 * vend1
vstart10 = vend9
vend10 = 10 * vend1
vstart11 = vend10
vend11 = 11 * vend1
vstart12 = vend11
vend12 = 12 * vend1
vstart13 = vend12
vend13 = 13 * vend1
vstart13_5 = (13 * vend1) - 15
vstart14 = vend13
vend14 = 14 * vend1
vstart15 = vend14
vend15 = 15 * vend1
vstart16 = vend15
vend16 = 16 * vend1
vstart17 = vend16
vend17 = 17 * vend1
vstart18 = vend17
vend18 = 18 * vend1
vstart19 = vend18
vend19 = 19 * vend1
vstart20 = vend19
vend20 = 20 * vend1

# Selecionar somente a parte desejada
nome = cnh[start7:end9, vstart4:vend12]
p_hab = cnh[ start7:end9, vstart17:vstart20]

nasc = cnh[start10:end11, vend8:vend15]

data_em = cnh[start12:end14, vend9:vend12]
validade = cnh[start12:end14, vstart14:vstart17]

doc = cnh[start14_5:end16, vstart9:vstart17]

cpf = cnh[start17:end18, vstart9:vstart13_5]
rg = cnh[start17:end18, vstart14:vstart17]
cat = cnh[start17:end18, vstart18:vstart20]

nacionalidade = cnh[start19:end21, vstart9:vstart15]

filiacao = cnh[ start21:end28, vstart9:vend15]

info = [nome, p_hab, nasc, data_em, validade, doc, cpf, rg, cat, nacionalidade, filiacao]

"""
for var in info:

    # Converter a imagem para escala de cinza e binarizar com limiar fixo
    gray = cv2.cvtColor(var, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    gaussian = cv2.GaussianBlur(binary_image, (9, 9), 10.0)
    unsharp_image = cv2.addWeighted(gray, 1.8, gaussian, -0.5, 0)


    custom_config = r'--oem 3 --psm 1'
    # Extrair texto da imagem binarizada
    text = pytesseract.image_to_string(unsharp_image, config=custom_config, lang='por')

    cv2.imshow('Processed Image', unsharp_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(text)
"""
for var_v in info:
    # Converter a imagem para escala de cinza 
    gray = cv2.cvtColor(var_v, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)

    # Usar gamma para aumentar o contraste
    gamma = 2
    adjusted = np.uint8(np.clip((gray / 200.0) ** gamma * 280.0, 0, 255))


    custom_config = r'--oem 3 --psm 1'
    # Extrair texto da imagem
    text = pytesseract.image_to_string(adjusted, config=custom_config, lang='por')

    print(text)
    cv2.imshow('Processed Image', adjusted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
"""teste --psm config:
1 (PSM_AUTO): Tesseract determina automaticamente a estrutura da página e faz a segmentação.
2 (PSM_SINGLE_BLOCK): Tesseract assume que há um único bloco de texto na imagem.
3 (PSM_SINGLE_LINE): Tesseract trata a imagem como contendo apenas uma linha de texto.
4 (PSM_SINGLE_WORD): Tesseract tenta reconhecer palavras individuais.
5 (PSM_SINGLE_CHAR): Tesseract tenta reconhecer caracteres individuais.
6 (PSM_SPARSE_TEXT): Tesseract trata a imagem como contendo um texto disperso, com várias linhas de texto.
7 (PSM_SPARSE_TEXT_OSD): Tesseract trata a imagem como contendo um texto disperso com detecção de orientação e script.
8 (PSM_RAW_LINE): Tesseract trata a imagem como um único bloco de texto, mas faz reconhecimento de linha sem segmentação.
9 (PSM_COUNT): Indica o número total de modos de segmentação.
10 (PSM_SPARSE_TEXT_OEM): Tesseract trata a imagem como contendo um texto disperso e usa o modo OEM.
11 (PSM_AUTO_ONLY): Tesseract determina automaticamente a estrutura da página.
 """
