from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3777054484&f_AL=true&f_WT=2&geoId=102713980&keywords=marketing&location=India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
time.sleep(5)

login = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn")
login.click()

username = driver.find_element(By.ID, "username")
username.send_keys("my_email")

password = driver.find_element(By.ID, "password")
password.send_keys("my_password")

signin = driver.find_element(By.CLASS_NAME, "btn__primary--large")
signin.click()

time.sleep(5)
save_job = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save_job.click()

