from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# enable CORS
CORS(app)


@app.route('/')
def hello():
    return 'Hello, Jub!'


if __name__ == '__main__':
    app.run()
