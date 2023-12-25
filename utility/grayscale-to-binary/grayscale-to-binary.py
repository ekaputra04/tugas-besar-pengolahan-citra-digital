import cv2

namaImage = 'gray_1.jpg'

# Baca gambar grayscale
image_grayscale = cv2.imread(namaImage, cv2.IMREAD_GRAYSCALE)

# Ambil threshold menggunakan metode Binary Inverse Thresholding
_, image_binary = cv2.threshold(image_grayscale, 128, 255, cv2.THRESH_BINARY_INV)


# Simpan gambar binary
cv2.imwrite('binary_' + namaImage, image_binary)

# Tampilkan gambar asli dan gambar binary
cv2.imshow('Citra Awal', image_grayscale)
cv2.imshow('Citra Binary', image_binary)

# Tunggu hingga pengguna menekan tombol keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
