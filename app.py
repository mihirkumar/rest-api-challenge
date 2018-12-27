from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

max_name_length = 50
max_address_length = 100
max_number_length = 10
max_email_length = 30

#Change this to Elasticsearch's port if not using the default 9200 port.
es_port = 9200 

es = Elasticsearch('http://127.0.0.1:' + str(es_port))

app = Flask(__name__)

@app.route('/')
def default():
    return 'Connection is working.'

@app.route('/contact', methods = ['GET', 'POST'])
def list_create_handler():
    if request.method == 'GET':
        page_size = request.args.get('pageSize', None)
        page = request.args.get('page', None)
        query = request.args.get('query', None)

        return list_all(page_size, page, query)
    
    elif request.method == 'POST':
        contact_name = request.args.get('name', None)
        phone_number = request.args.get('number', None)
        email_id = request.args.get('email', None)
        physical_address = request.args.get('address', None)

        return create(contact_name, phone_number, email_id, physical_address)
    
    else:
        return 'Invalid request.'
    
@app.route('/contact/<name>', methods = ['GET', 'PUT', 'DELETE'])
def search_update_delete_handler(name):
    if request.method == 'GET':
        return search_by_name(name)

    elif request.method == 'PUT':
        contact_name = name
        phone_number = request.args.get('number', None)
        email_id = request.args.get('email', None)
        physical_address = request.args.get('address', None)

        return update(contact_name, phone_number, email_id, physical_address)

    elif request.method == 'DELETE':
        return delete(name)

    else:
        return 'Invalid request.'

if __name__ == '__main__':
    app.run(port = 5000)

# Helper functions

def check_params(contact_name = '', phone_number = '', email_id = '', physical_address = ''):

    # If any length is exceeded we return False to indicate invalid parameters
    if len(str(contact_name)) > max_name_length:
        return 'Contact name is too long.'

    elif len(str(phone_number)) > max_number_length:
        return 'Phone number is too long.'

    elif len(str(email_id)) > max_email_length:
        return 'Email ID is too long.'

    elif len(str(physical_address)) > max_address_length:
        return 'Physical address is too long.'
    
    return True
    
def list_all(page_size = 10, page = 0, query = {}):

    #default values in elasticsearch
    if page_size is None:
        page_size = 10
    elif int(page_size) < 0:
        page_size = 10

    if page is None:
        page = 0
    elif int(page) < 0:
        page = 0
    
    if not (type(query) == dict):
        query = {}

    if int(page) + int(page_size) > 10000:
        return 'Sum of pageSize and page cannot exceed 10,000 according to Elasticsearch specifications.'

    results = es.search(
        index = 'rest_api_mihir',
        doc_type = 'contact',
        from_ = page,
        size = page_size,
        body = query
    )
    
    return jsonify(results)

def create(contact_name, phone_number, email_id, physical_address):
    flag = check_params(contact_name, phone_number, email_id, physical_address)

    if type(flag) == str:
        return flag

    body = {
        'contact_name': contact_name,
        'phone_number': phone_number,
        'email_id': email_id,
        'physical_address': physical_address
    }

    results = es.create(
        index = 'rest_api_mihir',
        doc_type = 'contact',
        id = contact_name,
        body = body
    )
    
    return jsonify(results)

def search_by_name(name):

    flag = check_params(name)

    if type(flag) == str:
        return flag

    results = es.search(
        index = 'rest_api_mihir',
        doc_type = 'contact',
        body = {
            'query': {
                'constant_score':{
                    'filter': {
                        'term': {
                            'contact_name.keyword': name
                        }
                    }
                }
            }
        }
    )

    return jsonify(results)

def update(contact_name, phone_number, email_id, physical_address):

    flag = check_params(contact_name, phone_number, email_id, physical_address)    

    if type(flag) == str:
        return flag
    
    body = {
        'contact_name': contact_name,
        'phone_number': phone_number,
        'email_id': email_id,
        'physical_address': physical_address
    }

    results = es.update(
        index = 'rest_api_mihir',
        doc_type = 'contact',
        id = contact_name,
        body = {
            'doc': body
        }
    )

    return jsonify(results)

def delete(name):

    flag = check_params(name)

    if type(flag) == str:
        return flag
    
    results = es.delete(
        index = 'rest_api_mihir',
        doc_type = 'contact',
        id = name
    )

    return jsonify(results)
