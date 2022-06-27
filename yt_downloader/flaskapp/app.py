"""
YT Downloader
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>YouTube Video Downloader</h1>"

if __name__ == "__main__":
    app.run(debug=True)
