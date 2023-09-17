import cv2

# Yüz tanıma için önceden eğitilmiş bir XML dosyasını yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera erişimi veya bir video dosyası aç
cap = cv2.VideoCapture(0)  # 0, sistemdeki ilk kameralı cihazı kullanır

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Kareyi gri tonlamaya çevir (Yüz tanıma için daha hızlıdır)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Algılanan yüzlerin etrafına bir dikdörtgen çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Kareyi göster
    cv2.imshow('Face Detection', frame)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve açık pencereleri kapat
cap.release()
cv2.destroyAllWindows()