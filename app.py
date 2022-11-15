import certifi
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

ca = certifi.where()
client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.suyddmw.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.fourGlasses


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/team0')
# def home():
#     return render_template('team0.html')

# @app.route('/team1')
# def home():
#     return render_template('team1.html')

# @app.route('/team2')
# def home():
#     return render_template('team2.html')

# @app.route('/team3')
# def home():
#     return render_template('team3.html')


@app.route("/review", methods=["POST"])
def insertReviewPost():
    review_receive = request.form['review_give']

    doc = {
        'review': review_receive,
    }
    db.song.insert_one(doc)
    return jsonify({'msg': '저장완료'})


@app.route("/review", methods=["GET"])
def homework_get():
    reviews = list(db.song.find({}, {'_id': False}).sort('_id',-1).limit(5))
    print()
    return jsonify({'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
