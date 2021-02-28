from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass

PATH = "..\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/")


username = input("Username: ")
password = getpass.getpass()
captchaSol = 0

try:

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    element.send_keys(username)

    element = driver.find_element_by_id("password")
    element.send_keys(password)

    element = driver.find_element_by_id("login").text.split("\n")[3].split()
    if("add" in element):
        captchaSol = int(element[element.index("add") + 1]) + int(element[element.index("add") + 3])
    elif("subtract" in element):
        captchaSol = int(element[element.index("subtract") + 1]) - int(element[element.index("subtract") + 3])    
    elif("first" in element):
        captchaSol = int(element[element.index("first") + 2]) 
    elif("second" in element):
        captchaSol = int(element[element.index("second") + 4])

    element = driver.find_element_by_id("valuepkg3")
    element.clear()
    element.send_keys(captchaSol)

    element = driver.find_element_by_id("loginbtn")
    element.click()

except TimeoutException:
    driver.quit()
    print("Failed to load the site. Please try again")