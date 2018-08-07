from flask import Flask

app = Flask(__name__)
a = 1
c = 3
@app.route("/")
def index():
    return 'hello'



if __name__ == '__main__':
    app.run()
