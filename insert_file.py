from selenium import webdriver
import os

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/file_input.html")
input1 = browser.find_element_by_css_selector('[name = "firstname"]')
input1.send_keys('qwerty')
input2 = browser.find_element_by_css_selector('[name = "lastname"]')
input2.send_keys('qwerty1')
input3 = browser.find_element_by_css_selector('[name = "email"]')
input3.send_keys('qwerty12')
element = browser.find_element_by_css_selector('#file')
current_dir = os.path.abspath(os.path.dirname('C:\\'))
file_path = os.path.join(current_dir, '1 (2).txt')
element.send_keys(file_path)
button = browser.find_element_by_css_selector('.btn').click()
browser.quit()
