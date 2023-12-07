''' BaseModel Class '''
import uuid
from datetime import datetime


class BaseModel:
    '''
    A class that defines all common attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''
        initializing of the BaseModel
        args:
        kwargs: wont be used
        '''
        self.id = str(uuid.uuid4())
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        '''
        return string representation of the BaseModel
        '''
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''
        update the public instance attribute with time
        '''
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        '''
        return a dictionary representation of all instances
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict["email"] = self.email
        obj_dict["password"] = self.password
        obj_dict["first_name"] = self.first_name
        obj_dict["last_name"] = self.last_name
        return obj_dict
