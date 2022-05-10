from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage.
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy peacock feathers' for row in rows),
            'New to-do item did not appear in table')  # add comment because otherwise it is vague

        self.fail('Test finished!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly". (Eidth is very methodical)

# The page updates again, and shows both items on her list.

# Eidth wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her—there is some
# explanatory text to that effect.

# She visits that URL—her to-do list is still there.

# Satisfied, she goes back to sleep.
