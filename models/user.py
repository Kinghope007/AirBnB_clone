''' User module class '''
#!/usr/bin/python3
'''
Module for user class
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    class represenating a User
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
