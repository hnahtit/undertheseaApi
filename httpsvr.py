from underthesea import classify
from underthesea import sentiment
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin\


# Khai bao cong cua server
my_port = '8000'

# Doan ma khoi tao server
app = Flask(__name__)
CORS(app)

# Khai bao ham xu ly request index


@app.route('/')
@cross_origin()
def index():
    return "Welcome to flask API!"

# Khai bao ham xu ly request hello_word


@app.route('/hello_world', methods=['GET'])
@cross_origin()
def hello_world():
    # Lay staff id cua client gui len
    staff_id = request.args.get('staff_id')
    # Tra ve cau chao Hello
    return "Hello " + str(staff_id)

# call underthesea

@app.route('/classify', methods=['GET'])
@cross_origin()
def classification():
    # Lay staff id cua client gui len
    source_string = request.args.get('text')
    # Tra ve cau chao Hello
    return ''.join(classify(str(source_string)))

@app.route('/sentiment', methods=['GET'])
@cross_origin()
def sentimentAnalysis():
    # Lay staff id cua client gui len
    source_string = request.args.get('text')
    # Tra ve cau chao Hello
    return sentiment(str(source_string))

# Thuc thi server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=my_port)
