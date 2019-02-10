from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/Users/VivekShetty/PycharmProjects/XpathbySearch/Drivers/chromedriver.exe')
driver.get('http://facebook.com')
driver.find_element_by_xpath("//input[@name='email']").send_keys('vivek')
driver.find_element_by_xpath("//input[@name='pass']").send_keys('test')
driver.find_element_by_xpath("//a[text()='Forgotten account?']").click()