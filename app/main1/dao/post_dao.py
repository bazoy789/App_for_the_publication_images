import json
from pprint import pprint


class PostDAO:

    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        try:
            with open( self.path, 'r', encoding='UTF-8' ) as file:
                i = json.load( file )
                return i
        except FileNotFoundError:
            return 'Файл не найден'


    def get_posts_by_user(self, user_name: str):
        user_posts = []
        try:
            for post_name in self.get_posts_all():
                if user_name == post_name['poster_name']:
                    if post_name['content'] != '':
                        user_posts.append( post_name )
                    else:
                        return list()
            return user_posts
        except:
            raise ValueError( 'Нет пользователя или нет постов' )


    def get_comments_by_post_id(self, post_id: int):
        comment_one_post = []
        try:
            for comment_post in self.get_posts_all():
                if post_id == comment_post['post_id']:
                    if comment_post['comment'] != '':
                        comment_one_post.append({'commenter_name': comment_post['commenter_name'],
                                                 'comment': comment_post['comment']})
                    else:
                        return list()
            return comment_one_post
        except:
            raise ValueError( 'Нет поста или нет комментарий' )


    def search_for_posts(self, query):
        posts_content = []
        try:
            for search_ in self.get_posts_all():
                if query.lower() in search_['content'].lower():
                    posts_content.append( search_ )
            return posts_content

        except:
            raise ValueError( 'По данному запросу ничего не найдено' )


    def get_post_by_pk(self, pk):
        for post_pk in self.get_posts_all():
            if pk == post_pk['pk']:
                return post_pk
        return f'{pk} - такого поста нет'

    def search_for_tag(self):
        posts_content = []
        try:
            for search_ in self.get_posts_all():
                for i in search_['content'].lower().split( ' ' ):
                    if i[0] == '#':
                        posts_content.append( i )
            return posts_content
        except:
            raise ValueError( 'По данному запросу ничего не найдено' )