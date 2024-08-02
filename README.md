# Desafio_04_Brain
Desafio de visão computacional

# Objetivo:
O desafio 4 proposto pelo BRAIN, consiste no desenvolvimento  e treinamento de um modelo de visão computacional, que possui como base um DataSet que contém um conjunto de imagens de CNHs, a partir destas, visa-se extrair informações de uma CNH inserida através de uma imagem baixada ou obtida através de uma webcam. Para isto o projeto foi dividido em 2 partes, sendo a primeira a extração de dados de uma imagem específica e a segunda a extração de dados de uma imagem obtida através de uma WebCam.

# Extrair informações de uma imagem (1ª parte):
## utils_modelo1 e utils_modelo2:
Estes são 2 códigos diferentes, que são responsáveis por fazer o reconhecimento de textos em 2 tipos diferentes de modelos de CNHs.

### Bibliotecas necessárias:
Para pode realizar isto é necessário a utilização de algumas bibliotecas principais para lidar com a imagem, sendo elas, pytesseract, que responsável pela extração de textos e, cv2 (OpenCV), que é responsável por fazer o processamento.

### Código
Após a instalação de todas as dependências, é realizado a repartição da imagens em diferentes quadrantes, verticais e horizontais. Tendo estes separados, para definição de cada campo da imagem, é feita a seleção das partes correspondentes a cada box de informação da CNH, posteriormente, passa-se um filtro para transformação na imagem, tornando ela em uma de escala preto e branco (tons de cinza) e aumenta-se o contraste dela para facilitar o reconhecimento de textos. Para finalizar, com a imagem processada, é feita uma iteração com os campos definidos anteriomente, para que seja feito a extração do texto presente naquele local. 

# Extrair informações da WebCam (2ª parte):
## Etapa I - Desenvolvimento do DataSet e do modelo

### DataSet:
Para o treinamento do modelo é necessário a criação de um cojunto de dados, para que assim, ele possa receber, extrair e aprender com esses dados. Com isso em mente foram selecionadas imagens de CNHs de diversas fontes da internet, porém, por ser um documento sigiloso que contém dos dados pessoais de uma pessoa, acabou se tornando um desafio encontrar estas imagens para criação deste DataSet, fazendo com que este acabasse sendo um pouco limitado.

### Modelo:
Com o auxílio do site RoboFlow, criar o modelo para reconhecimento do campo para extração dos dados da cnh acabou se provando uma tarefa simples, sendo necessário somente selecionar o local onde os dados seriam retirados em cada imagem do DataSet criado anteriormente, fazendo com que no treinamento, ao passar o mesmo tipo de imagem (CNH) o modelo aprenda a reconhecer um padrão e entender o que ele está vendo, para que quando uma nova imagem seja inserida ele reconheça este mesmo padrão.

## Etapa II - Utils e Script
### Script - Obtenção da imagem:
Após o desenvolvimento do modelo, foi partido para etapa de obtenção da imagem, para isto utitilizou-se o módulo "Yolo" presente na biblioteca "Ultralytics", que é responsável por fazer o controle da WebCam utilizada. O script criado consiste basicamente na abertura da WebCam, onde posteriormente, com o auxílio do modelo desenvolvido é feito o reconhecimento da presença (ou não) de uma CNH na câmera aberta, para que assim seja feito o recorte de toda imagem que é reconhecida por ser uma CNH pelo modelo, sendo enviado posteriormente para a função "Utils", que faz todo o processamento da imagem para que possa retornar os dados para o script.

### Utils - Função de tratamento da imagem:
Com a imagem obtida pela WebCam, viu-se necessário a criação de uma função de tratamento, para que facilitasse o reconhecimento dos dados presentes. Função esta que transforma a imagem para uma escala de tons de cinza, e realiza o recorte dos campos de informações presente em uma CNH, o que é possível devido a padronização da localização dos dados na mesma.
