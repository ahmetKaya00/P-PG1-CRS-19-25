import cv2

image = cv2.imread("logo.png")

if image is None:
    print("Hata: Görüntü dosyası bulunamadı!")
    exit()

cv2.imshow("Orijinal Goruntu", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

h, w, c = image.shape

print(f"Goruntu Boyutları: {w}x{h} piksel, {c} kanal")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gri_tonlama.png", image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()