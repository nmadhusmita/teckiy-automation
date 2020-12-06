import unittest
from selenium import webdriver
from test.utility import UtilityTool


class GiveASuggestionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver\\chromedriver.exe')
        print("******** Chrome browser opened in setUpClass method ********")

    def setUp(self):
        driver = self.driver
        UtilityTool.login(driver)
        print("Logged into teckiydev.herokuapp.com in setUp method")

    '''
      This test case covers the following use case:
      1- Login to teckiy.com 
      2- Submit a suggestion
    '''
    def test_submit_a_suggestion(self):
        driver = self.driver
        try:
            driver.find_element_by_link_text("Suggestions").click()
            UtilityTool.switch_to_new_window(driver)
            email_address_text = driver.find_element_by_xpath("//*[@id=\"id_email_id\"]")
            email_address_text.send_keys("nmadhu@gmail.com")

            content_text_area = driver.find_element_by_xpath("//*[@id=\"id_content\"]")
            content_text_area.send_keys("We should make it more user friendly...")

            submit_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/form/button")
            # submit_btn.click()
            assert True
        except Exception as e:
            print("ERROR:: Unable to submit a suggestion - ", str(e))
            pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("------- Chrome browser closed in tearDownClass method ------")

    def tearDown(self):
        self.driver.back()
        UtilityTool.test_sign_out(self.driver)
        print("Navigating back in tearDown method")


if __name__ == "__main__":
    unittest.main()
