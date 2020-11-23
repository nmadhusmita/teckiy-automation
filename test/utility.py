from selenium.webdriver.support.ui import Select
import time


class UtilityTool:

    @staticmethod
    def test_sign_out(driver):
        try:
            driver.find_element_by_id("dropdownMenu2").click()
            driver.find_element_by_xpath("/html/body/div[1]/nav/div[3]/form/button").click()
            assert True
        except Exception as e:
            print("Error:: Unable to sign out....", str(e))

    @staticmethod
    def switch_to_new_window(driver):
        new_url = driver.window_handles
        driver.switch_to.window(new_url[0])

    @staticmethod
    def login(driver):
        driver.get("http://teckiydev.herokuapp.com/")
        driver.maximize_window()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("//*[@id=\"navbarResponsive\"]/ul/li[2]/a").click()

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

    @staticmethod
    def login_using_fb_account(driver):
        driver.get("https://teckiydev.herokuapp.com/")
        driver.maximize_window()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/a").click()

    @staticmethod
    def login_with_google_account(driver):
        driver.get("https://teckiydev.herokuapp.com/")
        driver.maximize_window()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/a").click()

    @staticmethod
    def login_with_github_account(driver):
        driver.get("https://teckiydev.herokuapp.com/")
        driver.maximize_window()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/a").click()

        UtilityTool.switch_to_new_window(driver)

        user_name = driver.find_element_by_xpath("//*[@id=\"login_field\"]")

    @staticmethod
    def select_from_dropdown(driver, select_id, visible_text, value):
        select = Select(driver.find_element_by_id(select_id))
        # select by visible text
        select.select_by_visible_text(visible_text)
        # select by value
        select.select_by_value(value)

    @staticmethod
    def switch_to_new_window(driver):
        newURl = driver.window_handles
        driver.switch_to.window(newURl[0])

    @staticmethod
    def find_and_insert_in_text_area(driver, text):
        time.sleep(2)
        frame = driver.find_element_by_class_name("cke_wysiwyg_frame")
        driver.switch_to.frame(frame)
        text_area = driver.find_element_by_xpath("/html/body/p")
        text_area.click()
        text_area.send_keys(text)
