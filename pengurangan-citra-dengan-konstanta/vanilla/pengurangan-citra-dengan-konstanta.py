from PIL import Image

# Buka gambar
gambar = Image.open('1.jpg')
gambar.show()

# Konstanta untuk pengurangan
constant_value = 100

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
hasil_gambar.save("hasil_pengurangan_konstanta.jpg")
print("Pengurangan gambar dengan konstanta selesai.")

# Tampilkan gambar hasil pengurangan
hasil_gambar.show()