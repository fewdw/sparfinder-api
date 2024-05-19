ACTIVATE VENV
source myenv/bin/activate

DEACTIVATE VENV
deactivate

FREEZE REQUIREMENTS
pip freeze > requirements.txt

INSTALL REQUIREMENTS
pip install -r requirements.txt

RUN SERVER
python3 server.py

