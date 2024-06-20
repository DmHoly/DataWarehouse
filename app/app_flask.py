from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/page2")
def page2():
    return "<p>This is page 2</p>"

if __name__ == '__main__':
    app.run()