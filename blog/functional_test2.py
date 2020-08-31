from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_check_title(self):
        self.browser.get('http://127.0.0.1:8000/blog')

        self.assertIn('Abdulhannadasan Ahmad', self.browser.title)
        header_text = self.browser.find_element_by_id('h1').text
        self.assertIn('Blog Postadss', header_text)

        

        self.fail('Finish the test')
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
        
