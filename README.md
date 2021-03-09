Egyptian national ID validator and data-extractor API

To install the repo files:

$ git clone https://github.com/BasemSrour/Egyptian-national-ID.git to clone the repo

$ cd EgyptianNationalID

$ virtualenv -p python3 envname
or
$ python3 -m venv envname

$ source env/bin/activate

$ pip install -U -r requirements.txt

$ python manage.py migrate

$ python manage.py runserver

open: localhost:8000/id-validator/ in any browser
or
open: localhost:8000/swagger/ in any browser but it is not ready as i expected it to be

Let's move on with localhost:8000/id-validator/
and enter the Egyptian ID number you wanna check its validity
and the response will be a dictionary of 
{
    "number": "29505271202117",
    "validity": "Valid ID number",
    "birth_year": 1995,
    "birth_month": 5,
    "birth_day": 27
}
if the entered number is valid

or
{
    "number": "49616382313228",
    "validity": "Invalid ID number",
    "birth_year": 0,
    "birth_month": 0,
    "birth_day": 0
}
if the entered number is not valid
