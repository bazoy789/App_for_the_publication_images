from flask import Blueprint, render_template, request, jsonify
# from dao.bookmarks_dao import

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates', url_prefix='/bookmarks')

@bookmarks_blueprint.route('/add/<posts_id>', methods=['POST'])
def add_bookmarks(posts_id):
    pass

@bookmarks_blueprint.route('/remove/<posts_id>', methods=['POST'])
def remove_bookmarks(posts_id):
    pass