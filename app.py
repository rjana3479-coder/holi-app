from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <body style='text-align:center; background-color:#ffe6f0;'>
        <h1 style='color:purple;'>🌸 Happy Holi Buddy! 🌸</h1>
        <h2>Play Safe & Enjoy Colors 🎨</h2>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
