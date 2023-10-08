import cv2
import numpy as np

# Baca dua citra yang akan diurangkan
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

cv2.imshow('Gambar 1', img1)
cv2.imshow('Gambar 2', img2)

if img1.shape != img2.shape:
        # Menyesuaikan ukuran gambar agar sama
        width = min(img1.shape[1], img2.shape[1])
        height = min(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))

# Lakukan perkalian citra
result = cv2.multiply(img1, img2)

# Simpan hasil operasi perkalian ke dalam sebuah file
cv2.imwrite('hasil_perkalian.jpg', result)

# Tampilkan citra hasil perkalian
cv2.imshow('Perkalian 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()