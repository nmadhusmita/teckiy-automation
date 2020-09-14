import unittest
from selenium import webdriver
import time

driver = webdriver.Chrome()




if __name__ == '__main__':
    unittest.main()



    class Basic_Automation:

        def __init__(self):
            pass

        def get_chrome_driver(self):
            # Get chrome driver
            driver = webdriver.Chrome("C:\\Users\\madhu\\Downloads\\chromedriver_84\\chromedriver.exe")
            return driver

        def open_site(self):
            # Get the chrome driver and open teckiy.com site.
            driver = self.get_chrome_driver()
            driver.get("https://teckiydev.herokuapp.com/")
            return driver

        def create_an_account(self):
            driver = self.open_site()
            # Find the Login button by xpath and click
            driver.find_element_by_xpath("//*[@id=\"navbarsExampleDefault\"]/button/a").click()
            # Navigate to Signup Page
            element = driver.find_element_by_link_text("Create an Account!")
            element.click()

            button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div[3]/button')
            button.click()

            # fill username in the box
            username = driver.find_element_by_xpath("//*[@id='id_login']")
            username.clear()
            username.send_keys("nmadhusmita018@gmail.com")
            time.sleep(2)

            # fill password in the box
            password = driver.find_element_by_id("//*[@id='id_password1']")

            password.clear()
            password.send_keys('Devansh@7')
            time.sleep(2)

            # Confirm password in the box
            password = driver.find_element_by_xpath("//*[@id='id_password2']")
            password.clear()
            password.send_keys('Devansh@7')
            time.sleep(2)

            # click on sign up page
            sign_up_button = driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div[3]/button')
            sign_up_button.click()

            time.sleep(20)
            driver.close()

            # Test Case: create_an_account in teckiy.com


    auto = Basic_Automation()
    auto.create_an_account()

    # # Reads password from a text file because
    # # it's silly to save the password in a script.
    # with open('password.txt', 'r') as myfile:
    #        Password = myfile.read().replace('\n', '')
    #
    # time.sleep(1)
    # # click on Terms and Conditions
    # toc = driver.find_element_by_name('terms_and_conditions')
    # toc.click()

    #

