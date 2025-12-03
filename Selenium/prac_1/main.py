from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")
# options.add_argument(r"user-data-dir=C:\Users\YourUserName\AppData\Local\Google\Chrome\User Data")
# options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
search_box.send_keys("bro code" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Bro code")
link.click()

input("Press Enter to close the browser...")
driver.quit()
