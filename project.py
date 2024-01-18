from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# set up the driver
driver = webdriver.Chrome()
driver.get("https://rateyourmusic.com/charts/")

# wait for the page to load
wait = WebDriverWait(driver, 20)

# click on the consent button
consent_button = driver.find_element(By.XPATH, "//p[contains(text(), 'Consent')]")
consent_button.click()

time.sleep(2)

# wait for the advert to load
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ad-close-button")))

# close the advert
close_button = driver.find_element(By.CLASS_NAME, "ad-close-button")
close_button.click()


wait.until(EC.presence_of_element_located((By.CLASS_NAME, "page_charts_settings_summary")))
           
# select the rating
# make it user-defined
rating = "Popular"

rating_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openChartTypeSelect();']")
rating_div.click()

option = driver.find_element(By.XPATH, f"//div[@data-description='{rating}']")
option.click()

time.sleep(2)


# select the type

types = []

release_type_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openObjectTypeSelect();']")
release_type_div.click()

# unselect beforehand
button = driver.find_element(By.CLASS_NAME, "release_type_btn.selected")
button.click()

time.sleep(3)

def select_release_type(release_type):
    release_type_div = driver.find_element(By.XPATH, f"//div[@onclick=\"RYMchart.toggleReleaseType('{release_type}');\"]")
    release_type_div.click()
    types.append(release_type)


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

time.sleep(2)

# select year

time_release = "Year range"

if time_release == "Year or Decade" or "Year range":

    time_release_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openDateSelect();']")
    time_release_div.click()

    time.sleep(5)

    option = driver.find_element(By.XPATH, f"//div[@data-description='{time_release}']")
    option.click()

    if time_release == "Year or Decade":

        # select the specific year or decade
        specific_year = "1964"

        if specific_year.endswith("s"):

            specific_decade = specific_year[:-1]
            decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{specific_decade}")
            decade_row.click()

        else:

            specific_year_cell = driver.find_element(By.ID, f"date_year_chooser_year_{specific_year}")
            specific_year_cell.click()

    

    elif time_release == "Year range":
        # select the year range
        
        start_year = "1967"
        end_year = "2000s"


        # start year
        if start_year.endswith("s"):

            start_decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{start_year[:-1]}")
            start_decade_row.click()

        else:

            start_year = driver.find_element(By.ID, f"date_year_chooser_year_{start_year}")
            start_year.click()

    
        # end year
        if end_year.endswith("s"):

            end_decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{end_year[:-1]}")
            end_decade_row.click()

        else:

            end_year = driver.find_element(By.ID, f"date_year_chooser_year_{end_year}")
            end_year.click()

    time.sleep(2)
    close_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Close')]")
    close_button.click()

else:
    pass

time.sleep(10)

