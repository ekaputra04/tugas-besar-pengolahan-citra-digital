from PIL import Image

# Buka gambar
gambar = Image.open('1.jpg')
gambar.show()

# Konstanta untuk penjumlahan
constant_value = 100

# Mendapatkan ukuran gambar
lebar, tinggi = gambar.size

# Buat gambar baru dengan ukuran yang sama
hasil_gambar = Image.new("RGB", (lebar, tinggi))

# Lakukan penjumlahan piksel per piksel
for x in range(lebar):
    for y in range(tinggi):
        pixel = gambar.getpixel((x, y))

        # Penjumlahan piksel dengan konstanta
        r = min(pixel[0] + constant_value, 255)
        g = min(pixel[1] + constant_value, 255)
        b = min(pixel[2] + constant_value, 255)

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save("hasil_penjumlahan_konstanta.jpg")
print("Penjumlahan dua gambar selesai.")

# Tampilkan gambar hasil penjumlahan
hasil_gambar.show()