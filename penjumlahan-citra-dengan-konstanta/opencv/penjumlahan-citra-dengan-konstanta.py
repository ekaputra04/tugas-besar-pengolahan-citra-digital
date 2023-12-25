import cv2

# Isi nama citra yang akan diproses
namaImage = '1.jpg'

constant_value = 100

image = cv2.imread(namaImage)

cv2.imshow('Gambar 1', image)

# Lakukan penjumlahan citra
result = cv2.add(image, (constant_value, constant_value, constant_value, 0))

# Simpan hasil operasi penjumlahan ke dalam sebuah file
cv2.imwrite('hasil_penjumlahan_' + namaImage, result)

# Tampilkan citra hasil penjumlahan
cv2.imshow('Penjumlahan 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()