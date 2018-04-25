'''
This file is used to list lambda functions and event mappings
'''
from libs.aws_lambda import *


def module_lambda_list_functions():
    list_functions()


def module_lambda_list_event_source_mappings():
    list_event_source_mappings()


def module_lambda_get_function(*text):
    '''
    get specfied function. Takes function name from list_functions and region the function exists in
    python3 weirdAAL.py -m lambda_get_function -a 'MY_LAMBDA_FUNCTION','us-west-2' -t yolo
    '''
    lambda_get_function(text[0][0], text[0][1])


def module_lambda_get_account_settings():
    '''
    Returns a customer's account settings.
    '''
    lambda_get_account_settings()
