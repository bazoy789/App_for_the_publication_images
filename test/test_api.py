from coursework2_source.app.api.dao.api_post_dao import ApiPostDAO
import pytest

@pytest.fixture()
def api_post_dao():
    api_dao_inctance = ApiPostDAO('C:\IT\Training\SkyPro\\3_Course\coursework2_source\data\posts.json')
    return api_dao_inctance

key_shoud_be = {'content',
'likes_count',
'pic',
'pk',
'poster_avatar',
'poster_name',
'views_count'}

class TestApi:

    def test_api_get_all(self, api_post_dao):
        api_post = api_post_dao.get_posts_all()
        assert type(api_post) == list, 'return not list'
        assert set(api_post[0].keys()) == key_shoud_be, 'key not pattern'


    def test_api_get_pk(self, api_post_dao):
        api_post_pk = api_post_dao.get_post_by_pk(1)
        assert type(api_post_pk) == dict, 'return not dict'
        assert api_post_pk['pk'] == 1, 'not found post != pk'