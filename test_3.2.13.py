from selenium import webdriver
import time
import unittest


class TestAsd(unittest.TestCase):
    def test_one(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            inputname = browser.find_element_by_css_selector('.first_block .first')
            inputname.send_keys('qwe')
            inputlastname = browser.find_element_by_css_selector('.first_block .second')
            inputlastname.send_keys('qwe1')
            inputemail = browser.find_element_by_css_selector('.first_block .third')
            inputemail.send_keys('qwe12')
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_two(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            inputname = browser.find_element_by_css_selector('.first_block .first')
            inputname.send_keys('qwe')
            inputlastname = browser.find_element_by_css_selector('.first_block .second')
            inputlastname.send_keys('qwe1')
            inputemail = browser.find_element_by_css_selector('.first_block .third')
            inputemail.send_keys('qwe12')
            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
