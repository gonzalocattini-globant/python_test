import os
from selenium import webdriver

chromedriver = "C:\\Users\\gonzalo.cattini\\IdeaProjects\\python_test\\resources\\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

#Add the chorme driver to the instance
driver = webdriver.Chrome(chromedriver)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print ( driver.title )
driver.quit()