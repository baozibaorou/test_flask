from flask import Flask

app = Flask(__name__)
a = 1
b = 2
@app.route("/")
def index():
    return 'hello'



if __name__ == '__main__':
    app.run()
