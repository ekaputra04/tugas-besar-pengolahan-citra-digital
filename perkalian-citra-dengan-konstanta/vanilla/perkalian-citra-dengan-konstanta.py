from PIL import Image

# Isi nama citra yang akan diproses
namaImage = '1.jpg'

# Konstanta untuk perkalian
constant_value = 1.8

# Buka gambar
gambar = Image.open(namaImage)
gambar.show()

# Mendapatkan ukuran gambar
lebar, tinggi = gambar.size

# Buat gambar baru dengan ukuran yang sama
hasil_gambar = Image.new("RGB", (lebar, tinggi))

# Lakukan perkalian piksel per piksel
for x in range(lebar):
    for y in range(tinggi):
        pixel = gambar.getpixel((x, y))

        # perkalian piksel dengan konstanta
        r = int(min(max(pixel[0] * constant_value, 0), 255))
        g = int(min(max(pixel[1] * constant_value, 0), 255))
        b = int(min(max(pixel[2] * constant_value, 0), 255))

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save('hasil_perkalian_' + namaImage)

# Tampilkan gambar hasil perkalian
hasil_gambar.show()