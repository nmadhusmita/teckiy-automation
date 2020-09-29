from selenium.webdriver.support.ui import Select


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
        driver.get("https://teckiydev.herokuapp.com/")
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
