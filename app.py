from flask import Flask, redirect, request
import secrets

app = Flask(__name__)

links = {}

@app.route("/")
def home():
    return "Uzzal Link Shortener is running!"

@app.route("/create", methods=["GET"])
def create():
    url = request.args.get("url")

    if not url:
        return "URL missing", 400

    if not url.startswith(("http://", "https://")):
        return "Invalid URL", 400

    code = secrets.token_urlsafe(5)
    links[code] = url

    return {
        "short_code": code,
        "short_url": f"/s/{code}"
    }

@app.route("/s/<code>")
def short_link(code):
    url = links.get(code)

    if not url:
        return "Short link not found", 404

    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
