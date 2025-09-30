from app import app


@app.route("/")
@app.route("/index")
def home() -> str:
    return "Hello, World!"

