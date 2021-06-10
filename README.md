# Flask-Blog

Site using Flask, Python, CSS, and HTML to display 3 portfolio template options. The home site holds varying customizable portfolio templates for user's to implement, choose, and edit based on preference.
 
## Running and Creating Portfolio Pages


Create a folder titled "templates" in your directory. Place html files in this folder.
Create a fold titled "static" in your directory. Place the "img" and "styles" folders in this folder.
Create a folder titled "img" in your directory. Place .png and .jpeg/.jpg files in this folder.
Create a folder titled "styles" in your directory. Place .css files in this folder.

## Installation

Make sure you have python3 and pip installed


Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage


Create a .env file using the example.env template


Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

## Implementation Troubleshooting for Macs in Terminal:
ENTER the following into the terminal, line by line, after downloading python3 and Flask. 
```bash
$ alias python=python3 
$ python -m venv python3-virtualenv 
$ source python3-virtualenv/bin/activate 
$ curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py 
$ pip install Flask 
$ export FLASK_ENV=development 
$ flask run 
```
