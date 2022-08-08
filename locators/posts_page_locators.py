from selenium.webdriver.common.by import By


class PostsPageLocators:
    post_title = (By.XPATH, '//h1[@class="alignwide wp-block-post-title"]')
    block_list = (By.XPATH, '//div[@class="wp-container-7 entry-content wp-block-post-content"]/ul')
    block_quote_text = (By.XPATH, '//blockquote[@class="wp-block-quote"]/p')
    block_quote_author = (By.XPATH, '//blockquote[@class="wp-block-quote"]/cite')
    block_text = (By.XPATH, '//div[@class="wp-container-7 entry-content wp-block-post-content"]')
    block_img = (By.XPATH, '//figure[@class="wp-block-image size-large"]/img')
