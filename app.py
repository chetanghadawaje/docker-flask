from flask import Flask
app = Flask(__name__)
@app.route('/test')
def hello_whale():
    return "Hello Welcome to DOCKER.."
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
