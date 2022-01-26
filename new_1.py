from selenium import webdriver
import time 

link = "http://suninjuly.github.io/math.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    import math
    
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_xpath('//div[@class="form-group"]/label/span[2]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector(#answer)
    input1.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
finally:
    time.sleep(10)
    browser.quit()