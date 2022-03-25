import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# create a Chrome driver instance, specify path to chromedriver file
# # this give DeprecationWarning
# driver = webdriver.Chrome('../chromedriver.exe')

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'------------------------------------')
    print(f'Test start at: {datetime.datetime.now()}')

    # make browser full screen
    driver.maximize_window()
    # give the browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to Advantage Shopping website
    driver.get(locators.adv_shop_cart_url)
    # check that Advantage Shopping URL and the home page title are displayed
    if driver.current_url == locators.adv_shop_cart_url and driver.title == '&nbsp;Advantage Shopping':
        print('Congratulations! Advantage Shopping website launched successfully')
        print(f'Advantage Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(10)
    else:
        print(f'Oops! Advantage Shopping did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        sleep(10)


def teardown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
teardown()