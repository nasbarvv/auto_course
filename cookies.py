#Задание 1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://google.com')
browser.maximize_window()


cookie = {'name': 'username', 'value': 'user123'}
browser.add_cookie(cookie)

browser.refresh()

# Получаем и выводим значение куки "username"
cookie_value = browser.get_cookie('username')['value']
print("Значение куки 'username':", cookie_value)

# Закрываем браузер
browser.quit()

#Задание 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://vk.com')
browser.maximize_window()


cookie = {'name': 'username', 'value': 'user13'}
browser.add_cookie(cookie)

browser.refresh()

# Получаем и выводим значение куки "username"
cookie_value = browser.get_cookie('username')['value']
print("Значение куки 'username':", cookie_value)

browser.refresh()

browser.delete_cookie('username')

if browser.get_cookie('username') is None:
    print ("Куки успешно удалены")

# Закрываем браузер
browser.quit()



