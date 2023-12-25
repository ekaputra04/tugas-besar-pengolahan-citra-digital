from PIL import Image

# Isi nama citra yang akan diproses
namaImage = '1.jpg'

# Konstanta untuk pengurangan
constant_value = 200

# Buka gambar
gambar = Image.open(namaImage)
gambar.show()

# Mendapatkan ukuran gambar
lebar, tinggi = gambar.size

# Buat gambar baru dengan ukuran yang sama
hasil_gambar = Image.new("RGB", (lebar, tinggi))

# Lakukan pengurangan piksel per piksel
for x in range(lebar):
    for y in range(tinggi):
        pixel = gambar.getpixel((x, y))

        # pengurangan piksel dengan konstanta
        r = max(pixel[0] - constant_value, 0)
        g = max(pixel[1] - constant_value, 0)
        b = max(pixel[2] - constant_value, 0)

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save('hasil_pengurangan_' + namaImage)

# Tampilkan gambar hasil pengurangan
hasil_gambar.show()