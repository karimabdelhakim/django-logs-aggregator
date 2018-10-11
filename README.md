# django-logs-aggregator
## Installation
$ <code>pip3 install virtualenv</code>  
$ <code>virtualenv -p python3 myenv && cd myenv</code>  
activate virtual environment  
$ <code>source bin/activate</code>  
clone  
$ <code>git clone https://github.com/karimabdelhakim/django-logs-aggregator.git</code>  
$ <code>cd django-logs-aggregator</code>  
install requirements  
$ <code>pip install -r requirements.txt</code>  
$ <code>python manage.py migrate</code>  
$ <code>python manage.py runserver</code>  
## Usage
go to  <link>http://127.0.0.1:8000/</link>  
Register and login then you will be redirected to logs view  
get a token  
$ <code>curl -X POST http://localhost:8000/api/auth/token/ -H 'content-type: application/json' -d '{"username": "myusername","password": "mypass"}'</code>  
example response: <code>{"token":"<token_value>"}</code>  
make a log with token and data  
$ <code>curl -X POST http://localhost:8000/api/logs/create/ -H 'authorization: JWT <your_token>' -H 'content-type: application/json' -d '{ "type": "warning", "message": "some message", "text":"some text" }'</code>  
"type":must be "info", "warning" or "error"  
"message": log message (required)  
"text": optional
