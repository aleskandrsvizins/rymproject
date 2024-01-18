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

rating_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openChartTypeSelect();']")
rating_div.click()

option = driver.find_element(By.XPATH, f"//div[@data-description='{rating}']")
option.click()

# time.sleep(5)


# select the type

types = []

def select_release_type(release_type):
    release_type_div = driver.find_element(By.XPATH, f"//div[@onclick=\"RYMchart.toggleReleaseType('{release_type}');\"]")
    release_type_div.click()
    types.append(release_type)

release_type_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openObjectTypeSelect();']")
release_type_div.click()

# unselect beforehand
elements = driver.find_elements(By.CLASS_NAME, "release_type_btn.selected")
for element in elements:
    element.click()

time.sleep(5)


# select releases

select_release_type("album")
select_release_type("ep")
select_release_type("mixtape")

# Click on the close button
close_button = driver.find_element(By.XPATH, "//a[@onclick='RYMchart.closeObjectTypeSelect();']")
close_button.click()

# main_releases_div = driver.find_element(By.XPATH, "//a[@onclick='RYMchart.selectReleaseTypeMain();']")
# main_releases_div.click()
# types.append("Main")

# select_release_type("album")
# select_release_type("ep")
# select_release_type("mixtape")
# select_release_type("djmix")
# select_release_type("single")
# select_release_type("comp")

# if "Main" in types:
#     selected_types = "Main"
# else:
#     selected_types = ", ".join(types)



time.sleep(5)