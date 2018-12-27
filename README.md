# REST API Challenge

This repository contains code for a fully functional REST API built with Flask and Elasticsearch.

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
7. That's it! Send a POST request to http://127.0.0.1:5000 using [Postman](https://www.getpostman.com/) or a tool of your choice.

## Running unit tests

In Command Prompt(Windows) or Terminal(mac OS/Linux), while in the active virtual environment, run: 

``` python -m unittest tests.py ```
