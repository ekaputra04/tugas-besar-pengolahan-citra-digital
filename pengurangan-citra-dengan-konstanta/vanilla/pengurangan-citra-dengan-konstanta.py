from PIL import Image

# Buka gambar
gambar = Image.open('1.jpg')
gambar.show()

# Konstanta untuk pengurangan
constant_value = 50

# Mendapatkan ukuran gambar
lebar, tinggi = gambar.size

# Buat gambar baru dengan ukuran yang sama
hasil_gambar = Image.new("RGB", (lebar, tinggi))

# Lakukan pengurangan piksel per piksel
for x in range(lebar):
    for y in range(tinggi):
        pixel = gambar.getpixel((x, y))

        # pengurangan piksel dengan konstanta
        r = min(pixel[0] - constant_value, 255)
        g = min(pixel[1] - constant_value, 255)
        b = min(pixel[2] - constant_value, 255)

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save("hasil_pengurangan_konstanta.jpg")
print("Pengurangan gambar dengan konstanta selesai.")

# Tampilkan gambar hasil pengurangan
hasil_gambar.show()