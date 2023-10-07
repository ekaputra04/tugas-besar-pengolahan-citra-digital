# app.py

from flask import Flask, request, render_template, redirect, url_for
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# penambahan dua citra
def add_images(image1, image2):
    # Baca gambar
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # Pastikan kedua gambar memiliki ukuran yang sama
    if img1.shape != img2.shape:
        # Menyesuaikan ukuran gambar agar sama
        width = min(img1.shape[1], img2.shape[1])
        height = min(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))

    result = cv2.add(img1, img2)
    return result

# pengurangan 2 citra
def subtract_images(image1, image2):
    # Baca gambar
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # Pastikan kedua gambar memiliki ukuran yang sama
    if img1.shape != img2.shape:
        # Menyesuaikan ukuran gambar agar sama
        width = min(img1.shape[1], img2.shape[1])
        height = min(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))

    result = cv2.subtract(img1, img2)
    return result
    
# penjumlahan citra dengan konstanta
def add_constant(image_path, constant_value):
    # Baca gambar
    image = cv2.imread(image_path)

    # Tambahkan konstanta ke semua piksel dalam gambar
    result_image = cv2.add(image, (constant_value, constant_value, constant_value, 0))
    return result_image

# pengurangan citra dengan konstanta
def subtract_constant(image_path, constant_value):
    # Baca gambar
    image = cv2.imread(image_path)

    # Tambahkan konstanta ke semua piksel dalam gambar
    result_image = cv2.subtract(image, (constant_value, constant_value, constant_value, 0))
    return result_image

# perkalian 2 citra
def multiplication_images(image1, image2):
    # Baca gambar
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # Pastikan kedua gambar memiliki ukuran yang sama
    if img1.shape != img2.shape:
        # Menyesuaikan ukuran gambar agar sama
        width = min(img1.shape[1], img2.shape[1])
        height = min(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))

    result = cv2.multiply(img1, img2)
    return result
    
# image blanding
def blending_images(image1, image2, alpha, beta):
    # Baca gambar
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # Pastikan kedua gambar memiliki ukuran yang sama
    if img1.shape != img2.shape:
        # Menyesuaikan ukuran gambar agar sama
        width = min(img1.shape[1], img2.shape[1])
        height = min(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (width, height))
        img2 = cv2.resize(img2, (width, height))
    
    result = cv2.addWeighted(img1, alpha, img2, beta, 0)
    return result

# logika operator

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Simpan file di direktori yang telah ditentukan
    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)
    file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
    file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

    img_url1 = f'/static/uploads/{filename1}'
    img_url2 = f'/static/uploads/{filename2}'

    # Ambil jenis operasi yang dipilih
    operation = request.form.get('operation')  
    # Ambil nilai konstanta dari form dengan default 0 jika tidak ada
    constant_value = int(request.form.get('constant-value', '0'))
    # Ambil nilai alpha dari form dengan default 0.5 jika tidak ada
    alpha = float(request.form.get('alpha', '0.5'))
    # Ambil nilai beta dari form dengan default 0.5 jika tidak ada
    beta = float(request.form.get('beta', '0.5'))


    # Operasikan gambar dan simpan hasilnya
    # penjumlahan dua citra
    if operation == 'addition':
        result_img = add_images(os.path.join(app.config['UPLOAD_FOLDER'], filename1), os.path.join(app.config['UPLOAD_FOLDER'], filename2))
        result_filename = f'result_add_{filename1}_{filename2}'
        operation_label = "Penjumlahan Dua Citra"
    # penjumlahan citra dengan konstanta
    elif operation == 'addition-constanta':
        result_img = add_constant(os.path.join(app.config['UPLOAD_FOLDER'], filename1), constant_value)
        result_filename = f'result_add_const_{constant_value}_{filename1}'
        operation_label = "Penjumlahan dengan Konstanta"
    # pengurangan dua citra
    elif operation == 'subtraction':
        result_img = subtract_images(os.path.join(app.config['UPLOAD_FOLDER'], filename1), os.path.join(app.config['UPLOAD_FOLDER'], filename2))
        result_filename = f'result_subtraction_{filename1}_{filename2}'
        operation_label = "Pengurangan Dua Citra"
    # pengurangan citra dengan konstanta
    elif operation == 'subtraction-constanta':
        result_img = subtract_constant(os.path.join(app.config['UPLOAD_FOLDER'], filename1), constant_value)
        result_filename = f'result_substract_const_{constant_value}_{filename1}'
        operation_label = "Pengurangan dengan Konstanta"
    # perkalian dua citra
    elif operation == 'multiplication':
        result_img = multiplication_images(os.path.join(app.config['UPLOAD_FOLDER'], filename1), constant_value)
        result_filename = f'result_multiplication_{filename1}_{filename2}'
        operation_label = "Perkalian Dua Citra"
    # image blanding
    elif operation == 'img-blending':
        result_img = blending_images(os.path.join(app.config['UPLOAD_FOLDER'], filename1), os.path.join(app.config['UPLOAD_FOLDER'], filename2), alpha, beta)
        result_filename = f'result_blending_{filename1}_{filename2}'
        operation_label = "Images Blanding"
    # logika operator

    result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)

    cv2.imwrite(result_path, result_img)

    return render_template('result.html', img_url1=img_url1, img_url2=img_url2, result_img=result_path, operation_label=operation_label)

if __name__ == '__main__':
    app.run(debug=True)
