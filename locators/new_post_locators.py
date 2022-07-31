from selenium.webdriver.common.by import By


class NewPostLocators:
    add_new_link = (By.XPATH, '//a[@href="post-new.php"]')
    add_title = (By.XPATH, '//h1[@aria-label="Add title"]')
    add_block = (By.XPATH, '//button[aria-label="Add block"]')
    search_input = (By.ID, "components-search-control-0")
    list_item = (By.ID, "id-57timl-3")
    list_layout = (By.XPATH, "//div[@class='is-root-container block-editor-block-list__layout']")
    publish_button = (By.XPATH, "//button[@class='components-button editor-post-publish-panel__toggle editor-post-publish-button__button is-primary']")
    publish_button_approve = (By.XPATH, "//button[@class='components-button editor-post-publish-button editor-post-publish-button__button is-primary']")
    cancel_button = (By.XPATH, "//button[@class='components-button is-secondary']")
    view_post_link = (By.XPATH, "//a[@class='components-button is-primary']")

