import unittest
import time
from selenium import webdriver
from test.utility import UtilityTool


class PaginationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver85\\chromedriver.exe')
        print("******** Chrome browser opened ********")

    def setUp(self):
        driver = self.driver
        UtilityTool.login(driver)
        print("Logged into teckiydev.herokuapp.com in setUp method")

    '''
      This test case covers the following use case:
      1- Login to teckiy.com 
      2- Search using a keyword
      3- Open a link from the search result
      4- Add a comment to the ticket
    '''
    def test_pagination(self):
        driver = self.driver
        try:
            # Go to 2nd page
            driver.find_element_by_link_text("2").click()
            time.sleep(5)

            # Go to previous page
            driver.find_element_by_link_text("Previous").click()
            time.sleep(5)

            # Go to next page
            driver.find_element_by_link_text("Next").click()
            time.sleep(5)

            # Go to First page
            driver.find_element_by_link_text("First").click()
            time.sleep(5)

            # Go to last page
            driver.find_element_by_link_text("Last").click()
            time.sleep(5)

        except Exception as e:
            print(str(e))
            pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("------- Chrome browser closed ------")

    def tearDown(self):
        self.driver.back()
        UtilityTool.test_sign_out(self.driver)


if __name__ == "__main__":
    unittest.main()
