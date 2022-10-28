from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def get_results():
    response = jsonify({
        "slackUsername":"Brownie",
        "backend":True,
        "age":29,
        "bio":"Full stack developer and JavaScript evangelist"
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response,200

if __name__ == "__main__":
    app.run(debug=True)