from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'tests/chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_check_title(self):
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('Abdulhannan Ahmad', self.browser.title)
        self.fail('Finish the test')
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
        
