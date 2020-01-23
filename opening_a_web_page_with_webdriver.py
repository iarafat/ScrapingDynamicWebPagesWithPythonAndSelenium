from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get('https://www.pluralsight.com/')
# driver.quit()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://www.pluralsight.com/')
