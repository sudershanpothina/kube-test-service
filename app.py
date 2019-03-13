from flask import Flask
import os 

app = Flask(__name__)

@app.route('/hostname')
def hostname():
    return os.uname()[1]

@app.route('/hostname/sub')
def hostname_sub():
    return "sub: " + os.uname()[1]

@app.route('/health')
def health_check():
    return "healthy"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')