from flask import Blueprint, render_template, request, jsonify
import logging
from .dao.api_post_dao import ApiPostDAO

api_blueprint = Blueprint('Blueprint', __name__, url_prefix='/api', )
post = ApiPostDAO('C:\IT\Training\SkyPro\\3_Course\coursework2_source\data\posts.json')
log = logging.basicConfig(filename='log/api.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)


@api_blueprint.route('/posts')
def get_all_post():
    all_posts = post.get_posts_all()
    logging.info('Запрос .api/posts')
    return jsonify(all_posts)

@api_blueprint.route('/posts/<int:pk>')
def get_by_pk(pk):
    posts = post.get_post_by_pk(pk)
    logging.info(f'Запрос .api/posts/{pk}')
    return jsonify(posts)

