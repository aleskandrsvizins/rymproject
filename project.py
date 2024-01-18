from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

# set up the driver
driver = webdriver.Chrome()
driver.get("https://rateyourmusic.com/charts/")

# wait for the page to load
wait = WebDriverWait(driver, 10)

# click on the consent button
consent_button = driver.find_element(By.XPATH, "//p[contains(text(), 'Consent')]")
consent_button.click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "page_charts_settings_summary")))
           
# select the rating
# make it user-defined
rating = "Popular"

rating_div = driver.find_element(By.XPATH, "//div[@class = 'page_chart_query_item page_chart_query_item_type_selector']")
rating_div.click()

time.sleep(5)

option = driver.find_element(By.XPATH, f"//div[@data-description='{rating}']")
option.click()

time.sleep(5)


