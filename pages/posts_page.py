from locators.posts_page_locators import PostsPageLocators


class PostPage:
    def __init__(self,driver):
        self.driver = driver

    def correct_dispayled_data_for_list(self):
        return self.driver.find_element(*PostsPageLocators.post_title).text
