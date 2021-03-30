from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html')

@app.route('/price', methods=['POST'])
def add():
    if request.method =='POST':
        radius = int(request.form['radius'])
        height = int(request.form['height'])


    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)