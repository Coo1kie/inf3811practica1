from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return("HELLO WORLD")
@app.route("/despedida")
def despedida():
    return("bye WORLD XD")
if __name__ == "__main__":
    pass
    app.run(debug=True,port=3811)
