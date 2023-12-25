import cv2

# Isi nama citra yang akan diproses
namaImage = '1.jpg'

constant_value = 200

image = cv2.imread(namaImage)

cv2.imshow('Gambar 1', image)

# Lakukan pengurangan citra
result = cv2.subtract(image, (constant_value, constant_value, constant_value, 0))

# Simpan hasil operasi pengurangan ke dalam sebuah file
cv2.imwrite('hasil_pengurangan_' + namaImage, result)

# Tampilkan citra hasil pengurangan
cv2.imshow('Pengurangan 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()