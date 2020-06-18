from selenium import webdriver
import time
import os



try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys('My_name')

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys('My_last_name')

    input3 = browser.find_element_by_name("email")
    input3.send_keys('E-mail')

    element = browser.find_element_by_id("file")
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')  
    element.send_keys(file_path)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
