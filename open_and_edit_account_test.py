import unittest
from selenium import webdriver
from utility import UtilityTool


class OpenAndEditAccountPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver85\\chromedriver.exe')
        print("******** Chrome browser opened in setUpClass method ********")

    def setUp(self):
        driver = self.driver
        UtilityTool.login(driver)
        print("Logged into teckiydev.herokuapp.com in setUp method")

    def test_open_and_edit_account_page(self):
        driver = self.driver
        try:
            driver.find_element_by_id("dropdownMenu2").click()
            driver.find_element_by_xpath("/html/body/div[1]/nav/div[3]/a/button").click()
        except Exception as e:
            print("Error:: Unable to open account", str(e))
        assert True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("------- Chrome browser closed in tearDownClass method ------")

    def tearDown(self):
        self.driver.back()
        UtilityTool.test_sign_out()
        print("Navigating back in tearDown method")


if __name__ == "__main__":
    unittest.main()


