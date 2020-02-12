# django_test
Technical Test for Django login and api endpoint. 

# register user
User registration can be via api or by graphic interface

Method: POST
Params: username,password
url:register/
example: curl -X POST -d 'username=acoto@mail.com&password=147852' http://localhost:8000/register/

# get auth token
with the username and passworg the user can generate the access_token

Method: POST
Params: username, password, grant_type, client_id
example: curl -X POST -d 'username=acoto@mail.com&password=741&grant_type=password&client_id=acoto@mail.com' http://localhost:8000/oauth2/access_token/

# Access user model
With the access_toke the client can access the user data model.

Method: GET
example: curl -X GET -H 'Content-Type: application/json' -H 'Authorization: bearer 463abb6ff5fceab6d0d98a654637c156da260040' http://localhost:8000/umodel/

The access_token is used in request header.

# For run the test.

1- Clone the repository
git clone https://github.com/acoto/django_test.git

2-Create python virtualenv
virtualenv -p python2 venv

3- Activate virtual environment
source venv/bin/activate

4- Intall python requirements
pip install -r requirements.txt

5- Migrate apps and databases
python manage.py migrate

6- Run the server
python manage.py runserver

7- Go to application
127.0.0.1:8000/

The web application contains the routes and forms for: Login, Logout, Registration



