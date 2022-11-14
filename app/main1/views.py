from flask import Blueprint, render_template, request
from .dao.post_dao import PostDAO

catalog_blueprint = Blueprint('catalog_blueprint',__name__, template_folder="templates")
post = PostDAO('C:\IT\Training\SkyPro\\3_Course\coursework2_source\data\posts.json')
comment = PostDAO('C:\IT\Training\SkyPro\\3_Course\coursework2_source\data\comments.json')

@catalog_blueprint.route('/')
def main_page():
    all_posts = post.get_posts_all()
    return render_template('index.html', all_posts=all_posts)

@catalog_blueprint.route('/post/<int:postid>')
def view_post(postid):
    post_pk = post.get_post_by_pk(postid)
    comment_pk = comment.get_comments_by_post_id(postid)
    len_comment = len(comment_pk)

    return render_template('post.html', post_pk=post_pk, comment_pk=comment_pk,
                           len_comment=len_comment,)

@catalog_blueprint.route('/search')
def search_by_post():
    task = request.args.get('s')
    post_search = post.search_for_posts(task)
    count_posts =len(post_search)
    return render_template('search.html', task=task ,post_search=post_search,count_posts=count_posts)


@catalog_blueprint.route('/users/<username>')
def posts_by_username(username):
    search_name = post.get_posts_by_user(username)
    tag_search = post.search_for_tag()
    return render_template('user-feed.html', search_name=search_name, tag_search=tag_search)


@catalog_blueprint.route('/tag/<tagname>')
def search_tag(tagname):
    tag_search = post.search_for_tag()
    post_search = post.search_for_posts(tagname)
    return render_template( 'tag.html', post_search=post_search, tag_search=tag_search,)
