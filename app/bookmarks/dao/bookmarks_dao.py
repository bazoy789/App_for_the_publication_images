from flask import jsonify, json

class Bookmarks_dao:

    def __init__(self, post):
        self.post = post

    def reat_file(self):
        with open( self.post, 'r', encoding='UTF-8' ) as file:
            return json.load(file)

    def save_bookmarks_post(self, post):
        with open(self.post, 'w', encoding='UTF-8') as file:
            json.dump(post,file, ensure_ascii=False)

    def remove_bookmarks_post(self, post):
        bookmarks_remove =  self.reat_file()
        bookmarks_remove.remove(post)
        self.save_bookmarks_post( bookmarks_remove )


    def add_bookmarks_post(self, post):
        bookmarks = self.reat_file()
        bookmarks.append(post)
        self.save_bookmarks_post(bookmarks)
