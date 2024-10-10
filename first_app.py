from flask import Flask

app = Flask(__name__)

# set FLASK_APP=first_app.py  ---sets env variable
# flask run -- runs project

@app.route('/')
def hello_world():
    return '<h4> Hello World</h4>'


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port='5000',debug=True)
