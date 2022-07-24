from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager


class LoginPage:

    def navigate_to_url(url):
        driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
        driver.get(url)


