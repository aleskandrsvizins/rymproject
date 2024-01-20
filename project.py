from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import math

import time
import datetime
import random
import re

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# select the rating
# make it user-defined

print("")

rating_option = input("Rate by:\n[1] Top \033[90m(As determined by users' ratings)\033[0m\n[2] Popular \033[90m(Most number of ratings)\033[0m\n[3] Esoteric \033[90m(Relatively unknown but with high average ratings)\033[0m\n[4] Diverse \033[90m(Artists are limited to one entry per chart)\033[0m\n[5] Bottom \033[90m(As determined by users' ratings)\033[0m\nChoose an option: ")

if rating_option == "1":
    rating = "Top"
elif rating_option == "2":
    rating = "Popular"
elif rating_option == "3":
    rating = "Esoteric"
elif rating_option == "4":
    rating = "Diverse"
elif rating_option == "5":
    rating = "Bottom"
else:
    print("Invalid option. Defaulting to Top.")
    rating = "Top"

print("")

print("Chosen rating option:", rating, "rating")

print("")

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# select type
    
release_types = {
    
    '1': {'name': 'Album', 'selected': False},
    '2': {'name': 'EP', 'selected': False},
    '3': {'name': 'Mixtape', 'selected': False},
    '4': {'name': 'DJ Mix', 'selected': False},
    '5': {'name': 'Single', 'selected': False},
    '6': {'name': 'Compilation', 'selected': False},
    '7': {'name': 'All', 'selected': False}
}

user_input = ""  # Add a default value for user_input

def print_release_types():
    for key, value in release_types.items():
        print(f"[{'x' if value['selected'] else ' '}] [{key}]: {value['name']}")

# User input for release types
        
while True:

    print_release_types()

    print("")

    print("Select a release type by entering the corresponding number. Press Enter when done.")

    print("")

    user_input = input().strip()

    if user_input == "":
        break

    if user_input == "7":
        for value in release_types.values():
            value['selected'] = True

    if user_input in release_types:
        release_types[user_input]['selected'] = not release_types[user_input]['selected']

    selected_types = [value['name'].lower().replace(' ', '') if value['name'].lower() != 'compilation' else 'comp' for value in release_types.values() if value['selected']]
    

    print("")

    print("\033[96mSelected types:", selected_types, "\033[0m")

    print("")

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# select date
start_year = ""
end_year = ""
start_decade = ""    
end_decade = ""

    
print("[1] All-time (charts from all time)")
print("[2] Specific year or decade (for example '1984', '2010s')")
print("[3] Year-range (for example '1984-2016')")

print("")

time_option = input("Select a time option by entering the corresponding number: ").strip()

print("")

if time_option == "1":

    print("Selected time option: All-time")
    time_release = "All-time"

elif time_option == "2":
 
    time_input = input("Enter a specific year or decade: ").strip()
    time_release = "Year or Decade"

    print("")

    if re.match(r"^\d{4}$", time_input):
        # Single year
        print("Selected time option: Specific year")
        print("")
        print("Year:", time_input)

    elif re.match(r"^\d{4}s$", time_input):
        # Decade
        print("Selected time option: Specific decade")
        print("")
        print("Decade:", time_input)

    else:
        print("Invalid input. Defaulting to All-time.")
        print("")
        time_option = "1"

else:

    # Year-range option

    time_input = input("Enter a year range (e.g., '1984-2016'): ").strip()
    time_release = "Year range"

    print("")
    
    if re.match(r"^\d{4}-\d{4}$", time_input):

        # Valid year range

        start_year, end_year = time_input.split("-")

        print("Selected time option: Year-range")
        print("")
        print("Start Year:", start_year)
        print("End Year:", end_year)

    elif re.match(r"^\d{4}s-\d{4}$", time_input):

        # Valid decade range
        start_decade, end_year = time_input.split("-")
        start_year = start_decade[:-1] + "s"
        print("Selected time option: Decade-range")
        print("")
        print("Start Decade:", start_year)
        print("End Year:", end_year)

    elif re.match(r"^\d{4}-\d{4}s$", time_input):
        
        # Valid decade range
        start_year, end_decade = time_input.split("-")
        print("Selected time option: Decade-range")
        print("")
        print("Start Year:", start_year)
        print("End Decade:", end_decade[:-1] + "s")

    elif re.match(r"^\d{4}s-\d{4}s$", time_input):
        # Valid decade range
        start_decade, end_decade = time_input.split("-")
        start_year = start_decade[:-1] + "s"
        end_year = end_decade[:-1] + "s"
        print("Selected time option: Decade-range")
        print("")
        print("Start Decade:", start_decade)
        print("End Decade:", end_decade)

    else:
        print("Invalid input. Defaulting to All-time.")
        time_option = "1"

print("")

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# select number of releases

number_releases = input("Enter the number of releases to be \033[33mcollected\033[0m: ").strip()

print("")

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

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

# wait for the element to appear and then remove it
# def remove_element(driver):
#    element = driver.find_element(By.CLASS_NAME, 'connatix_video')
#    driver.execute_script("""
#    var element = arguments[0];
#    element.parentNode.removeChild(element);
#    """, element)
#    return True

# wait.until(remove_element)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "page_charts_settings_summary")))

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# RATING

rating_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openChartTypeSelect();']")
rating_div.click()

option = driver.find_element(By.XPATH, f"//div[@data-description='{rating}']")
option.click()

time.sleep(2)

# for url
rating_url = rating.lower()

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# TYPE

types = []

release_type_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openObjectTypeSelect();']")
release_type_div.click()

# unselect beforehand
button = driver.find_element(By.CLASS_NAME, "release_type_btn.selected")
button.click()

time.sleep(2)

def select_release_type(release_type):
    release_type_div = driver.find_element(By.XPATH, f"//div[@onclick=\"RYMchart.toggleReleaseType('{release_type}');\"]")
    release_type_div.click()
    types.append(release_type)


# select releases

for release_type in selected_types:
    select_release_type(release_type)


# Click on the close button
close_button = driver.find_element(By.XPATH, "//a[@onclick='RYMchart.closeObjectTypeSelect();']")
close_button.click()

# for url
types = ",".join(s.lower() for s in types)

time.sleep(2)

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# DATE

current_year = datetime.datetime.now().year

time_release_div = driver.find_element(By.XPATH, "//div[@onclick='RYMchart.openDateSelect();']")
time_release_div.click()

time.sleep(2)

option = driver.find_element(By.XPATH, f"//div[@data-description='{time_release}']")
option.click()

if time_release == "Year or Decade":

        date_url = time_input

        if time_input or int(time_input[:-1]) < 1950:

            date_year_chooser_toggle = driver.find_element(By.CLASS_NAME, "date_year_chooser_toggle")
            date_year_chooser_toggle.click()

            time.sleep(2)

            if time_input.endswith("s"):

                specific_decade = time_input[:-1]
                decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{specific_decade}")
                decade_row.click()

            else:

                specific_year_cell = driver.find_element(By.ID, f"date_year_chooser_year_{time_input}")
                specific_year_cell.click()

        else:
            
            if time_input.endswith("s"):

                specific_decade = time_input[:-1]
                decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{specific_decade}")
                decade_row.click()

            else:

                specific_year_cell = driver.find_element(By.ID, f"date_year_chooser_year_{time_input}")
                specific_year_cell.click()
            
        # Click on the empty space
        div_close = driver.find_element(By.ID, "overlay_invisible")
        div_close.click()
    

elif time_release == "Year range":
        
        # select the year range

        start_url = start_year
        end_url = end_year

        # start year

        if start_year or int(start_decade[:-1]) < 1950:

            date_year_chooser_toggle = driver.find_element(By.CLASS_NAME, "date_year_chooser_toggle")
            date_year_chooser_toggle.click()

            time.sleep(2)

        if start_decade.endswith("s"):

            start_decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{start_decade[:-1]}")
            start_decade_row.click()

            start_url = start_decade[:-1]

        else:
            start_year = driver.find_element(By.ID, f"date_year_chooser_year_{start_year}")
            start_year.click()

        # end year
                
        if end_year or int(end_decade[:-1]) < 1950:

            date_year_chooser_toggle = driver.find_element(By.CLASS_NAME, "date_year_chooser_toggle")
            date_year_chooser_toggle.click()

            time.sleep(2)

        if end_decade.endswith("s"):

            end_decade_row = driver.find_element(By.ID, f"date_year_chooser_decade_{end_decade[:-1]}")
            end_decade_row.click()
            
            end_url = end_decade[:-1]

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

# ══════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹════════════⊹⊱≼≽⊰⊹══════

# update chart

update_button = driver.find_element(By.XPATH, "//a[@onclick='RYMchart.onClickCreateChart();']")
update_button.click()

time.sleep(5)

# soup is tasty, but not as tasty as soup.find_all()
# soup did not work

# RELEASES


releases_collected = 0

number_releases = int(number_releases)

num_pages = math.ceil(number_releases / 40.0)

number_order = 0

data = []
    
# fetch and parse data
for page_num in range(1, num_pages + 1):

    if releases_collected <= number_releases:
        
        # construct the url
        url = f"https://rateyourmusic.com/charts/{rating_url}/{types}/{date_url}/{page_num if page_num > 1 else ''}/"

        driver.get(url)

        # extract necessary information

        releases = driver.find_elements(By.CLASS_NAME, 'page_charts_section_charts_item')

        releases_to_process = min(number_releases, 40)
        
        for release in releases[:releases_to_process]:

            releases_collected += 1

            number_order += 1

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
                'Number': number_order,
                'Name': name,
                'Average': stats_average,
                'Ratings': stats_ratings,
                'Artist': artist,
                'Date': date,
                'Primary Genres': primary_genres,
                'Secondary Genres': secondary_genres,
                'Descriptors': descriptors
            })

        # update the number of releases left
        number_releases -= releases_to_process

        # wait for 10 to 15 sec, before making the next request
        time.sleep(random.uniform(10, 15))

driver.quit()

df = pd.DataFrame(data)

# save the data
df.to_csv(f"list ranked by {rating_url} rating {date_url}.csv", index=False)

print("🫲 here is your clean file. enjoy.")






