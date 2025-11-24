from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home route: renders a simple HTML page.
    """
    return render_template("index.html")

@app.route("/health")
def health():
    """
    Health check endpoint for CI/CD to verify the app is running.
    """
    return {"status": "ok"}, 200


if __name__ == "__main__":
    # Run in debug for local development
    app.run(host="0.0.0.0", port=5000, debug=True)
