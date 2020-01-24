from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chromeOptions = Options()
chromeOptions.add_argument('--kiosk')

driver = webdriver.Chrome(options=chromeOptions)
driver.get('https://www.premierleague.com/')

players_ele = driver.find_element_by_link_text('Players').click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'search-input')))
search_ele = driver.find_element_by_id('search-input')
search_ele.send_keys('Weyne Rooney')
search_ele.send_keys(Keys.RETURN)

# button_ele = driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/header/div/div[1]/div/div[@role='button']").click()

# time.sleep(1)

driver.implicitly_wait(5)
click_wayne = driver.find_element_by_xpath("//img[@data-player='p13017']").click()

page_source_overview = driver.page_source



