import random
import pytest
from pages.login_page import LoginPage
from pages.new_post_page import AddNewPost
from pages.posts_page import PostPage
from tests import const


@pytest.mark.usefixtures('setup')
class TestNewPost:

    def test_new_post_list(self):
        add_new_post = AddNewPost(self.driver)
        add_new_post.log_in(const.login, const.password)

        title = 'New title_unique no:' + str(random.randint(0, 1000))
        text1 = 'new text for 1th row'
        text2 = 'new text for 2nd row'
        text3 = 'the last text for 3rd row'
        add_new_post.new_post_list(title , text1, text2, text3)

        post_page = PostPage(self.driver)
        assert title == post_page.correct_dispayled_data_for_list()
