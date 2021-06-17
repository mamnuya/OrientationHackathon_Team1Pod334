import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


#@app.route('/')
#def index():
#    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/ixchel')
def ixchel():
    return render_template('ixchel.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
