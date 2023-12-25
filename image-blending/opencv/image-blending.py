import cv2

# Isi nama citra yang akan diproses
namaImage1 = '1.jpg'
namaImage2 = '2.jpg'

# Berikan bobot (weight) untuk kedua citra
alpha = 0.5  # Bobot untuk citra pertama (0-1)
beta = 0.5   # Bobot untuk citra kedua (0-1)

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

# Gabungkan kedua citra menggunakan formula blending
result = cv2.addWeighted(image1, alpha, image2, beta, 0)

# Simpan hasil operasi perkalian ke dalam sebuah file
cv2.imwrite('blending_' + namaImage1 + '_' + namaImage2, result)

# Tampilkan citra hasil perkalian
cv2.imshow('Images Blending', result)
cv2.waitKey(0)
cv2.destroyAllWindows()