import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


#links ending in ("/") will redirect to the file within the ()
#The same style applies to the following methods
#This allows multiple pages to interact through links.
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/health', methods=['GET'])
def health():
    return "200"

@app.route("/mamnuya")
def Rinki():
        return render_template('Rinki.html')

@app.route("/nandhini")
def Nandhini():
        return render_template('Webp.html')

@app.route("/ixchel")
def Marcela():
        return render_template('ixchel.html')

if __name__ == '__main__':
    app.run(debug=True)
