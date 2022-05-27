from selenium import webdriver
import numpy as np
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import random
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.pond5.com/?gclid=Cj0KCQiA3fiPBhCCARIsAFQ8QzXjZrXpb_fO9o5lUVPxOnm0Q58rZxEtMPJWP-HQ3-eGxitYE1vuqwcaArlyEALw_wcB")

urls = []
data = {}
data['a'] = []
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div[4]/div[4]/span"))).click()
time.sleep(5)
username = driver.find_element_by_id('inputLoginModalLogin')
username.send_keys("UPORABNIŠKO IME")
password = driver.find_element_by_id('inputLoginModalPassword')
password.send_keys("GESLO")

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='loginSignupLightbox']/div/div[3]/div/div[2]/button"))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/header/div/div[4]/div[5]/div[1]/a"))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/div[2]/div/div[1]/div[1]/div[4]/a"))).click()
time.sleep(5)
#wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[3]/form/div[2]/a[10]'))).click()
time.sleep(5)
#wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[3]/form/div[2]/a[13]'))).click()

corporateName = ["Success", "Emotion", "Uplifting", "Magical", "Winning", "Greatness"]
corporateName = set(corporateName)
corporate = ["Inspirational", "Upbeat", "Corporate", "Background", "Ambient"]
corporate = set(corporate)
futurebassName = ["Vlog", "Uplifting", "On", "The", "Best", "Happy", "Chill"]
futurebassName = set(futurebassName)
futurebass = ["Future Bass", "Electronic", "Urban", "Groovy", "Vlog", "Background"]
futurebass = set(futurebass)
hiphopName = ["Vlog", "Uplifting", "On", "The", "Best", "Happy", "Chill"]
hiphopName = set(hiphopName)
hiphop = ["Hip Hop", "New York", "Chill", "Nostalgic", "Trip", "Chill", "Vlog"]
hiphop = set(hiphop)
lofiName = ["Vlog", "Uplifting", "On", "The", "Warm", "Happy", "Chill", "Youtube"]
lofiName = set(lofiName)
lofi = ["Lofi", "Hip Hop", "Chill", "Lo-Fi", "Laid Back", "Chill", "Vlog", "Hip"]
lofi = set(lofi)
popName = ["Uplifting", "Pop", "On", "Summer", "Warm", "Happy", "Chill"]
popName = set(popName)
pop = ["Pop", "Fun", "Summer", "Upbeat", "Happy", "Fun"]
pop = set(pop)
rockName = ["Rock", "Up", "Action", "Indie", "Fun", "Action"]
rockName = set(rockName)
rock = ["Trailer ", "Rock", "Action", "Indie", "Sport"]
rock = set(rock)
stompName = ["Hit", "Up", "Drums", "Perc", "Fun", "Action"]
stompName = set(stompName)
stomp = ["Groovy ", "Percussion", "Stomp", "Clap", "Drums", "Typo", "Advertising"]
stomp = set(stomp)
technoName = ["Hard", "Cyber", "Add", "Advert", "Industrial", "Tech"]
technoName = set(technoName)
techno = ["Industrial", "Techno", "Sport", "Cyberpunk", "Action"]
techno = set(techno)
technologyName = ["Future", "Tech", "Technology", "Medical", "Professional", "Tech"]
technologyName = set(technologyName)
technology = ["Minimal", "Technology", "Background", "Corporate", "Tech"]
technology = set(technology)
trailerName = ["Touch", "Inspirational", "Uplifting", "Motivational"]
trailerName = set(trailerName)
trailer = ["Epic", "Inspirational", "Uplifting", "Motivational", "Cinematic"]
trailer = set(trailer)
trapName = ["Trap", "On", "Hard", "Trend"]
trapName = set(trapName)
trap = ["Sport", "Trap", "Hip Hop", "Motivational", "Trendy"]
trap = set(trap)
funkName = ["Beast", "Mode", "Funky", "Trendy", "Groovy", "Funk", "Fun"]
funkName = set(trapName)
funk = ["Fun", "Jazz", "Funk", "Upbeat", "Groovy", "Energetic" ,"Party"]
funk = set(trap)

# Save the window opener (current window, do not mistaken with tab... not the same)
parent = driver.window_handles[0]

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


for x in range(0, 17):
    i = 0
    for row in driver.find_elements_by_class_name('UploadsTable-row'):
        sleep(1)

        if i == 99:
            print(i)
            break

        editButton = row.find_element_by_xpath('.//td[10]/a')
        #driver.execute_script("arguments[0].click();", editButton)
        # Open the link in a new tab by sending key strokes on the element
        # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
        editButton.send_keys(Keys.CONTROL + Keys.RETURN)

        chld = driver.window_handles[1]
        driver.switch_to.window(chld)

        time.sleep(4)
        name = ""

        inputbox = driver.find_element_by_xpath("//*[@id='editClip']/div[1]/div[3]/div/input")
        genre = inputbox.get_attribute('value')
        print(genre)

        if "corporate" in genre.lower():
            print("Found corporate!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(corporateName, numofnames)
            trackAttributes = random.sample(corporate, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)


        elif "future bass" in genre.lower():
            print("future bass!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()
            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(futurebassName, numofnames)
            trackAttributes = random.sample(futurebass, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        elif "hip hop" in genre.lower() or "hip-hop" in genre.lower():
            print("hip hop!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(hiphopName, numofnames)
            trackAttributes = random.sample(hiphop, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        elif "lofi" in genre.lower() or "lo-fi" in genre.lower() or "lo fi" in genre.lower():
            print("lofi!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(lofiName, numofnames)
            trackAttributes = random.sample(lofi, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        elif "pop" in genre.lower():
            print("pop!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(popName, numofnames)
            trackAttributes = random.sample(pop, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        elif "rock" in genre.lower():
            print("rock!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(rockName, numofnames)
            trackAttributes = random.sample(rock, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        elif "stomp" in genre.lower() or "percussion" in genre.lower() or "drums" in genre.lower():
            print("stomp!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(stompName, numofnames)
            trackAttributes = random.sample(stomp, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        elif "techno" in genre.lower() or "cyberpunk" in genre.lower():
            print("techno!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(technoName, numofnames)
            trackAttributes = random.sample(techno, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        elif "technology" in genre.lower():
            print("technology!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(technologyName, numofnames)
            trackAttributes = random.sample(technology, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)


        elif "trailer" in genre.lower():
            print("trailer!")
            driver.implicitly_wait(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(trailerName, numofnames)
            trackAttributes = random.sample(trailer, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)


        elif "trap" in genre.lower():
            print("trap!")
            time.sleep(4)

            inputName = driver.find_element_by_xpath('//*[@id="editClip"]/div[1]/div[3]/div/input')
            inputName.clear()

            numofnames = random.randint(1, 3)
            numofatr = random.randint(3, 5)

            trackName = random.sample(trapName, numofnames)
            trackAttributes = random.sample(trap, numofatr)
            name = ' '.join(trackName) + " (" + ' '.join(trackAttributes) + ")"
            print(name)
            sleep(1)

            inputName.send_keys(name)

            artist = driver.find_element_by_xpath('//*[@id="composer"]')
            artist.clear()
            artist.send_keys("Enhanced Vision")

            sleep(1)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button'):
                elementSUBMIT = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT)

            if check_exists_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button'):
                elementSUBMIT2 = driver.find_element_by_xpath('//*[@id="js_tags"]/div[6]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", elementSUBMIT2)

        driver.close()

        driver.switch_to.window(parent)

        i += 1

    pages = driver.find_elements_by_class_name('Button.Button--transparent.Button--bare.u-paddingH5px')
    driver.execute_script("arguments[0].click();", pages[x+13])



time.sleep(5)

driver.quit()
