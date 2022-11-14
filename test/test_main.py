from coursework2_source.app.main1.dao.post_dao import PostDAO
import pytest



@pytest.fixture()
def post_dao():
    post_dao_instance = PostDAO('C:\IT\Training\SkyPro\\3_Course\coursework2_source\data\posts.json')
    return post_dao_instance

key_shoud_be = {'content',
 'likes_count',
 'pic',
 'pk',
 'poster_avatar',
 'poster_name',
 'views_count'}

class TestPostDAO:

    def test_get_all(self, post_dao):
        posts = post_dao.get_posts_all()
        assert type(posts) == list, 'Возвращается не список'
        assert len(posts) > 0, 'Возвращается пустой список'
        assert set(posts[0].keys()) == key_shoud_be, 'неверный список'

    def test_get_post_by_pk(self,post_dao):
        post = post_dao.get_post_by_pk(1)
        assert post['pk'] == 1, 'возвращается неправильный Post'
        assert set(post.keys()) == key_shoud_be, 'неверный список'
