from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/output')
def output():
    return "hi"
if __name__== "__main__":
    app.run()

    