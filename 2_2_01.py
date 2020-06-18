from selenium import webdriver
import time
import math
#def calc(sum01):
  #return (int(x)+int(y))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    
    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    sum01 = str((int(x)+int(y)))

    browser.find_element_by_css_selector("[value='" + sum01 + "']").click()
    #from selenium.webdriver.support.ui import Select
    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_visible_text('%s' % sum01)
	

    #input1 = browser.find_element_by_id("answer")
    #input1.send_keys(calc(x))

    #option1 = browser.find_element_by_id("robotCheckbox")
    #option1.click()

    #option1 = browser.find_element_by_id("robotsRule")
    #option1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()