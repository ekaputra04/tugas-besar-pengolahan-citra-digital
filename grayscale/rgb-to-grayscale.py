import cv2

# Baca gambar
img = cv2.imread('gambar.jpg')

cv2.imshow('Citra Awal', img)

# Ubah gambar menjadi grayscale
result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simpan hasil operasi perkalian ke dalam sebuah file
cv2.imwrite('hasil_grayscale.jpg', result)

# Tampilkan citra grayscale
cv2.imshow('Citra Grayscale', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
