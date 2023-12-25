from PIL import Image

# Isi nama citra yang akan diproses
namaImage1 = 'binary_1.jpg'
namaImage2 = 'binary_2.jpg'

# Buka dua citra yang akan diproses
image1 = Image.open(namaImage1).convert("RGB")
image2 = Image.open(namaImage2).convert("RGB")

# Tampilkan gambar awal
image1.show()
image2.show()

# Mendapatkan ukuran gambar
lebar1, tinggi1 = image1.size
lebar2, tinggi2 = image2.size

# Menyesuaikan ukuran gambar agar sama
lebar = min(lebar1, lebar2)
tinggi = min(tinggi1, tinggi2)

image1 = image1.resize((lebar, tinggi))
image2 = image2.resize((lebar, tinggi))

width, height = image1.size
hasil_gambar = Image.new("RGB", (width, height))

for x in range(width):
    for y in range(height):
        pixel1 = image1.getpixel((x, y))
        pixel2 = image2.getpixel((x, y))

        # Operasi logika OR
        r = max(pixel1[0], pixel2[0])
        g = max(pixel1[1], pixel2[1])
        b = max(pixel1[2], pixel2[2])

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save("operator_or_" + namaImage1 + '_' + namaImage2)

# Tampilkan gambar hasil
hasil_gambar.show()
