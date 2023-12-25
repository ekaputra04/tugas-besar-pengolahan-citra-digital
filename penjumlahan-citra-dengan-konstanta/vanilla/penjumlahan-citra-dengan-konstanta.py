from PIL import Image

# Isi nama citra yang akan diproses
namaImage = '1.jpg'

# Konstanta untuk penjumlahan
constant_value = 100

# Buka gambar
gambar = Image.open(namaImage)
gambar.show()

# Mendapatkan ukuran gambar
lebar, tinggi = gambar.size

# Buat gambar baru dengan ukuran yang sama
hasil_gambar = Image.new("RGB", (lebar, tinggi))

# Lakukan penjumlahan piksel per piksel
for x in range(lebar):
    for y in range(tinggi):
        pixel = gambar.getpixel((x, y))

        # penjumlahan piksel dengan konstanta
        r = max(pixel[0] + constant_value, 0)
        g = max(pixel[1] + constant_value, 0)
        b = max(pixel[2] + constant_value, 0)

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save('hasil_penjumlahan_' + namaImage)

# Tampilkan gambar hasil penjumlahan
hasil_gambar.show()