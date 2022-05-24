from django.test import LiveServerTestCase
from urllib import response
from matplotlib.pyplot import ticklabel_format
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

 # with LiveServerTestCase, you can run test with manage.py (without manually
 # running the server) and separate each test
class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        # 繁！
        # self.assertTrue(
        #     any(row.text == '1. Buy peacock feathers' for row in rows),
        #     f'New to-do item did not appear in table. Contents were:\n{table.text}')  # add comment because otherwise it is vague

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage.
        self.browser.get(self.live_server_url)

        # She notices the page title and header metion to-do lists
        self.assertIn(
            'To-Do', self.browser.title), "Browser title was: " + self.browser.title
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box. (Edith's hobby
        # is trying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly". (Eidth is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and shows both items on her list.
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2. Use peacock feathers to make a fly')



# Eidth wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her—there is some
# explanatory text to that effect.

# She visits that URL—her to-do list is still there.

# Satisfied, she goes back to sleep.
