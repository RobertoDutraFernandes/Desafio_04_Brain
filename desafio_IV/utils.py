import pytesseract
import cv2
import numpy as np


# Definir o caminho do executável Tesseract caso esteja no windows
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/Pichau/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

def processar_img(img):
    cnh = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

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
    nome = cnh[start1:end4, vstart1:vend15]
    primeira_habilitacao = cnh[ start1:end4, vstart17:vend20]

    informacoes_de_nascimento = cnh[start5:end8, vstart8:vend17]

    data_de_emissao = cnh[start8:end12, vstart8:vend12]
    validade = cnh[start8:end12, vstart12:vend17]

    doc_identidade = cnh[start12:end15, vstart8:vstart17]

    cpf = cnh[start15:end18, vstart8:vend13]
    rg = cnh[start15:end18, vstart14:vend17]
    cat_hab = cnh[start15:end18, vstart18:vstart20]

    nacionalidade = cnh[start19:end21, vstart8:vstart15]

    filiacao = cnh[ start22:end30, vstart8:vend20]

    info = {"Nome:":nome, "1ª habilitacao:":primeira_habilitacao, "Informacoes de nascimento:":informacoes_de_nascimento, "Data de emissao:":data_de_emissao,
            "Validade:":validade, "Doc. identidade:":doc_identidade, "Cpf:":cpf, "rg:":rg, "Cat_hab:":cat_hab, "Nacionalidade:":nacionalidade, "Filiação:":filiacao}

    for var_name, var_v in info.items():
        # Converter a imagem para escala de cinza 
        gray = cv2.cvtColor(var_v, cv2.COLOR_BGR2GRAY)
        equ = cv2.equalizeHist(gray)

        # Usar gamma para aumentar o contraste
        gamma = 2
        adjusted = np.uint8(np.clip((gray / 200.0) ** gamma * 280.0, 0, 255))


        custom_config = r'--oem 3 --psm 1'
        # Extrair texto da imagem
        text = pytesseract.image_to_string(adjusted, config=custom_config, lang='por')
        print(var_name)
        print(text + '\n')
        cv2.imshow('Processed Image', adjusted)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        