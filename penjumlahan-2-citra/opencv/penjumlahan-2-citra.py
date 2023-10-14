import cv2

# Baca kedua citra 
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

# menampilkan kedua gambar awal
cv2.imshow('Gambar 1', img1)
cv2.imshow('Gambar 2', img2)

# Menyesuaikan ukuran gambar agar sama
if img1.shape != img2.shape:
        width = min(img1.shape[1], img2.shape[1])
        height = min(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))

# Lakukan penjumlahan dua citra
result = cv2.add(img1, img2)

# Simpan hasil operasi penjumlahan ke dalam sebuah file
cv2.imwrite('hasil_penjumlahan.jpg', result)

# Tampilkan citra hasil pengurangan
cv2.imshow('Penjumlahan 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()