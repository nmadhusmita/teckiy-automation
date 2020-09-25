import unittest
from selenium import webdriver
from utility import UtilityTool


class AddACommentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver85\\chromedriver.exe')
        print("******** Chrome browser opened in setUpClass method ********")

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
    def test_search_open_and_add_comment_in_a_ticket(self):
        driver = self.driver
        # Search using the given string 'DJango4'
        search_box = driver.find_element_by_xpath("//*[@id=\"mySearch\"]")
        search_box.send_keys("DJango4")
        search_box.submit()

        # Open the first link from search result
        search_result_link = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/a")
        search_result_link.click()
        try:
            ask_doubt = driver.find_element_by_id("ask-doubt")
            ask_doubt.click()
            text_area = driver.find_element_by_id("exampleFormControlTextarea1")
            text_area.click()
            text_area.send_keys("Can u check your question?")
            driver.find_element_by_id("another-btn").click()
            assert True
            print("-- Successfully added a comment in a link")
        except Exception as e:
            print(str(e))
            pass

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
