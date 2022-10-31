import cv2

#Abrindo imagem
img = cv2.imread("car.jpg")

#Deixando a imagem cinza
cinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#transformando a imagem de cinza em uma imagem binária.
_,bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)


#Aplicando o desfoque na imagem para facilitar a detecção do objeto
desfoque = cv2.GaussianBlur(bin,(5,5),0)


#Ira retornar 2 parametros
contorno, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Desenhar apenas os contornos quadrados e grandes
for c in contorno:

    perimetro = cv2.arcLength(c, True)

    if perimetro > 500 and perimetro < 650:
        # Codigo fecha os contornos e aproxima da forma mais provavel dele (quadrado, circulo,...)
        aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)

        if len(aprox) == 4:
            (x, y, alt, lar) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + alt, y + lar), (0, 255, 0), 4)

            roi = img[y:y + lar, x:x + alt]
 		
	    #Salvo a imagem da placa na pasta do projeto
            cv2.imwrite("result.png", roi)
#Exibindo a placa pro usuario
cv2.imshow("Draw Final", img)

#Fecha imagem
cv2.waitKey(0)
cv2.destroyAllWindows()
