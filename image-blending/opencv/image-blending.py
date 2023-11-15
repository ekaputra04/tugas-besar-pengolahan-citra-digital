import cv2

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

# Berikan bobot (weight) untuk kedua citra
alpha = 0.3  # Bobot untuk citra pertama (0-1)
beta = 0.7   # Bobot untuk citra kedua (0-1)

# Gabungkan kedua citra menggunakan formula blending
result = cv2.addWeighted(img1, alpha, img2, beta, 0)

# Simpan hasil operasi perkalian ke dalam sebuah file
cv2.imwrite('hasil_blending.jpg', result)

# Tampilkan citra hasil perkalian
cv2.imshow('Image Blending', result)
cv2.waitKey(0)
cv2.destroyAllWindows()