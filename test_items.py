import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_presence(browser):
    browser.get(link)
    time.sleep(30)
	# search button
    add_to_cart_button = WebDriverWait(browser, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
    )

    # test
    assert add_to_cart_button.is_displayed(), "Button is not on a page."
