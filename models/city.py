#!/usr/bin/python3
'''
city module
'''

from models.base_model import BaseModel


class City(BaseModel):
    '''
    Class represeanting city
    '''
    state_id = ""
    name = ""
