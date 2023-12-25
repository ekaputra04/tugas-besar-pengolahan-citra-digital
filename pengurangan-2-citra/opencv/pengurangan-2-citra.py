import cv2

img1 = cv2.imread('gray_2.jpg')
img2 = cv2.imread('gray_1.jpg')

cv2.imshow('Gambar 1', img1)
cv2.imshow('Gambar 2', img2)

# Menyesuaikan ukuran gambar agar sama
if img1.shape != img2.shape:
        width = min(img1.shape[1], img2.shape[1])
        height = min(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))

# Lakukan pengurangan citra
result = cv2.subtract(img1, img2)

# Simpan hasil operasi pengurangan ke dalam sebuah file
cv2.imwrite('hasil_pengurangan.jpg', result)

# Tampilkan citra hasil pengurangan
cv2.imshow('Pengurangan 2 Citra', result)
cv2.waitKey(0)
cv2.destroyAllWindows()