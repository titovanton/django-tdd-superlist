import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class HomePageTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = '/usr/bin/google-chrome-stable'
        options.add_argument('--headless')
        options.add_argument('--visible=0')
        options.add_argument('--window-size=800x600')
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://10.0.2.15:8000')
        self.assertIn('To-Do', self.browser.title)
        h1 = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', h1.text)
        inputbox = self.browser.find_element_by_id('id-new-item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys('\n')


if __name__ == '__main__':
    unittest.main()
