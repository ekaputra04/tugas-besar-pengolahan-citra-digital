from PIL import Image

# Isi nama citra yang akan diproses
namaImage1 = '1.jpg'
namaImage2 = '2.jpg'

# Berikan bobot (weight) untuk kedua citra
alpha = 0.5  # Bobot untuk citra pertama (0-1)
beta = 0.5   # Bobot untuk citra kedua (0-1)

# Buka dua citra yang akan diproses
image1 = Image.open(namaImage1)
image2 = Image.open(namaImage2)

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

# Lakukan blending piksel per piksel
blended_image = Image.new("RGB", image1.size)
    
for x in range(image1.width):
    for y in range(image1.height):
        pixel1 = image1.getpixel((x, y))
        pixel2 = image2.getpixel((x, y))

        # Perhitungan blending
        r = int(alpha * pixel1[0] + beta * pixel2[0])
        g = int(alpha * pixel1[1] + beta * pixel2[1])
        b = int(alpha * pixel1[2] + beta * pixel2[2])

        blended_image.putpixel((x, y), (r, g, b))

# Simpan hasil gambar
blended_image.save('blending_' + namaImage1 + '_' + namaImage2)

# Tampilkan gambar hasil blending
blended_image.show()