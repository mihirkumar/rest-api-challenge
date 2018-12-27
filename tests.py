# Importing required modules
import unittest
import random
import string
from flask import Flask, request, jsonify, wrappers
from elasticsearch import Elasticsearch
from app import check_params, list_all, create, search_by_name, update, delete

# Constraints on parameter lengths
end_dump_offset = 4
max_name_length = 50
max_address_length = 100
max_number_length = 10
max_email_length = 30
max_test_length = 100000
max_es_value_page = 10000

#Change this to Elasticsearch's port if not using the default 9200 port.
es_port = 9200 

# Connecting to the running Elasticsearch service
es = Elasticsearch('http://127.0.0.1:' + str(es_port))

# Class containing tests for helper methods
class TestHelperMethods(unittest.TestCase):

    def test_check_params(self):
        # Constructing random parameters for testing
        legal_random_name_size = random.randint(1,max_name_length)
        illegal_random_name_size = random.randint(max_name_length+1, max_test_length)

        legal_random_address_size = random.randint(1,max_address_length)
        illegal_random_address_size = random.randint(max_address_length+1, max_test_length)

        legal_random_number_size = random.randint(1,max_number_length)
        illegal_random_number_size = random.randint(max_number_length+1, max_test_length)

        legal_random_email_size = random.randint(1,max_email_length)
        illegal_random_email_size = random.randint(max_email_length+1, max_test_length)

        legal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_name_size)])
        illegal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_name_size)])

        legal_random_address_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_address_size)])
        illegal_random_address_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_address_size)])

        legal_random_number_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_number_size)])
        illegal_random_number_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_number_size)])

        legal_random_email_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_email_size)])
        illegal_random_email_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_email_size)])

        # Setting return types for legal/illegal requests
        legal_return_type = bool
        illegal_return_type = str
        
        # Test assertions
        self.assertEqual(type(check_params(legal_random_name_string, legal_random_number_string, legal_random_email_string, legal_random_address_string)), legal_return_type)

        self.assertEqual(type(check_params(illegal_random_name_string, legal_random_number_string, legal_random_email_string, legal_random_address_string)), illegal_return_type)

        self.assertEqual(type(check_params(legal_random_name_string, illegal_random_number_string, legal_random_email_string, legal_random_address_string)), illegal_return_type)

        self.assertEqual(type(check_params(legal_random_name_string, legal_random_number_string, illegal_random_email_string, legal_random_address_string)), illegal_return_type)

        self.assertEqual(type(check_params(legal_random_name_string, legal_random_number_string, legal_random_email_string, illegal_random_address_string)), illegal_return_type)

        self.assertEqual(type(check_params(illegal_random_name_string, illegal_random_number_string, illegal_random_email_string, illegal_random_address_string)), illegal_return_type)

    def test_list_all(self):
        # Constructing random parameters for testing
        legal_pageSize_size = random.randint(0,max_es_value_page//2)
        legal_page_size = random.randint(0,max_es_value_page//2)

        illegal_pageSize_size = random.randint(max_es_value_page+1,max_test_length)
        illegal_page_size = random.randint(max_es_value_page+1,max_test_length)

        # Test assertion for too large pageSize and page parameters
        self.assertEqual(list_all(illegal_pageSize_size, illegal_page_size, {}),'Sum of pageSize and page cannot exceed 10,000 according to Elasticsearch specifications.')

        # Getting correct search results from Elasticsearch
        assertion_value = es.search(
            index = 'rest_api_mihir',
            doc_type = 'contact',
            from_ = legal_page_size,
            size = legal_pageSize_size,
            body = {}
        )

        # Test assertion in app context
        with Flask(__name__).app_context():
            self.assertEqual(list_all(legal_pageSize_size, legal_page_size).data[:-end_dump_offset], jsonify(assertion_value).data[:-end_dump_offset])

    def test_create(self):
        # Constructing random parameters for testing
        legal_random_name_size = random.randint(1,max_name_length)
        illegal_random_name_size = random.randint(max_name_length+1, max_test_length)

        legal_random_address_size = random.randint(1,max_address_length)
        illegal_random_address_size = random.randint(max_address_length+1, max_test_length)

        legal_random_number_size = random.randint(1,max_number_length)
        illegal_random_number_size = random.randint(max_number_length+1, max_test_length)

        legal_random_email_size = random.randint(1,max_email_length)
        illegal_random_email_size = random.randint(max_email_length+1, max_test_length)

        legal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_name_size)])
        illegal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_name_size)])

        legal_random_address_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_address_size)])
        illegal_random_address_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_address_size)])

        legal_random_number_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_number_size)])
        illegal_random_number_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_number_size)])

        legal_random_email_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_email_size)])
        illegal_random_email_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_email_size)])

        # Setting return types for legal/illegal requests
        legal_return_type = wrappers.Response
        illegal_return_type = str
        
        # Test assertions in app context
        with Flask(__name__).app_context():
            self.assertEqual(type(create(legal_random_name_string, legal_random_number_string, legal_random_email_string, legal_random_address_string)), legal_return_type)

            self.assertEqual(type(create(illegal_random_name_string, legal_random_number_string, legal_random_email_string, legal_random_address_string)), illegal_return_type)

            self.assertEqual(type(create(legal_random_name_string, illegal_random_number_string, legal_random_email_string, legal_random_address_string)), illegal_return_type)

            self.assertEqual(type(create(legal_random_name_string, legal_random_number_string, illegal_random_email_string, legal_random_address_string)), illegal_return_type)

            self.assertEqual(type(create(legal_random_name_string, legal_random_number_string, legal_random_email_string, illegal_random_address_string)), illegal_return_type)

            self.assertEqual(type(create(illegal_random_name_string, illegal_random_number_string, illegal_random_email_string, illegal_random_address_string)), illegal_return_type)

    def test_search_by_name(self):
        # Constructing random parameters for testing
        legal_random_name_size = random.randint(1,max_name_length)
        illegal_random_name_size = random.randint(max_name_length+1, max_test_length)

        legal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_name_size)])
        illegal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_name_size)])

        # Setting return types for legal/illegal requests
        legal_return_type = wrappers.Response
        illegal_return_type = str
        
        # Test name parameter
        name_to_search = 'testname'

        # Search for the selected name above in Elasticsearch
        assertion_value = es.search(
            index = 'rest_api_mihir',
            doc_type = 'contact',
            body = {
                'query': {
                    'constant_score':{
                        'filter': {
                            'term': {
                                'contact_name.keyword': name_to_search
                            }
                        }
                    }
                }
            }
        )

        # Test assertions in app context
        with Flask(__name__).app_context():
            self.assertEqual(type(search_by_name(legal_random_name_string)), legal_return_type)

            self.assertEqual(type(search_by_name(illegal_random_name_string)), illegal_return_type)

            self.assertEqual(search_by_name(name_to_search).data[:-end_dump_offset], jsonify(assertion_value).data[:-end_dump_offset])

    def test_update(self):
        # Constructing random parameters for testing
        legal_random_address_size = random.randint(1,max_address_length)
        illegal_random_address_size = random.randint(max_address_length+1, max_test_length)

        legal_random_number_size = random.randint(1,max_number_length)
        illegal_random_number_size = random.randint(max_number_length+1, max_test_length)

        legal_random_email_size = random.randint(1,max_email_length)
        illegal_random_email_size = random.randint(max_email_length+1, max_test_length)

        legal_random_address_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_address_size)])
        illegal_random_address_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_address_size)])

        legal_random_number_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_number_size)])
        illegal_random_number_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_number_size)])

        legal_random_email_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_email_size)])
        illegal_random_email_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_email_size)])

        # Setting return types for legal/illegal requests
        legal_return_type = wrappers.Response
        illegal_return_type = str
        
        # Test name parameter
        name_to_update = 'testname'

        # Test assertions in app context
        with Flask(__name__).app_context():
            self.assertEqual(type(update(name_to_update, legal_random_number_string, legal_random_email_string, legal_random_address_string)), legal_return_type)

            self.assertEqual(type(update(name_to_update, illegal_random_number_string, legal_random_email_string, legal_random_address_string)), illegal_return_type)

            self.assertEqual(type(update(name_to_update, legal_random_number_string, illegal_random_email_string, legal_random_address_string)), illegal_return_type)

            self.assertEqual(type(update(name_to_update, legal_random_number_string, legal_random_email_string, illegal_random_address_string)), illegal_return_type)

            self.assertEqual(type(update(name_to_update, illegal_random_number_string, illegal_random_email_string, illegal_random_address_string)), illegal_return_type)

    def test_delete(self):
        # Constructing random parameters for testing
        legal_random_name_size = random.randint(1,max_name_length)
        illegal_random_name_size = random.randint(max_name_length+1, max_test_length)

        legal_random_address_size = random.randint(1,max_address_length)

        legal_random_number_size = random.randint(1,max_number_length)

        legal_random_email_size = random.randint(1,max_email_length)

        legal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_name_size)])
        illegal_random_name_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(illegal_random_name_size)])

        legal_random_address_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_address_size)])

        legal_random_number_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_number_size)])

        legal_random_email_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(legal_random_email_size)])
        
        # Setting return types for legal/illegal requests
        legal_return_type = wrappers.Response
        illegal_return_type = str

        # Test assertions in app context
        with Flask(__name__).app_context():
            create(legal_random_name_string, legal_random_number_string, legal_random_email_string, legal_random_address_string)

            self.assertEqual(type(delete(legal_random_name_string)), legal_return_type)

            self.assertEqual(type(delete(illegal_random_name_string)), illegal_return_type)

# Running all assertions
if __name__ == '__main__':
    unittest.main()