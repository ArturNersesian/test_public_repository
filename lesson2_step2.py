from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, '[id="treasure"]')
    number = treasure.get_attribute("valuex")
    print(number)
    answer = calc(number)
    print(answer)
    input1 = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
    input1.send_keys(answer)

    option1 = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # 2 секунды чтоб посмотреть что мы ввели в поля
    button.click()

    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()