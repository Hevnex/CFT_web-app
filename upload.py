from PIL import Image
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        img = Image.open(f)
        width = img.size[0]
        height = img.size[1]
        black_pix = 0
        white_pix = 0
        for i in range(width):
            for j in range(height):
                if img.getpixel((i, j)) == (0, 0, 0):
                    black_pix += 1
                elif img.getpixel((i, j)) == (255, 255, 255):
                    white_pix += 1
                else:
                    continue
        if black_pix > white_pix:
            return "Black pixels (" + str(black_pix) + ") more than White pixels (" + str(white_pix) + ")"
        elif black_pix < white_pix:
            return "White pixels (" + str(white_pix) + ") more than Black pixels (" + str(black_pix) + ")"
        else:
            return "Black pixels (" + str(black_pix) + ") as many as White pixels (" + str(white_pix) + ")"



