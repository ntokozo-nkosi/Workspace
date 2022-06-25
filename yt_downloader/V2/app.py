from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

Link ="empty"

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    if request.method == "POST":
        return request.form.get("url")
    return redirect(url_for("test"))

@app.route("/test")
def test():
    return Link


if __name__ == "__main__":
    app.run(debug=True)
