from selenium import webdriver


options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('headless')
options.add_argument('visible=0')
options.add_argument('window-size=800x600')
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)

driver.get('http://localhost:8000')
assert 'Django' in driver.title
