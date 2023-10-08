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

# Tentukan bobot (alpha) untuk citra pertama dan citra kedua
alpha = 0.7  # Bobot untuk citra pertama (0-1)
beta = 0.3   # Bobot untuk citra kedua (0-1)

# Lakukan blending piksel per piksel
blended_image = Image.new("RGB", img1.size)
    
for x in range(img1.width):
    for y in range(img1.height):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))

        # Perhitungan blending
        r = int(alpha * pixel1[0] + beta * pixel2[0])
        g = int(alpha * pixel1[1] + beta * pixel2[1])
        b = int(alpha * pixel1[2] + beta * pixel2[2])

        blended_image.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
blended_image.save("hasil_blending.jpg")
print("Image blending selesai.")

# Tampilkan gambar hasil blending
blended_image.show()