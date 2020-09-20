from selenium import webdriver
import time
import unittest
from utility import UtilityTool


class SignupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver85\\chromedriver.exe')
        print("******** Chrome browser opened in setUpClass method ********")

    def setUp(self):
        driver = self.driver
        driver.get("https://teckiydev.herokuapp.com/")
        print("Opened teckiydev.herokuapp.com in setUp method")

    def test_signup_with_username_password(self):
        driver = self.driver
        # Find the signup button by xpath and click
        driver.find_element_by_xpath("/html/body/div[1]/nav/form[3]/button").click()
        # Navigate to Signup Page
        # element = driver.find_element_by_link_text("Create an Account!")
        # element.click()

        UtilityTool.switch_to_new_window(driver)

        # button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div[3]/button')
        # button.click()

        # fill username in the box
        username = driver.find_element_by_xpath("//*[@id=\"id_email\"]")
        username.clear()
        username.send_keys("nmadhusmita018@gmail.com")
        time.sleep(2)

        # fill password in the box
        password = driver.find_element_by_xpath("//*[@id=\"id_password1\"]")
        password.clear()
        password.send_keys('Devansh@7')
        time.sleep(2)

        # Confirm password in the box
        password = driver.find_element_by_xpath("//*[@id=\"id_password2\"]")
        password.clear()
        password.send_keys('Devansh@7')
        time.sleep(2)

        # click on sign up page
        sign_up_button = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div[3]/button')
        sign_up_button.click()

        time.sleep(5)
        assert True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("------- Chrome browser closed in tearDownClass method ------")

    def tearDown(self):
        self.driver.back()
        print("Navigating back in tearDown method")


if __name__ == "__main__":
    unittest.main()
