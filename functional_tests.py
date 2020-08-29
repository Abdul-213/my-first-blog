from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_check_title(self):
        self.browser.get('http://127.0.0.1:8000/blog')

        self.assertIn('Abdulhannan Ahmad', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Blog Posts', header_text)
        self.fail('Finish the test')
        
    def test_can_add_new_post(self):
        self.browser.get('http://127.0.0.1:8000/post/new/')

        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('New post', header_text)
        self.fail('Finish the test')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
        
