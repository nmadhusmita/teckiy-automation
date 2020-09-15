import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Basic_Automation:

    def __init__(self):
        pass

    def get_chrome_driver(self):
        # Get chrome driver
        driver = webdriver.Chrome("D:\\Code\\chromedriver85\\chromedriver.exe")
        return driver

    def open_site(self):
        # Get the chrome driver and open teckiy.com site.
        driver = self.get_chrome_driver()
        driver.get("https://teckiydev.herokuapp.com/")
        return driver

    def login(self, browser=None):
        driver = self.open_site()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("/html/body/div[1]/nav/form[2]/button").click()

        # fill username in the box
        username = driver.find_element_by_xpath("//*[@id='id_login']")
        username.clear()
        username.send_keys("nmadhusmita018@gmail.com")

        # fill password in the box
        password = driver.find_element_by_xpath("//*[@id='id_password']")
        password.clear()
        password.send_keys('Devansh@7')

        login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[3]/button')
        login_button.click()

        return driver

    def search_question_or_blog(self, search_str):
        driver = self.login()
        # Click on the login button

        search_box = driver.find_element_by_xpath("//*[@id=\"mySearch\"]")
        search_box.send_keys(search_str)
        search_box.submit()

        table = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/span/h6/a")  # finds webresults
        table[0].click()

        # body = driver.find_element_by_xpath("//*[@id=\"cke_id_comment\"]")
        # body.click()
        # body.send_keys("teckiy")
        # assert True
        return driver


    def log_out(self):
        driver = self.search_question_or_blog("Python")
        # logout = driver.find_element_by_id("dropdownMenuButton").
        #
        # driver.find_element_by_xpath("//*[@id=\"navbarsExampleDefault\"]/div/div/a")
        #//*[@id="navbarsExampleDefault"]/div/form
        #//*[@id="navbarsExampleDefault"]/div
        ##navbarsExampleDefault > div > div > form > input[type=hidden]
        assert True


    def create_an_account(self):
        driver = self.open_site()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("//*[@id=\"navbarsExampleDefault\"]/button/a").click()
        # Navigate to Signup Page
        element = driver.find_element_by_link_text("Create an Account!")
        element.click()

        newURl = driver.window_handles
        driver.switch_to.window(newURl[0])

        button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[2]/form/div[3]/button')
        button.click()

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


auto = Basic_Automation()
auto.log_out()
# auto.search_question_or_blog("Python")

# Test Case: Login To teckiy.com
# auto = Basic_Automation()
# auto.login()
