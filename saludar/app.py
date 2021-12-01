from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return("HOLA MUNDO XD")
if __name__ == "__main__":
    pass
    app.run()
