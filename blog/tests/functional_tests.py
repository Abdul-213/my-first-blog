from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
# browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
browser.get('http://127.0.0.1:8000/')

assert 'Django' in browser.title