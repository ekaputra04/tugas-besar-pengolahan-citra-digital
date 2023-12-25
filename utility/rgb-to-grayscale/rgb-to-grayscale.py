import cv2

namaImage = '1.jpg'

# Baca gambar
image_rgb = cv2.imread(namaImage)


# Ubah gambar menjadi grayscale
image_grayscale = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

# Simpan hasil konversi ke dalam sebuah file
cv2.imwrite('gray_' + namaImage, image_grayscale)

# Tampilkan citra
cv2.imshow('Citra Awal', image_rgb)
cv2.imshow('Citra Grayscale', image_grayscale)

# Tunggu hingga pengguna menekan tombol keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
