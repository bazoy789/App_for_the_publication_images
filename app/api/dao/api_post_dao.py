import json
from pprint import pprint


class ApiPostDAO:

    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        try:
            with open( self.path, 'r', encoding='UTF-8' ) as file:
                data_json = json.load( file )
                return data_json
        except FileNotFoundError:
            return 'Файл не найден'


    def get_post_by_pk(self, pk):
        for post_pk in self.get_posts_all():
            if pk == post_pk['pk']:
                return post_pk
        return f'{pk} - такого поста нет'
