from ultralytics import YOLO
import cv2
import utils

# Abre a camera 0
cap = cv2.VideoCapture(0)
# Carrega o modelo
my_model = YOLO("./best.pt")

seguir =  False
frozen_frame = None

while cap.isOpened():
    # Capturar frame da webcam
    success, frame = cap.read()
    if success == False:
        break
     
    # Segue pro if se a captura for bem sucedida
    results = my_model(frame, conf = 0.75)

        # para cada result ele faz 1 plot
    for result in results:
        frame = result.plot()
        for box in result.boxes:
                # Obtém as coordenadas da caixa
                x1, y1, x2, y2 = map(int, box.xyxy[0])

    # Mostra a imagem plotada
    cv2.imshow("Tela", frame)

        
    # Delay de 1 ms
    delay = cv2.waitKey(1)

    if delay == ord('q'):
        break

    if delay == ord('w'):
        frozen_frame = frame[y1:y2, x1:x2]
        cv2.imshow("tela", frozen_frame)
    
    #if delay == ord('s'):
         #cv2.imwrite('img_teste.png', frozen_frame)


utils.processar_img(frozen_frame)

cap.release()
cv2.destroyAllWindows()
print("Encerrando")