# twitter rest integration

This is a software as a service project based on the Twelve-Factor design
https://12factor.net/

1. Factory pattern (create_app) is applied to execute the app as one or 
more stateless processes https://12factor.net/processes
1. Configurations are strictly separated (each env. has seperate config) 
https://12factor.net/config
1. Dependencies are explicitly declared and 
isolated (requirements.txt) https://12factor.net/dependencies
1. Services exported via port 5000 https://12factor.net/port-binding
1. Instant start and graceful shutdown of the app (uwsgi http.ini) 
https://12factor.net/disposability
1. Logging are treated as event streams and 
proper formaters are applied https://12factor.net/logs
1. Oauth2 is implemented to communicate with api.twitter.com.
1. Flask-restx is used for restful services which support 
swagger out of box
1. Tests are written with pytest

#Installation
place an env. file into the root directory within the content below

Directory structure
```python
├── README.md
├── backend
│   ├── __init__.py
│   └── services.py
├── config.py
├── data
├── .env
├── http.ini
├── requirements.txt
├── rest
│   ├── __init__.py
│   └── twitter_namespace.py
├── static
│   └── file.txt
├── templates
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_auth.py
└── wsgi.py

```
Envrionment variables
```.env
API_KEY="*******"
API_SECRET_KEY="*******"
ACCESS_TOKEN="*******"
ACCESS_SECRET="********"
BASE_URL = "https://api.twitter.com/"
URL_AUTH="oauth2/token"
URL_SEARCH="1.1/search/tweets.json"

```

Installation
```python
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uwsgi http.ini

```
Test
```python
python3 $(which py.test)
```


