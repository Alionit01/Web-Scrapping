from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://duckduckgo.com/?q=orteil+dashnet+cookie+clicker")

wait = WebDriverWait(driver, 15)

links = driver.find_element(By.PARTIAL_LINK_TEXT, "Cookie Clicker")
links.click()
accept = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cc_btn.cc_btn_accept_all")))
accept.click()
time.sleep(5)
english = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#langSelect-EN")))
english.click()
# # Use XPath to locate any visible input[type='text']
# search_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @name='q']")))
#
# search_box.send_keys("smily emoji" + Keys.ENTER)
# links = driver.find_element(By.PARTIAL_LINK_TEXT, "Smiley")
# links.click()

# results
results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.result__a")))
print(f"Found {len(results)} results.")

input("Press Enter to close the browser...")
driver.quit()
