# -*- coding: utf-8 -*-
__author__ =  "olenji"
'''
    date    :2016-11-2 17:20
    function:   测式selenium
                如果再lunix无ui系统 需要使用 pyvirtualdisplay 不燃会报错
    py_version  : 2.7
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(driver.current_url)
print(driver.page_source)
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()
display.stop()
