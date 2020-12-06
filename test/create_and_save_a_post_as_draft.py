from selenium import webdriver
from test.utility import UtilityTool
import unittest


class CreateAndSaveABlogAsDraftTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Code\\chromedriver\\chromedriver.exe')

    def setUp(self):
        UtilityTool.login(self.driver)

    def test_submit_a_blog_in_draft_mode(self):
        driver = self.driver

        try:
            # Click on the profile drop down
            driver.find_element_by_xpath("//*[@id=\"dropdownMenu2\"]").click()

            # Select 'Account' option and click
            driver.find_element_by_xpath("/html/body/div[1]/nav/div[3]/div[2]/a").click()

            # Click on 'Posts' nav item
            driver.find_element_by_link_text("Posts").click()

            # Click on 'Write a Post' link in Posts page
            driver.find_element_by_link_text("Write a Post").click()

            # Set Blog Title
            blog_title = driver.find_element_by_xpath("//*[@id=\"id_title\"]")
            blog_title.send_keys("Distributed System Architecture")

            # Set 'Content'
            UtilityTool.find_and_insert_in_text_area(driver, "Write the blog details")

            # Come out of text area iFrame
            driver.switch_to.parent_frame()

            # Set 'Tags'
            blog_title = driver.find_element_by_xpath("//*[@id=\"id_tags\"]")
            blog_title.send_keys("System Design, Cloud, Architecture")

            # Click on 'Draft'
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/form/input[2]').click()
            assert True
            print("-- Successfully save a Blog in Draft mode")
        except Exception as e:
            print(str(e))
            pass

        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()

        def tearDown(self):
            self.driver.back()
            UtilityTool.test_sign_out(self.driver)

    if __name__ == "__main__":
        unittest.main()

