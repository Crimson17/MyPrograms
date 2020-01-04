from flask import Flask
import socket

myIP = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)

@app.route("/")
def main():
    return "Posalji mi Miu postom. heheeehhehehaehaseasehgdasedasd"

if __name__ == "__main__":
    app.run(debug=True, host=myIP, port=80)
