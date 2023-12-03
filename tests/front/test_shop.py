import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_product_view_sku():
    """
    Test case WERT-1
    """
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") 
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")

    service = Service()
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url = "https://testqastudio.me/"
    driver.get(url=url)
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()
    sku = driver.find_element(By.CLASS_NAME, value="sku")
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"