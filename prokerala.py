import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Define the website to scrape and path where the chromedriver is located
website = "https://www.prokerala.com/astrology/past-life/"

# Define 'driver' variable
driver = webdriver.Chrome()
# Open Google Chrome with chromedriver
driver.get(website)

dropdown = Select(driver.find_element(by=By.ID, value="fin_year"))
dropdown.select_by_value('2002')
time.sleep(1)

dropdown = Select(driver.find_element(by=By.ID, value="fin_month"))
dropdown.select_by_visible_text('Jan')
time.sleep(1)

dropdown = Select(driver.find_element(by=By.ID, value="fin_day"))
dropdown.select_by_value('15')
time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR, "#btn-past-life") 
button.click()

time.sleep(5)

# Storing data
text = []
result = driver.find_element(by=By.ID, value="resultDiv")
paragraphs = result.find_elements(by=By.TAG_NAME, value='p')

for paragraph in paragraphs:
    text.append(paragraph.text)

print(text)
