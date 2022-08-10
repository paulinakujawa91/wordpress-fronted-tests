import random
import pytest
from helpers import helpers
from pages.new_post_page import NewPostPage
from pages.posts_page import PostPage
from tests import const


@pytest.mark.usefixtures('setup')
class TestNewPost:
    title = 'New title_unique no:' + str(random.randint(0, 1000))

    def test_correctly_saving_for_title(self):
        new_post = NewPostPage(self.driver)

        new_post.log_in(const.login, const.password)
        new_post.create_new_post()
        new_post.set_post_title(self.title)
        new_post.publish_post()
        post_page = PostPage(self.driver)

        assert self.title == post_page.correct_displayed_data_for_list()

    def test_correctly_saving_for_list(self):
        text1 = 'new text for 1th row unique text no:' + str(random.randint(0, 1000))
        text2 = 'new text for 2nd row unique text no:' + str(random.randint(0, 1000))
        text3 = 'the last text for 3rd row unique text no:' + str(random.randint(0, 1000))
        new_post = NewPostPage(self.driver)

        new_post.log_in(const.login, const.password)
        new_post.create_new_post()
        new_post.set_post_title(self.title)
        new_post.add_block_list()
        new_post.add_item_to_list(text1)
        new_post.add_item_to_list(text2)
        new_post.add_item_to_list(text3)
        new_post.publish_post()
        post_page = PostPage(self.driver)

        assert text1 + '\n' + text2 + '\n' + text3 == post_page.get_data_for_list()

    def test_correctly_saving_for_quote(self):
        quote = 'To be or not to be unique text:' + helpers.get_random_string()
        author = 'WS' + helpers.get_random_string()
        new_post = NewPostPage(self.driver)

        new_post.log_in(const.login, const.password)
        new_post.create_new_post()
        new_post.set_post_title(self.title)
        new_post.add_block_quote(quote, author)
        new_post.publish_post()
        post_page = PostPage(self.driver)

        assert quote == post_page.get_quote()
        assert author == post_page.get_quote_author()
