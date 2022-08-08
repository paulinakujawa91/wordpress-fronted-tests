import random
import pytest
from helpers import helpers
from pages.new_post_page import AddNewPost
from pages.posts_page import PostPage
from tests import const


@pytest.mark.usefixtures('setup')
class TestNewPost:

    def test_correctly_saving_for_title(self):
        add_new_post = AddNewPost(self.driver)
        add_new_post.log_in(const.login, const.password)
        title = 'New title_unique no:' + str(random.randint(0, 1000))
        add_new_post.new_post_title(title)
        add_new_post.publish_post()
        post_page = PostPage(self.driver)
        assert title == post_page.correct_displayed_data_for_list()

    def test_correctly_saving_for_list(self):
        add_new_post = AddNewPost(self.driver)
        add_new_post.log_in(const.login, const.password)
        title = 'New title for list'
        text1 = 'new text for 1th row unique text no:' + str(random.randint(0, 1000))
        text2 = 'new text for 2nd row unique text no:' + str(random.randint(0, 1000))
        text3 = 'the last text for 3rd row unique text no:' + str(random.randint(0, 1000))
        add_new_post.new_post_title(title)
        add_new_post.add_block_list()
        add_new_post.add_item_to_list(text1)
        add_new_post.add_item_to_list(text2)
        add_new_post.add_item_to_list(text3)
        add_new_post.publish_post()
        post_page = PostPage(self.driver)
        assert text1 + '\n' + text2 + '\n' + text3 == post_page.get_data_for_list()

    def test_correctly_saving_for_quote(self):
        add_new_post = AddNewPost(self.driver)
        add_new_post.log_in(const.login, const.password)
        title = 'New title_unique no:' + str(random.randint(0, 1000))
        quote = 'To be or not to be unique text:' + helpers.get_random_string()
        author = 'WS' + helpers.get_random_string()
        add_new_post.new_post_title(title)
        add_new_post.add_block_quote(quote, author)
        add_new_post.publish_post()
        post_page = PostPage(self.driver)
        assert quote == post_page.get_quote()
        assert author == post_page.get_quote_author()
