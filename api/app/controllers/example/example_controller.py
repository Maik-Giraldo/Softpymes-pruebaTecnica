# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from app.exception import InternalServerError
from app import db
from app.models.example.example_model import ExampleModel
from app.schemas.example.example_schema import examples


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def get_all():
        result = ExampleModel.query.paginate(0,19, False)
        try:
            response = {
                'info': {
                    'current_page': 0,
                    'next': 1,
                    'prev': None
                },
                'data': examples.dump(result.items)
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def get_page(page):
        result = ExampleModel.query.paginate(int(page), 20, False)
        try:
            next = 0
            
            if (int(page) + 1)* 20 > result.total:
                if result.total - (int(page) + 1) * 20 > 0 and result.total - (int(page) + 1) * 20 <= 20:        
                    next = int(page) + 1
                else:
                    next = None
            else:
                if result.total % 20 == 0:
                    if (int(page) + 1 ) * 20 < result.total:
                        next = int(page) + 1
                    else:
                        next = None
                else:
                    if result.total - (int(page) + 1) * 20 > 0 and result.total - (int(page) + 1) * 20 <= 20: 
                        next = int(page) + 1
                    else:
                        next = None
            response = {
                'info': {
                    'current_page': page,
                    'next':  next,
                    'prev':  int(page) - 1 if int(page) - 1 > 0 else  None 
                },
                'data': examples.dump(result.items)
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)