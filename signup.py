from selenium import webdriver
import time

class signup:

    def switch_to_new_window(self, driver):
        newURl = driver.window_handles
        driver.switch_to.window(newURl[0])

    def get_chrome_driver(self):
        # Get chrome driver
        driver = webdriver.Chrome("D:\\Code\\chromedriver85\\chromedriver.exe")
        return driver

    def open_site(self):
        # Get the chrome driver and open teckiy.com site.
        driver = self.get_chrome_driver()
        driver.get("https://teckiydev.herokuapp.com/")
        return driver

    def create_an_account(self):
        driver = self.open_site()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("/html/body/div[1]/nav/form[3]/button").click()
        # Navigate to Signup Page
        # element = driver.find_element_by_link_text("Create an Account!")
        # element.click()

        self.switch_to_new_window(driver)

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
        sign_up_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div[3]/button')
        sign_up_button.click()

        time.sleep(20)
        driver.close()

        assert True
        # Test Case: create_an_account in teckiy.com

        # logout from Teckiy
        # logout = driver.find_element_by_id("userNavigationLabel")
        # logout.click()
        # logout1 = driver.find_element_by_class_name("uiLinkButtonInput")  # error in this line
        # logout1.click()
        #
        # time.sleep(5)
        #
        # driver.quit()
sp = signup()
sp.create_an_account()