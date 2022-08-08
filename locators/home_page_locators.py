from selenium.webdriver.common.by import By


class HomePageLocators:
    home_page_header = (By.XPATH, '//div[@class="welcome-panel-header"]')
    posts_button = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/ul/li[3]/a/div[3]')
    categories_button = (By.XPATH, '//a[@href="edit-tags.php?taxonomy=category"]')
