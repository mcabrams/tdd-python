from selenium.webdriver.remote import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest


class NewVisitorTest(unittest.TestCase):
    live_server_url = 'http://web:8000/'

    def setUp(self):
        self.browser = webdriver.WebDriver(
            command_executor="http://selenium:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME
        )

        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_finish_me(self):
        self.browser.get(self.live_server_url)
        self.fail('Finish me!')

if __name__ == '__main__':
    unittest.main()
