from selenium import webdriver
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    
    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    sum01 = str((int(x)+int(y)))
    
    #один вариант через css селектор
    #browser.find_element_by_css_selector("[value='" + sum01 + "']").click()
    
    #второй через поиск по тексту суммы
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum01)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()