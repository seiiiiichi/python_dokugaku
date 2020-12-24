# coding; UTF-8

# Flaskパッケージを用いて、ウェブブラウザに文字を表示
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
	return "Hello, w"
	
	getgit gitgit

app.run(port=800ori