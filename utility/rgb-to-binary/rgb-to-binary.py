import cv2

namaImage = '1.jpg'

# Baca gambar
image_rgb = cv2.imread(namaImage)


# Ubah gambar menjadi grayscale
image_grayscale = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

# Lakukan thresholding untuk mengubah citra menjadi binary
_, image_binary = cv2.threshold(image_grayscale, 128, 255, cv2.THRESH_BINARY)

# Simpan hasil operasi thresholding ke dalam sebuah file
cv2.imwrite('binary_' + namaImage, image_binary)

# Tampilkan citra 
cv2.imshow('Citra Awal', image_rgb)
cv2.imshow('Citra Binary', image_binary)

# Tunggu hingga pengguna menekan tombol keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
