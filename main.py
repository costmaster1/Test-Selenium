import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def test_title(driver):
    driver.get('https://docs.pytest.org/en/stable/index.html')
    element = driver.find_element(By.XPATH, '/html/body/div[1]/aside/div/div/div[2]/div/ul[1]/li[1]/a')
    assert driver.title == 'Тест пройден успешно...'

#def test_search_input(driver):
    #driver.get('https://docs.pytest.org/en/stable/index.html')
    #element = driver.find_element(By.XPATH, '//input[@class="arrow__input mini-suggest__input"]')
    #element.send_keys('pytest')



  





    


