# Flask-Blog

Flask site using HTML and Python to introduce 3 members of the Production Engineering Fellowship.
 
 
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
