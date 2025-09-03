from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.CSS_SELECTOR, "#game #rightPanel #store")

while True:
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > 5:
            print("5 seconds have passed. Stopping execution.")
            break

        cookie.click()
    # implement buy logic

    all_elements = store.find_elements(By.CSS_SELECTOR, "div")
    elements_to_buy = []
    for element in all_elements:
        if element.get_attribute("class") != "grayed":
            elements_to_buy.append(element)

        #elements_to_buy = [element for element in all_elements if element.get_attribute("class") != "grayed"]

    buy = elements_to_buy.pop()
    buy.click()