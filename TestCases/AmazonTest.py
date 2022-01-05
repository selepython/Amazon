import time

from selenium import webdriver
import unittest
import HtmlTestRunner
import sys

sys.path.append("C://Users/Muzamil Pasha/PycharmProjects/AmazonProject")

from Pages.AmazonPage import AmazonPage


class AmazonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Muzamil Pasha\\PycharmProjects\\AmazonProject\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_amazon_valid(self):
        driver = self.driver

        driver.get("https://www.amazon.in/")

        amazon = AmazonPage(driver)
        amazon.enter_username("Wrist Watches")
        amazon.click_search()
        amazon.click_analog()
        amazon.click_leather()
        amazon.click_titan()
        amazon.click_discount()
        amazon.click_fifth()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))
