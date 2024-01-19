from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
from fpdf import FPDF

import time
import datetime
import random

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

# for url
rating_url = rating.lower()

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

# for url
types = ",".join(s.lower() for s in types)

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

current_year = datetime.datetime.now().year

time_release_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openDateSelect();']")
time_release_div.click()

time.sleep(2)

option = driver.find_element(By.XPATH, f"//div[@data-description='{time_release}']")
option.click()

if time_release == "Year or Decade":

        # select the specific year or decade

        specific_year = "1964"

        date_url = specific_year

        if specific_year.endswith("s"):

            specific_decade = specific_year[:-1]
            decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{specific_decade}")
            decade_row.click()

        else:

            specific_year_cell = driver.find_element(By.ID, f"date_year_chooser_year_{specific_year}")
            specific_year_cell.click()
            
        # Click on the empty space
        div_close = driver.find_element(By.ID, "overlay_invisible")
        div_close.click()
    

elif time_release == "Year range":
        
        # select the year range
        
        start_year = "2024"
        end_year = "2000s"

        start_url = start_year
        end_url = end_year

        # start year
        if start_year.endswith("s"):

            start_decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{start_year[:-1]}")
            start_decade_row.click()

            start_url = start_year[:-1]

        else:

            start_year = driver.find_element(By.ID, f"date_year_chooser_year_{start_year}")
            start_year.click()

    
        # end year
        if end_year.endswith("s"):

            end_decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{end_year[:-1]}")
            end_decade_row.click()

            end_url = end_year[:-1]

        else:

            end_year = driver.find_element(By.ID, f"date_year_chooser_year_{end_year}")
            end_year.click()


        date_url = f"{start_url}-{end_url}"

        if date_url == "1900-1999":
            date_url = "20th_century"

        elif date_url == f"{current_year}-2000":
             date_url = "21st_century"

        else:
            date_url = f"{start_url}-{end_url}"
             

        # Click on the empty space
        div_close = driver.find_element(By.ID, "overlay_invisible")
        div_close.click()


else:
     date_url = time_release.lower()
     pass

time.sleep(2)

# update chart

update_button = driver.find_element(By.XPATH, "//a[@onclick='RYMchart.onClickCreateChart();']")
update_button.click()

time.sleep(10)

# soup is tasty, but not as tasty as soup.find_all()
# soup did not work

# number of releases
num_releases = 2

releases_collected = 0
number = 0
page_num = 1
data = []
    
# fetch and parse data

while releases_collected < num_releases:
    # construct the url
    if page_num == 1:
          url = f"https://rateyourmusic.com/charts/{rating_url}/{types}/{date_url}/"
    else:
         url = f"https://rateyourmusic.com/charts/{rating_url}/{types}/{date_url}/{page_num}/"

    driver.get(url)

    # extract necessary information

    releases = driver.find_elements(By.CLASS_NAME, 'page_charts_section_charts_item')

    for release in releases:

        number += 1

        name = release.find_element(By.CSS_SELECTOR, 'a.page_charts_section_charts_item_link.release').text

        stats_average = release.find_element(By.CLASS_NAME, 'page_charts_section_charts_item_details_average_num').text

        stats_ratings = release.find_element(By.CLASS_NAME, 'page_charts_section_charts_item_details_ratings').text

        artist = release.find_element(By.CSS_SELECTOR, 'a.artist').text

        date = release.find_element(By.CLASS_NAME, 'page_charts_section_charts_item_date').text.replace("Album", "")


        primary_genres = []

        genre_elements = release.find_elements(By.CSS_SELECTOR, '.page_charts_section_charts_item_genres_primary .genre')

        for genre_element in genre_elements:
            primary_genres.append(genre_element.text)
        
        primary_genres = ' / '.join(primary_genres)


        secondary_genres = []

        secondary_genre_elements = release.find_elements(By.CSS_SELECTOR, '.page_charts_section_charts_item_genres_secondary .comma_separated')

        for secondary_genre_element in secondary_genre_elements:
            secondary_genres.append(secondary_genre_element.text)

        secondary_genres = ' / '.join(secondary_genres)

        descriptors = ' / '.join(release.find_element(By.CLASS_NAME, 'page_charts_section_charts_item_genre_descriptors').text.split())


        data.append({
            'Number': number,
            'Name': name,
            'Average': stats_average,
            'Ratings': stats_ratings,
            'Artist': artist,
            'Date': date,
            'Primary Genres': primary_genres,
            'Secondary Genres': secondary_genres,
            'Descriptors': descriptors
        })

        # update the number of releases collected
        releases_collected += len(releases)

    # increment the page number
    page_num += 1

    # wait for 10 to 15 sec, before making the next request
    time.sleep(random.uniform(10, 15))

driver.quit()

df = pd.DataFrame(data)

# save the data
df.to_csv(f"list ranked by {rating_url} rating.csv", index=False)






