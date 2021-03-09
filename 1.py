
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox

driver=webdriver.Chrome()
#wait = WebDriverWait(driver, 20)

#driver.implicitly_wait(20) # seconds

#driver.get("http://somedomain/url_that_delays_loading")
#myDynamicElement = driver.find_element_by_id("myDynamicElement")

driver.get('http://www.python.org')

driver.find_element_by_link_text("Documentation").click()

assert 'Python' in driver.title
elem=driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)


#assert "No results found." not in driver.page_source
#assert "No results found." not in driver.page_source
driver.close()
