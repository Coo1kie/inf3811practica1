from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return("HELLO WORLD)
if __name__ == "__main__":
    pass
    app.run(debug=True,port=5001)
