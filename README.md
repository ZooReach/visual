To run the application

python3 -m venv localenv

source localenv/bin/activate

pip install -r requirements.txt

FLASK_APP=flaskr:app FLASK_DEBUG=1 python -m flask run