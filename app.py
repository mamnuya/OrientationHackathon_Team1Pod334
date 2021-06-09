from flask import Flask, render_template
app = Flask(__name__)


#links ending in ("/") will redirect to the file within the ()
#The same style applies to the following methods
#This allows multiple pages to interact through links.
@app.route("/")
def home():
    return render_template('home.html')

#links ending in /mamnuya will redirect to the file within the ()
@app.route("/mamnuya")
def Rinki():
        return render_template('Rinki.html')

@app.route("/EXAMPLE")
def Nandhini():
        return render_template('EXAMPLE.html')

@app.route("/EXAMPLE")
def Marcela():
        return render_template('EXAMPLE.html')


if __name__ == '__main__':
    app.run(debug=True)
