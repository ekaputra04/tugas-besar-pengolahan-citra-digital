import cv2

# Isi nama citra yang akan diproses
namaImage = '1.jpg'

constant_value = 1.8

image = cv2.imread(namaImage)

cv2.imshow('Gambar 1', image)

# Lakukan perkalian citra
result = cv2.multiply(image, (constant_value, constant_value, constant_value, 0))

# Simpan hasil operasi perkalian ke dalam sebuah file
cv2.imwrite('hasil_perkalian_' + namaImage, result)

# Tampilkan citra hasil perkalian
cv2.imshow('Perkalian 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()