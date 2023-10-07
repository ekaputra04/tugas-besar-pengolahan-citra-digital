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

    # Pastikan ukuran kedua gambar sama
    if img1.shape == img2.shape:
        result = cv2.add(img1, img2)
        return result
    else:
        return None

# pengurangan 2 citra
def subtract_images(image1, image2):
    # Baca gambar
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # Pastikan ukuran kedua gambar sama
    if img1.shape == img2.shape:
        result = cv2.subtract(img1, img2)
        return result
    else:
        return None

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

# perkalian citra
# image blanding

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

    # Operasikan gambar dan simpan hasilnya
    # penjumlahan dua citra
    operation = request.form.get('operation')  # Ambil jenis operasi yang dipilih
    # Ambil nilai konstanta dari form dengan default 0 jika tidak ada
    constant_value = int(request.form.get('constant-value', 0))

    if operation == 'addition':
        result_img = add_images(os.path.join(app.config['UPLOAD_FOLDER'], filename1), os.path.join(app.config['UPLOAD_FOLDER'], filename2))
        result_filename = f'result_add_{filename1}_{filename2}'
        operation_label = "Penjumlahan Dua Citra"
    elif operation == 'addition-constanta':
        # Operasikan gambar dan simpan hasilnya (penjumlahan citra dengan konstanta)
        # gambar 1
        result_img = add_constant(os.path.join(app.config['UPLOAD_FOLDER'], filename1), constant_value)
        result_filename = f'result_add_const_{filename1}_{constant_value}'
        operation_label = "Penjumlahan dengan Konstanta"
    elif operation == 'subtraction':
        result_img = subtract_images(os.path.join(app.config['UPLOAD_FOLDER'], filename1), os.path.join(app.config['UPLOAD_FOLDER'], filename2))
        result_filename = f'result_subtraction_{filename1}_{filename2}'
        operation_label = "Pengurangan Dua Citra"
    elif operation == 'subtraction-constanta':
        # Operasikan gambar dan simpan hasilnya (penjumlahan citra dengan konstanta)
        # gambar 1
        result_img = subtract_constant(os.path.join(app.config['UPLOAD_FOLDER'], filename1), constant_value)
        result_filename = f'result_substract_const_{filename1}_{constant_value}'
        operation_label = "Pengurangan dengan Konstanta"
    
    result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)

    cv2.imwrite(result_path, result_img)

    return render_template('result.html', img_url1=img_url1, img_url2=img_url2, result_img=result_path, operation_label=operation_label)

if __name__ == '__main__':
    app.run(debug=True)
