from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from locators.categories_page_locators import CategoriesPageLocators
from pages.login_page import LoginPage


class CategoriesPage(LoginPage):

    def __init__(self, driver):
        LoginPage.__init__(self, driver)

    def open_category_view(self):
        self.driver.find_element(*CategoriesPageLocators.menu_posts).click()
        self.driver.find_element(*CategoriesPageLocators.categories_link).click()

    def add_new_category(self, category, slug, parent_category):
        self.driver.find_element(*CategoriesPageLocators.name_input).send_keys(category)
        self.driver.find_element(*CategoriesPageLocators.slug_input).send_keys(slug)

        select = Select(self.driver.find_element(*CategoriesPageLocators.parent_category_select))
        select.select_by_visible_text(parent_category)

        self.driver.find_element(*CategoriesPageLocators.save_button).click()

    def edit_category_name(self, old_category_name, new_category_name):
        self.driver.find_element(*CategoriesPageLocators.search_input).send_keys(old_category_name)
        self.driver.find_element(*CategoriesPageLocators.search_submit).click()
        self.hover_over_category_name()
        self.driver.find_element(*CategoriesPageLocators.edit_link).click()
        self.driver.find_element(*CategoriesPageLocators.edit_name_input).clear()
        self.driver.find_element(*CategoriesPageLocators.edit_name_input).send_keys(new_category_name)
        self.driver.find_element(*CategoriesPageLocators.update_button).click()

    def delete_category(self, category):
        self.driver.find_element(*CategoriesPageLocators.search_input).send_keys(category)
        self.driver.find_element(*CategoriesPageLocators.search_submit).click()
        self.hover_over_category_name()
        self.driver.find_element(*CategoriesPageLocators.delete_link).click()
        self.accept_delete()

    def is_category_exists(self, category):
        self.driver.find_element(*CategoriesPageLocators.search_input).send_keys(category)
        self.driver.find_element(*CategoriesPageLocators.search_submit).click()
        return not self.driver.find_elements(*CategoriesPageLocators.msg_not_found)

    def is_category_updated(self):
        return self.driver.find_element(*CategoriesPageLocators.edit_msg).is_displayed()

    def is_category_deleted(self, category):
        self.driver.find_element(*CategoriesPageLocators.search_input).send_keys(category)
        self.driver.find_element(*CategoriesPageLocators.search_submit).click()
        return self.driver.find_elements(*CategoriesPageLocators.msg_not_found)

    def hover_over_category_name(self):
        element_to_hover_over = self.driver.find_element(*CategoriesPageLocators.category_item_name)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def accept_delete(self):
        alert = self.driver.switch_to.alert
        alert.accept()
