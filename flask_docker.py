from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    intro = "<h3 style='color:#fd79a8;'>Welcome CI/CD using Jenkins</h1>"
    return intro

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
