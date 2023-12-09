#!/usr/bin/python3
from models.base_model import BaseModel
'''
Module for user class
'''


class User(BaseModel):
    '''
    class represenating a User
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
