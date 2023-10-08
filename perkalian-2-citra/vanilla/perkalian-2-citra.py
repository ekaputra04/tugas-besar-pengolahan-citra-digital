from PIL import Image

# Buka dua citra yang akan diurangkan
img1 = Image.open('1.jpg')
img2 = Image.open('2.jpg')

# Tampilkan gambar awal
img1.show()
img2.show()

# Mendapatkan ukuran gambar
lebar1, tinggi1 = img1.size
lebar2, tinggi2 = img2.size

# Menyesuaikan ukuran gambar agar sama
lebar = min(lebar1, lebar2)
tinggi = min(tinggi1, tinggi2)

img1 = img1.resize((lebar, tinggi))
img2 = img2.resize((lebar, tinggi))

width, height = img1.size
hasil_gambar = Image.new("RGB", (width, height))

# Lakukan perkalian piksel per piksel
for x in range(width):
    for y in range(height):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))

        # perkalian piksel
        r = min(pixel1[0] + pixel2[0], 255)
        g = min(pixel1[1] + pixel2[1], 255)
        b = min(pixel1[2] + pixel2[2], 255)

        hasil_gambar.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
hasil_gambar.save("hasil_perkalian.jpg")
print("Perkalian dua gambar selesai.")

# Tampilkan gambar hasil perkalian
hasil_gambar.show()