import os

def create_folders():
    os.makedirs("static")
    os.makedirs("templates")
    with open("app.py", "w") as f:
        f.write("""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
    """)
    with open(".env", "w") as f:
        f.write("""
MONGODB_URI=”YOUR_MONGO_DB_URI”
DB_NAME="YOUR_DB_NAME"
    """)
    with open(".gitignore", "w") as f:
        f.write("""
.gitignore
.env
/venv
    """)
    with open("start.sh", "w") as f:
        f.write("""
set -eu

export PYTHONUNBUFFERED=true

VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
python3 -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

$VIRTUALENV/bin/pip install -r requirements.txt

$VIRTUALENV/bin/python3 app.py
    Footer
        """)
    os.system("python3 -m venv venv")
    os.system("venv\\Scripts\\pip install flask pymongo python-dotenv")

create_folders()

