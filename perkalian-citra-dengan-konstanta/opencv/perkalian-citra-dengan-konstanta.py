import cv2
import numpy as np

# Baca citra awal
img1 = cv2.imread('1.jpg')

cv2.imshow('Gambar 1', img1)

# Konstanta untuk perkalian
constant_value = 1.8

# Tambahkan konstanta ke semua piksel dalam gambar
result = cv2.multiply(img1, (constant_value, constant_value, constant_value, 0))

# Simpan hasil operasi perkalian ke dalam sebuah file
cv2.imwrite('hasil_perkalian.jpg', result)

# Tampilkan citra hasil perkalian
cv2.imshow('Perkalian 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()