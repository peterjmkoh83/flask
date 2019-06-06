from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
     print("*"*100)
     print("running in hello function")
     return "Hello World!"

@app.route("/dojo")
def hello_dojo():
     print("*"*100)
     print("running in dojo function")
     return "Dojo!"

@app.route("/say/<name>")
def hello_say(name):
     print("*"*100)
     return f"hi {name}!".title()

@app.route("/repeat/<num>/<greeting>")
def hello_repeat(num, greeting):
     return f"{greeting}"*int(num)


if __name__ == "__main__":
     app.run(debug=True)