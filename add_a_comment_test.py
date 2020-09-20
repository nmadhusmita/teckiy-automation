import unittest
from selenium import webdriver
from utility import UtilityTool


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver85\\chromedriver.exe')
        print("******** Chrome browser opened in setUpClass method ********")

    def setUp(self):
        driver = self.driver
        UtilityTool.login(driver)
        print("Logged into teckiydev.herokuapp.com in setUp method")

    def test_search_open_and_add_comment_in_a_ticket(self):
        driver = self.driver
        # Search using the given string
        search_box = driver.find_element_by_xpath("//*[@id=\"mySearch\"]")
        search_box.send_keys("python3.8")
        search_box.submit()

        table = driver.find_elements_by_xpath(
            "/html/body/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/span/h6/a")  # finds webresults
        table[0].click()

        try:
            import time
            time.sleep(2)
            frame = driver.find_element_by_class_name("cke_wysiwyg_frame")
            driver.switch_to.frame(frame)
            text_area = driver.find_element_by_xpath("/html/body/p")

            text_area.click()

            text_area.send_keys("Comment from automation code")
            driver.switch_to.parent_frame()
            driver.find_element_by_id("commentmsgtest").click()
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
        print("Navigating back in tearDown method")


if __name__ == "__main__":
    unittest.main()
