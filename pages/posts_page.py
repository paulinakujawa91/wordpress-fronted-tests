from locators.posts_page_locators import PostsPageLocators


class PostPage:
    def __init__(self, driver):
        self.driver = driver

    def correct_displayed_data_for_list(self):
        return self.driver.find_element(*PostsPageLocators.post_title).text

    def get_data_for_list(self):
        return self.driver.find_element(*PostsPageLocators.block_list).text

    def get_quote(self):
        return self.driver.find_element(*PostsPageLocators.block_quote_text).text

    def get_quote_author(self):
        return self.driver.find_element(*PostsPageLocators.block_quote_author).text
