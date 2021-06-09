# Flask-Blog

Site using Flask and Python to display 3 choices of templates for user's to choose from. After choosing a template by preference, user can customize their choice of template for personal portfolio building.
 
 
## Running and Contributing Code


Create a folder titled "templates" in your directory. Place html files in this folder.

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
ENTER the following into the terminal, line by line
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
