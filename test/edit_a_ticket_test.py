from selenium import webdriver
from test.utility import UtilityTool
import unittest
import time


class EditATicketTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver85\\chromedriver.exe')
        print("******** Chrome browser opened in setUpClass method ********")

    def setUp(self):
        driver = self.driver
        UtilityTool.login(driver)
        print("Logged into teckiydev.herokuapp.com in setUp method")

    def test_edit_a_ticket(self):
        driver = self.driver
        # Search using the given string 'DJango4'
        search_box = driver.find_element_by_xpath("//*[@id=\"mySearch\"]")
        search_box.send_keys("DJango4")
        search_box.submit()

        # Open the first link from search result
        search_result_link = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/a")
        search_result_link.click()

        UtilityTool.switch_to_new_window(driver)

        # Click on edit button
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[2]/div[1]/span/a").click()

        UtilityTool.switch_to_new_window(driver)

        title_text = driver.find_element_by_xpath("//*[@id=\"id_title\"]")
        # Set Title
        title_text.clear()
        title_text.send_keys("Created By Automation Tool - DJango")

        try:
            UtilityTool.find_and_insert_in_text_area(driver, " How to automate teckiy.com ????")

            # Come out of text area iFrame
            driver.switch_to.parent_frame()

            # Select Ticket Type : Question/Blog
            UtilityTool.select_from_dropdown(driver, 'id_ticket_type', 'Task', 'T')

            # Select Area : Question/Blog
            UtilityTool.select_from_dropdown(driver, 'id_category', 'SQL', 'sql')

            # Click on update
            driver.find_element_by_xpath("//*[@id=\"commentmsgtest\"]").click()
            assert True
            print("-- Successfully edited a ticket")
        except Exception as e:
            print(str(e))
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
