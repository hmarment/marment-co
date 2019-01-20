from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__,
            static_folder="../client/dist/static",
            template_folder="../client/dist")

# enable CORS
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello, Jub!'


if __name__ == '__main__':
    app.run()
