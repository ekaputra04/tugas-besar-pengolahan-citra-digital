import cv2
import numpy as np

# Isi nama citra yang akan diproses
namaImage = 'binary_2.jpg'

# Baca citra yang akan diproses
image = cv2.imread(namaImage)

cv2.imshow('Citra Awal', image)

# Lakukan operasi not
result = cv2.bitwise_not(image)

# Simpan hasil operasi not ke dalam sebuah file
cv2.imwrite('operator_not_' + namaImage, result)

# Tampilkan citra hasil not
cv2.imshow('Hasil Logika Not', result)
cv2.waitKey(0)
cv2.destroyAllWindows()