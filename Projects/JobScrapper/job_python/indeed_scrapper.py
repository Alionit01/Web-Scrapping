from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/python-jobs/?currentJobId=4326690738&originalSubdomain=pk")

time.sleep(15)

titles = driver.find_elements(By.CSS_SELECTOR, "h2.jobTitle")

for t in titles:
    print(t.text)
