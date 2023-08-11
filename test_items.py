import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_should_be_on_the_page(browser):
    #time.sleep(30) #uncomment for test
    browser.get(link)
    button_present = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert button_present, "Button is not present on the page"
