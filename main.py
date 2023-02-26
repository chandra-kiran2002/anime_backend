from flask import Flask, request, send_file, jsonify
from PIL import Image
from flask_cors import CORS, cross_origin
from image_change import fun
from sklearn_kmean import change_image
import numpy
import base64
import io
from io import BytesIO
import matplotlib.image as im
app=Flask(__name__)
CORS(app, support_credentials=True)




# @app.route('/',methods = ['POST'])
# def home():
#       return "hello"

@app.route('/',methods = ['POST'])
@cross_origin()
def modify_image():
    image = request.files['image']
    print(image)
    print(request.values)
    k_value = int(request.values['k'])
    image = Image.open(image)
    image = image.convert('RGB')
    image.thumbnail((300,300))
    image = numpy.asarray(image)
    ans = change_image(k_value,image)
    data = Image.fromarray(ans.astype('uint8'), 'RGB')
    buffer = io.BytesIO()
    data.save(buffer, 'png')
    buffer.seek(0)
    data = buffer.read()
    data = base64.b64encode(data).decode()
    # return  jsonify({'msg': 'success', 'size': [data.width, data.height],'format': data.format, 'img': im_b64})
    return f'<img src="data:image/png;base64,{data}">'

if __name__ == '__main__':
   app.run(debug = True)