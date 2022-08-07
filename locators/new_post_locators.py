from selenium.webdriver.common.by import By


class NewPostLocators:
    menu_posts = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/ul/li[3]/a/div[3]')
    add_new_link = (By.XPATH, '//a[@href="post-new.php"]')
    add_title = (By.XPATH, '//h1[@aria-label="Add title"]')
    add_block = (By.XPATH, '//button[@aria-label="Add block"]')
    search_input = (By.ID, "components-search-control-0")
    list_item = (By.XPATH, "//button[@class='components-button block-editor-block-types-list__item editor-block-list-item-list']")
    list_layout = (By.XPATH, "//div[@class='is-root-container block-editor-block-list__layout']/ul/li")
    quote_item = (By.XPATH, '//span[@class="block-editor-block-types-list__item-title" and contains(.,"Quote")]')
    quote_layout_p = (By.XPATH, '//blockquote[@class="block-editor-block-list__block wp-block is-selected wp-block-quote"]//p')
    quote_layout_cite = (By.XPATH, '//blockquote[@class="block-editor-block-list__block wp-block is-selected wp-block-quote"]//cite')
    img_item = (By.XPATH, '//span[@class="block-editor-block-types-list__item-title" and contains(.,"Image")]')
    button_img = (By.XPATH, '//button[@class="components-button block-editor-media-placeholder__button block-editor-media-placeholder__upload-button is-primary" ]')
    publish_button = (By.XPATH, "//button[@class='components-button editor-post-publish-panel__toggle editor-post-publish-button__button is-primary']")
    publish_button_approve = (By.XPATH, "//button[@class='components-button editor-post-publish-button editor-post-publish-button__button is-primary']")
    cancel_button = (By.XPATH, "//button[@class='components-button is-secondary']")
    view_post_link = (By.XPATH, "//a[@class='components-button is-primary']")