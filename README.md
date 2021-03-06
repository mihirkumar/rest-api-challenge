# REST API Challenge

This repository contains code for a fully functional REST API built with Flask and Elasticsearch that supports storage and retrieval of contacts.

## Running the API

In Command Prompt(Windows) or Terminal(mac OS/Linux), run: 
1. ```git clone https://github.com/mihirkumar/rest-api-challenge.git```
2. ```cd rest-api-challenge```
3. Activate the virtual environment provided in rest-api-challenge/virtual_environment/ . Steps for doing so will depend on the operating system. In Windows, run ```cd virtual_environment\venv\Scripts``` followed by ```activate```. Steps for other operating systems can be found at https://virtualenv.pypa.io/en/latest/.
4. Run ```pip install flask elasticsearch```.
5. Run ```pip list```. The following packages should be installed. If not, please install them.
* Click (7.0)
* elasticsearch (6.3.1)
* Flask (1.0.2)
* itsdangerous (1.1.0)
* Jinja2 (2.10)
* MarkupSafe (1.1.0)
* pip (9.0.1)
* setuptools (28.8.0)
* urllib3 (1.24.1)
* Werkzeug (0.14.1)
6. In Command Prompt, run ``` set flask = app.py ``` followed by ``` flask run ```. This will start a server serving the API at http://127.0.0.1:5000 .
7. That's it! Send a POST request to http://127.0.0.1:5000 using [Postman](https://www.getpostman.com/) or a tool of your choice. Please also make sure Elasticsearch is running.

## Running unit tests

In Command Prompt(Windows) or Terminal(mac OS/Linux), while in the active virtual environment, run: 

``` python -m unittest tests.py ```

## Supported requests with format

The following requests are supported by this API:
* ```GET /contact?pageSize={}&page={}&query={}``` : This will return all contacts matching the query. If the query is empty, returns all contacts stored.
* ```POST /contact?name=test&number=1234567890&email=test@test.com&address=Vienna``` : This will create a new contact with provided details.
* ```GET /contact/{name}``` : This will return the contact by a unique name provided in the request.
* ```PUT /contact/{name}?name=test&number=1234567890&email=test@test.com&address=Vienna``` : This will update the unique contact of provided name. Errors if contact is not found.
* ```DELETE /contact/{name}``` : This will delete the unique contact of provided name. Errors if contact is not found.

## Parameter Constraints

Every contact must abide by the following constraints:
* Name should be at most 50 characters.
* Phone number should be at most 10 characters.
* Email ID should be at most 30 characters.
* Address should be at most 100 characters.

Please keep these constraints in mind while making requests to the API.
