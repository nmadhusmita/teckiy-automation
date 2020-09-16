from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Basic_Automation:

    def __init__(self):
        pass

    def select_from_dropdown(self, driver, select_id, visible_text, value):
        select = Select(driver.find_element_by_id(select_id))
        # select by visible text
        select.select_by_visible_text(visible_text)
        # select by value
        select.select_by_value(value)

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

    def submit_ticket(self):
        driver = self.login()
        driver.find_element_by_link_text("Submit Ticket").click()

        self.switch_to_new_window(driver)

        title_text = driver.find_element_by_xpath("//*[@id=\"id_title\"]")
        # Set Title
        title_text.send_keys("Created By Automation Tool - DJango1")

        try:
            import time
            time.sleep(5)
            frame = driver.find_element_by_class_name("cke_wysiwyg_frame")
            driver.switch_to.frame(frame)
            text_area = driver.find_element_by_xpath("/html/body/p")

            text_area.click()

            text_area.send_keys("How to automate teckiy.com using Selenium with python3.8??")

            driver.switch_to.parent_frame()

            # Select Ticket Type : Question/Blog
            self.select_from_dropdown(driver, 'id_ticket_type', 'Question', 'Q')

            # Select Area : Question/Blog
            self.select_from_dropdown(driver, 'id_category', 'Python', 'P')

            # Select Priority : Question/Blog
            self.select_from_dropdown(driver, 'id_priority', 'Low', 'L')

            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/button").click()

            assert True
        except Exception as e:
            print(str(e))
            pass
        return driver


    def search_question_or_blog(self, search_str):
        driver = self.submit_ticket()

        # Click on the login button
        search_box = driver.find_element_by_xpath("//*[@id=\"mySearch\"]")
        search_box.send_keys(search_str)
        search_box.submit()

        table = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/span/h6/a")  # finds webresults
        table[0].click()
        print("After clicking the search link")

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
        except Exception as e:
            print(str(e))
            pass


        return driver


    def log_out(self):
        driver = self.search_question_or_blog("python3.8")
        assert True


if __name__ == '__main__':
    auto = Basic_Automation()
    auto.search_question_or_blog("python3.8")
    # auto.log_out()

