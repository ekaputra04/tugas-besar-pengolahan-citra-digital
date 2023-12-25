import cv2

# Isi nama citra yang akan diproses
namaImage1 = '1.jpg'
namaImage2 = '2.jpg'

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

# Lakukan perkalian citra
result = cv2.multiply(image1, image2)

# Simpan hasil operasi perkalian ke dalam sebuah file
cv2.imwrite('hasil_perkalian_' + namaImage1 + '_' + namaImage2, result)

# Tampilkan citra hasil perkalian
cv2.imshow('perkalian 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()