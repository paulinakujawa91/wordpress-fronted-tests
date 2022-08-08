from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from locators.new_post_locators import NewPostLocators


class AddNewPost(LoginPage):

    def __init__(self, driver):
        LoginPage.__init__(self, driver)

    def new_post_title(self, title):
        self.driver.find_element(*NewPostLocators.menu_posts).click()
        self.driver.find_element(*NewPostLocators.add_new_link).click()
        self.driver.find_element(*NewPostLocators.add_title).send_keys(title)

    def add_block_list(self):
        self.driver.find_element(*NewPostLocators.add_block).click()
        self.driver.find_element(*NewPostLocators.list_item).click()

    def publish_post(self):
        self.driver.find_element(*NewPostLocators.publish_button).click()
        self.driver.find_element(*NewPostLocators.publish_button_approve).click()
        self.driver.find_element(*NewPostLocators.view_post_link).click()

    def add_item_to_list(self, item):
        self.driver.find_element(*NewPostLocators.list_layout).send_keys(item)
        self.driver.find_element(*NewPostLocators.list_layout).send_keys(Keys.ENTER)

    def add_block_quote(self, quote_p, author):
        self.driver.find_element(*NewPostLocators.add_block).click()
        self.driver.find_element(*NewPostLocators.quote_item).click()
        self.driver.find_element(*NewPostLocators.quote_layout_p).send_keys(quote_p)
        self.driver.find_element(*NewPostLocators.quote_layout_cite).send_keys(author)
