from selenium.webdriver.common.by import By


class CategoriesPageLocators:
    menu_posts = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/ul/li[3]/a/div[3]')
    categories_link = (By.XPATH, '//a[@href="edit-tags.php?taxonomy=category"]')
    name_input = (By.ID, "tag-name")
    slug_input = (By.ID, "tag-slug")
    parent_category_select = (By.ID, "parent")
    save_button = (By.ID, "submit")
    category_item_name = (By.XPATH, '//td[@data-colname="Name"]')
    edit_link = (By.XPATH, '//div[@class="row-actions"]/span[@class="edit"]')
    edit_name_input = (By.ID, "name")
    edit_msg = (By.ID, "message")
    description = (By.ID, "description")
    update_button = (By.XPATH, '//input[@class="button button-primary"]')
    search_input = (By.ID, "tag-search-input")
    search_submit = (By.ID, "search-submit")
    msg_not_found = (By.XPATH, '//td[contains(., "No categories found.")]')
    delete_link = (By.XPATH, '//a[@class="delete-tag aria-button-if-js"]')