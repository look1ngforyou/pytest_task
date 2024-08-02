from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-search-engine-choice-screen")
driver = Chrome(options=options)
wait = WebDriverWait(driver, 10)

URL = "http://the-internet.herokuapp.com/infinite_scroll"
driver.get(url=URL)

LAST_ELEMENT_LOC = (By.XPATH, "//div[contains(@class, 'jscroll-added')][2]")
last_element = wait.until(expected_conditions.presence_of_element_located(LAST_ELEMENT_LOC))
driver.execute_script("arguments[0].scrollIntoView();", last_element)

print("scrolled to 2 paragraph")

LAST_ELEMENT_LOC_1 = (By.XPATH, "//div[contains(@class, 'jscroll-added')][3]")
last_element = wait.until(expected_conditions.presence_of_element_located(LAST_ELEMENT_LOC_1))
driver.execute_script("arguments[0].scrollIntoView();", last_element)

print("scrolled to 3 paragraph")