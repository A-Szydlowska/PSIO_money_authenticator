import cv2

image = cv2.imread("image.jpg")

# Dostosuj jasność (alpha to współczynnik jasności, beta to offset)
image = cv2.addWeighted(image, 1.5, np.zeros(image.shape, image.dtype), 0, 10)

# Wykonaj rozmycie Gaussa
gaussian = cv2.GaussianBlur(image, (0, 0), 3)

# Wzmocnij ostrość (alpha to współczynnik wzmocnienia ostrości, beta to offset)
image = cv2.addWeighted(image, 2.0, gaussian, -1, 0)

# Konwertuj obraz do skali szarości
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Dostosuj kontrast
enhanced_gray = cv2.equalizeHist(gray)

# Przywróć kolor obrazowi po dostosowaniu kontrastu
enhanced_image = cv2.cvtColor(enhanced_gray, cv2.COLOR_GRAY2BGR)

# Zapisz obraz z dostosowanym kontrastem
cv2.imwrite("enhanced_image.jpg", enhanced_image)