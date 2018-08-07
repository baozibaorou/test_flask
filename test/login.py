from flask import Flask

app = Flask(__name__)
a = 1
@app.route("/")
def index():
    return 'hello'



if __name__ == '__main__':
    app.run()
