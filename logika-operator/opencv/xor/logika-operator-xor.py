import cv2
import numpy as np

# Isi nama citra yang akan diproses
namaImage1 = 'binary_1.jpg'
namaImage2 = 'binary_2.jpg'

# Baca dua citra yang akan diproses
image1 = cv2.imread(namaImage1)
image2 = cv2.imread(namaImage2)

cv2.imshow('Gambar 1', image1)
cv2.imshow('Gambar 2', image2)

# Menyesuaikan ukuran gambar agar sama
if image1.shape != image2.shape:
        width = min(image1.shape[1], image2.shape[1])
        height = min(image1.shape[0], image2.shape[0])
        image1 = cv2.resize(image1, (width, height))
        image2 = cv2.resize(image2, (width, height))

# Lakukan operasi xor
result = cv2.bitwise_xor(image1, image2)

# Simpan hasil operasi xor ke dalam sebuah file
cv2.imwrite('operator_xor_' + namaImage1 + '_' + namaImage2, result)

# Tampilkan citra hasil xor
cv2.imshow('Hasil Logika Xor', result)
cv2.waitKey(0)
cv2.destroyAllWindows()