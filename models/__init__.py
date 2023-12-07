#!/usr/bin/python3
from models.engine import file_storage
'''
__init__ magic method for models directory
'''

storage = file_storage.FileStorage()
storage.reload()
