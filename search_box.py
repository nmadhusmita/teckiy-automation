from selenium import webdriver


class Basic_Automation:

    def __init__(self):
        pass

    def get_chrome_driver(self):
        # Get chrome driver

        driver = webdriver.Chrome("D:\\Code\\chromedriver_84\\chromedriver.exe")
        return driver

    def open_site(self):
        # Get the chrome driver and open teckiy.com site.
        driver = self.get_chrome_driver()
        driver.get("https://teckiydev.herokuapp.com/")
        return driver

    def login(self, browser=None):
        driver = self.open_site()
        # Find the Login button by xpath and click
        driver.find_element_by_xpath("//*[@id=\"navbarsExampleDefault\"]/button/a").click()

        # fill username in the box
        username = driver.find_element_by_xpath("//*[@id='id_login']")
        username.clear()
        username.send_keys("nmadhusmita018@gmail.com")

        # fill password in the box
        password = driver.find_element_by_xpath("//*[@id='id_password']")
        password.clear()
        password.send_keys('Devansh@7')

        # Click on the login button
        login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[3]/button')
        login_button.click()
        assert True

        newURl = driver.window_handles
        driver.switch_to.window(newURl[0])

        search_data = driver.find_element_by_xpath("//*[@id=\"mySearch\"]").send_keys("Django").click()

        assert True

    def type_on_search_box(self, search_str):
        self.login()
        driver = self.get_chrome_driver()
        search_str = driver.find_element_by_xpath("//*[@id=\"mySearch\"]").send_keys(search_str).click()
        # return driver


auto = Basic_Automation()
auto.login()
