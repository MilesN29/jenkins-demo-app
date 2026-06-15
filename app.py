from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Jenkins CI/CD!'

@app.route('/test')
def test():
    return 'Successful test!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
