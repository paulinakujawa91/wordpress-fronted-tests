from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from locators.new_post_locators import NewPostLocators
from tests import const


class AddNewPost(LoginPage):

    def __init__(self,driver):
        LoginPage.__init__(self,driver)

    def new_post_list(self, title , text1, text2, text3):
        self.driver.find_element(*NewPostLocators.menu_posts).click()
        self.driver.find_element(*NewPostLocators.add_new_link).click()
        self.driver.find_element(*NewPostLocators.add_title).send_keys(title)
        self.driver.find_element(*NewPostLocators.add_block).click()
        self.driver.find_element(*NewPostLocators.list_item).click()
        self.driver.find_element(*NewPostLocators.list_layout).send_keys(text1)
        self.driver.find_element(*NewPostLocators.list_layout).send_keys(Keys.ENTER)
        self.driver.find_element(*NewPostLocators.list_layout).send_keys(text2)
        self.driver.find_element(*NewPostLocators.list_layout).send_keys(Keys.ENTER)
        self.driver.find_element(*NewPostLocators.list_layout).send_keys(text3)
        self.driver.find_element(*NewPostLocators.publish_button).click()
        self.driver.find_element(*NewPostLocators.publish_button_approve).click()
        self.driver.find_element(*NewPostLocators.view_post_link).click()

    def new_post_quote(self, title, quote_p, author):
        self.driver.find_element(*NewPostLocators.menu_posts).click()
        self.driver.find_element(*NewPostLocators.add_new_link).click()
        self.driver.find_element(*NewPostLocators.add_title).send_keys(title)
        self.driver.find_element(*NewPostLocators.add_block).click()
        self.driver.find_element(*NewPostLocators.quote_item).click()
        self.driver.find_element(*NewPostLocators.quote_layout_p).send_keys(quote_p)
        self.driver.find_element(*NewPostLocators.quote_layout_cite).send_keys(author)
        self.driver.find_element(*NewPostLocators.publish_button).click()
        self.driver.find_element(*NewPostLocators.publish_button_approve).click()
        self.driver.find_element(*NewPostLocators.view_post_link).click()

    def new_post_imagine(self):
        self.driver.find_element(*NewPostLocators.menu_posts).click()
        self.driver.find_element(*NewPostLocators.add_new_link).click()
        self.driver.find_element(*NewPostLocators.add_title).send_keys(const.title)
        self.driver.find_element(*NewPostLocators.add_block).click()
        self.driver.find_element(*NewPostLocators.img_item).click()
        self.driver.find_element(*NewPostLocators.button_img).click()
        #co dalej?
        self.driver.find_element(*NewPostLocators.publish_button).click()
        self.driver.find_element(*NewPostLocators.publish_button_approve).click()
        self.driver.find_element(*NewPostLocators.view_post_link).click()







