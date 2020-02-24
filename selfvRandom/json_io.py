import os
import requests
from flask import Flask, render_template, request, Response

app = Flask(__name__)


@app.route("/")
def hello():
    ret = open("index.html").read()
    return ret


if __name__ == "__main__":
    app.run()
