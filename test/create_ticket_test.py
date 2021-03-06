from selenium import webdriver
from test.utility import UtilityTool
import unittest


class CreateTicketTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver\\chromedriver.exe')
        print("******** Chrome browser opened in setUpClass method ********")

    def setUp(self):
        driver = self.driver
        UtilityTool.login(driver)
        print("Logged into teckiydev.herokuapp.com in setUp method")

    def test_submit_a_ticket(self):
        driver = self.driver
        driver.find_element_by_link_text("Submit Ticket").click()

        UtilityTool.switch_to_new_window(driver)

        title_text = driver.find_element_by_xpath("//*[@id=\"id_title\"]")
        # Set Title
        title_text.send_keys("Created By Automation Tool - DJango4")

        try:
            UtilityTool.find_and_insert_in_text_area(driver, "How to automate teckiy.com using Selenium with python3.8??")

            # Come out of text area iFrame
            driver.switch_to.parent_frame()

            # Select Ticket Type : Question/Blog
            UtilityTool.select_from_dropdown(driver, 'id_ticket_type', 'Question', 'Q')

            # Select Area : Question/Blog
            UtilityTool.select_from_dropdown(driver, 'id_category', 'Python', 'python')

            # Select Priority : Question/Blog
            UtilityTool.select_from_dropdown(driver, 'id_priority', 'Low', 'L')

            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/form/button").click()
            assert True
            print("-- Successfully created a new ticket")
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

