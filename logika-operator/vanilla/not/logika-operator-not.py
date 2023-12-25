from PIL import Image

# Isi nama citra yang akan diproses
namaImage1 = 'binary_1.jpg'

# Buka citra yang akan diproses
image1 = Image.open(namaImage1).convert("RGB")

# Tampilkan gambar awal
image1.show()

# Mendapatkan ukuran gambar
lebar, tinggi = image1.size

hasil_gambar = Image.new("RGB", (lebar, tinggi))

for x in range(lebar):
    for y in range(tinggi):
        pixel1 = image1.getpixel((x, y))

        # Operasi logika NOT (Inversi nilai piksel)
        r = 255 - pixel1[0]
        g = 255 - pixel1[1]
        b = 255 - pixel1[2]

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save("operator_not_" + namaImage1)

# Tampilkan gambar hasil
hasil_gambar.show()
