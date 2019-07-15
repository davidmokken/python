import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.imdb.com"


driver = webdriver.Chrome()
driver.get(url)
element = driver.find_element_by_id("navbar-query")

# Needs imput/name movie from (created)program
element.send_keys("some text")
element.send_keys(Keys.ENTER)


# driver.quit()

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()