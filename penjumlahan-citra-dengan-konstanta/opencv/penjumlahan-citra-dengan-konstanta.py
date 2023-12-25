import cv2

# Baca gambar
image = cv2.imread('gray_1.jpg')

# Tampilkan gambar asli
cv2.imshow('Gambar Asli', image)

# Konstanta untuk penjumlahan
constant_value = 200

# Tambahkan konstanta ke semua piksel dalam gambar
result = cv2.add(image, (constant_value, constant_value, constant_value, 0))

cv2.imwrite('hasil_penjumlahan_konstanta.jpg', result)

# Tampilkan gambar hasil penjumlahan dengan konstanta
cv2.imshow('Hasil Penjumlahan dengan Konstanta', result)

# Tunggu sampai pengguna menekan tombol apapun
cv2.waitKey(0)

# Tutup semua jendela gambar
cv2.destroyAllWindows()
