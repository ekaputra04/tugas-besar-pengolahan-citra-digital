from flask import Flask, request, render_template
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# resize images
def resize_images(image1, image2):
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

    return img1, img2

# penjumlahan dua citra
def add_images(image1, image2):
    img1, img2 = resize_images(image1, image2)
    result = cv2.add(img1, img2)
    return result

# pengurangan dua citra
def subtract_images(image1, image2):
    img1, img2 = resize_images(image1, image2)
    result = cv2.subtract(img1, img2)
    return result

# penjumlahan citra dengan konstanta
def add_constant(image_path, constant_value):
    # Baca gambar
    image = cv2.imread(image_path)

    # Tambahkan konstanta ke semua piksel dalam gambar
    result = cv2.add(image, (constant_value, constant_value, constant_value, 0))
    return result

# pengurangan citra dengan konstanta
def subtract_constant(image_path, constant_value):
    # Baca gambar
    image = cv2.imread(image_path)

    # Tambahkan konstanta ke semua piksel dalam gambar
    result = cv2.subtract(image, (constant_value, constant_value, constant_value, 0))
    return result

# perkalian 2 citra
def multiplication_images(image1, image2):
    img1, img2 = resize_images(image1, image2)
    result = cv2.multiply(img1, img2)
    return result

# image blending
def blending_images(image1, image2, alpha, beta):
    img1, img2 = resize_images(image1, image2)
    result = cv2.addWeighted(img1, alpha, img2, beta, 0)
    return result

# logika operator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    operation = request.form.get('operation')
    file1 = request.files['file1']
    file1_filename = secure_filename(file1.filename)
    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1_filename)
    file1.save(file1_path)

    print(operation)
    print(file1_filename)
    print(file1_path)

    img_url1 = f'/static/uploads/{file1_filename}'
    img_url2 = None

    if operation in ['addition', 'subtraction', 'multiplication']:
        file2 = request.files['file2']
        file2_filename = secure_filename(file2.filename)
        file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2_filename)
        file2.save(file2_path)
        img_url2 = f'/static/uploads/{file2_filename}'

    if operation == 'addition':
        result_img = add_images(file1_path, file2_path)
        result_filename = f'result_add_{file1_filename}_{file2_filename}'
        operation_label = "Penjumlahan Dua Citra"
    elif operation == 'addition-constant':
        constant_value = float(request.form.get('constant-value', "0"))
        result_img = add_constant(file1_path, constant_value)
        result_filename = f'result_add_const_{constant_value}_{file1_filename}'
        operation_label = "Penjumlahan dengan Konstanta"
    elif operation == 'subtraction':
        result_img = subtract_images(file1_path, file2_path)
        result_filename = f'result_subtraction_{file1_filename}_{file2_filename}'
        operation_label = "Pengurangan Dua Citra"
    elif operation == 'subtraction-constant':
        constant_value = float(request.form.get('constant-value', "0"))
        result_img = subtract_constant(file1_path, constant_value)
        result_filename = f'result_subtract_const_{constant_value}_{file1_filename}'
        operation_label = "Pengurangan dengan Konstanta"
    elif operation == 'multiplication':
        result_img = multiplication_images(file1_path, file2_path)
        result_filename = f'result_multiplication_{file1_filename}_{file2_filename}'
        operation_label = "Perkalian Dua Citra"
    elif operation == 'image-blending':
        file2 = request.files['file2']
        file2_filename = secure_filename(file2.filename)
        file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2_filename)
        file2.save(file2_path)
        img_url2 = f'/static/uploads/{file2_filename}'

        alpha = float(request.form.get('alpha', "0.5"))
        beta = float(request.form.get('beta', "0.5"))
        result_img = blending_images(file1_path, file2_path, alpha, beta)
        result_filename = f'result_blending_{file1_filename}_{file2_filename}'
        operation_label = "Images Blending"

    result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)

    cv2.imwrite(result_path, result_img)

    return render_template('result.html', img_url1=img_url1, img_url2=img_url2, result_img=result_path, operation_label=operation_label)

if __name__ == '__main__':
    app.run(debug=True)
