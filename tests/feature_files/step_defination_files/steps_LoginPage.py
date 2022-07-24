from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager

from behave import *

from utils.LoginPage import LoginPage


@given('I navigate to Free CRN login Page having url "{https://www.freecrm.com/}"')
def navigate_to_url(context, url):
    Login_Page = LoginPage()
    Login_Page.navigate_to_url(url)


@when('I click on login button')
def click_login_button(context):
    context.driver.find_element_by_xpath("//button[@name='login']").click()


@when(' I provide username as "{admin}"')

@then('I verify that homepage is open')
def homepage_displayed(context):
    context.driver.find_element_by_xpath("//title[@name='homepage']").is_displayed()
